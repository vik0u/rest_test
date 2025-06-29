import os
import shutil
import random
import argparse
import numpy as np
from PIL import Image
from tqdm import tqdm
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
import albumentations as A

INPUT_DIR = "images"
CLASSES_FILE = "images/classes.txt"
OUTPUT_DIR = "dataset"
NUM_WORKERS = 4
TRAIN_RATIO = 0.7
VAL_RATIO = 0.2
TEST_RATIO = 0.1
AUGMENT_COUNT = 2

# --- Создаём папки ---
os.makedirs(os.path.join(OUTPUT_DIR, "images", "train"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "labels", "train"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "images", "val"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "labels", "val"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "images", "test"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "labels", "test"), exist_ok=True)

# --- Чтение классов ---
with open(CLASSES_FILE, "r", encoding="utf-8") as f:
    classes = [line.strip() for line in f if line.strip()]
classes = list(OrderedDict.fromkeys(classes))  # Удаляем дубликаты

# --- Аугментации (Albumentations) ---
train_transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=15, p=0.3),
    A.Blur(blur_limit=3, p=0.1),
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels'], min_area=1, min_visibility=0.1))

def augment_and_save(img_path, label_path, output_img_dir, output_label_dir, augment_count):
    try:
        image = np.array(Image.open(img_path))
        img_height, img_width = image.shape[:2]

        with open(label_path, 'r') as f:
            lines = [line.strip().split() for line in f]
            bboxes = []
            class_labels = []

            for line in lines:
                if len(line) < 5:
                    continue

                class_id = int(line[0])
                bbox = list(map(float, line[1:5]))

                # Нормализуем bbox
                normalized_bbox = normalize_bbox(bbox, img_width, img_height)

                # Проверяем, что bbox валиден после нормализации
                if normalized_bbox[2] > 0 and normalized_bbox[3] > 0:
                    bboxes.append(normalized_bbox)
                    class_labels.append(class_id)

        if not bboxes:
            print(f"Нет валидных bbox в {label_path}, пропускаем")
            return

        base_name = os.path.splitext(os.path.basename(img_path))[0]

        # Сохраняем оригинальное изображение
        shutil.copy(img_path, os.path.join(output_img_dir, f"{base_name}.jpg"))
        shutil.copy(label_path, os.path.join(output_label_dir, f"{base_name}.txt"))

        # Аугментируем augment_count раз
        for i in range(augment_count):
            try:
                transformed = train_transform(
                    image=image,
                    bboxes=bboxes,
                    class_labels=class_labels
                )
                aug_image = transformed["image"]
                aug_bboxes = transformed["bboxes"]
                aug_labels = transformed["class_labels"]

                aug_img_path = os.path.join(output_img_dir, f"{base_name}_aug{i}.jpg")
                aug_label_path = os.path.join(output_label_dir, f"{base_name}_aug{i}.txt")

                Image.fromarray(aug_image).save(aug_img_path)
                with open(aug_label_path, 'w') as f:
                    for label, bbox in zip(aug_labels, aug_bboxes):
                        f.write(f"{label} {' '.join(map(str, bbox))}\n")
            except Exception as e:
                print(f"Ошибка при аугментации {img_path} (попытка {i + 1}): {str(e)}")
                continue

    except Exception as e:
        print(f"Ошибка при обработке {img_path}: {str(e)}")

# --- Функция для проверки и нормализации bbox ---
def normalize_bbox(bbox, img_width, img_height):
    """Нормализует координаты bbox к диапазону [0, 1]"""
    x_center, y_center, width, height = bbox
    x_center = max(0.0, min(1.0, x_center))
    y_center = max(0.0, min(1.0, y_center))
    width = max(0.0, min(1.0, width))
    height = max(0.0, min(1.0, height))
    return [x_center, y_center, width, height]


# --- Сбор данных ---
all_images = []
for file in os.listdir(INPUT_DIR):
    if file.lower().endswith((".jpg")):
        img_path = os.path.join(INPUT_DIR, file)
        label_path = os.path.splitext(img_path)[0] + ".txt"
        if os.path.exists(label_path):
            all_images.append((img_path, label_path))

random.shuffle(all_images)
total = len(all_images)

train_end = int(total * TRAIN_RATIO)
val_end = train_end + int(total * VAL_RATIO)

train_set = all_images[:train_end]
val_set = all_images[train_end:val_end]
test_set = all_images[val_end:]

print(f"total: {total}, \ntrain: {len(train_set)} ({TRAIN_RATIO*100:.0f}%), \nval: {len(val_set)} ({VAL_RATIO*100:.0f}%), \ntest: {len(test_set)} ({TEST_RATIO*100:.0f}%)")

# --- Обработка train с аугментацией ---
print(f"аугментация {len(train_set)} train")
for img_path, label_path in tqdm(train_set):
    augment_and_save(
        img_path,
        label_path,
        os.path.join(OUTPUT_DIR, "images", "train"),
        os.path.join(OUTPUT_DIR, "labels", "train"),
        AUGMENT_COUNT
    )

# --- Обработка val без аугментации ---
print(f"копирование {len(val_set)} val")
for img_path, label_path in tqdm(val_set):
    try:
        shutil.copy(img_path, os.path.join(OUTPUT_DIR, "images", "val", os.path.basename(img_path)))
        shutil.copy(label_path, os.path.join(OUTPUT_DIR, "labels", "val", os.path.basename(label_path)))
    except Exception as e:
        print(f"ошибка при копировании {img_path}: {str(e)}")

# --- Обработка test без аугментации ---
print(f"копирование {len(test_set)} test")
for img_path, label_path in tqdm(test_set):
    try:
        shutil.copy(img_path, os.path.join(OUTPUT_DIR, "images", "test", os.path.basename(img_path)))
        shutil.copy(label_path, os.path.join(OUTPUT_DIR, "labels", "test", os.path.basename(label_path)))
    except Exception as e:
        print(f"ошибка при копировании {img_path}: {str(e)}")

# --- Создание dataset.yaml ---
yaml_content = f"""
path: {os.path.abspath(OUTPUT_DIR)}
train: images/train
val: images/val
test: images/test

nc: {len(classes)}
names: {classes}
"""

with open(os.path.join(OUTPUT_DIR, "dataset.yaml"), 'w') as f:
    f.write(yaml_content)

print(f"create dataset: {os.path.abspath(OUTPUT_DIR)}")