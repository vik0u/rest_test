import os
import cv2

input_folder ="тест"
output_folder ="images"
frame_interval = 5

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if not filename.lower().endswith((".mov")):
        continue

    video_path = os.path.join(input_folder, filename)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"не удалось открыть {filename}")
        continue

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"обработка {filename} (FPS: {fps:.1f}, кадров: {total_frames})")

    saved_count = 0
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Сохраняем кадр с интервалом
        if frame_count % int(fps * frame_interval) == 0:
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_frame{saved_count:04d}.jpg")
            cv2.imwrite(output_path, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"сохранено: {saved_count}\n")