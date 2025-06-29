# rest_test

# данные
- dataset/ - готовый датасет для YOLO
- images/ - папка с разметкой
- results_0/ - результаты первой иттерации
- results_1/ - результаты второй иттерации
- тест/ - исходные данные
- extract_images.py - извлечение кадров из видео, сохранение
- prepare_dataset_aug.py - подготовка датасета для YOLO по размеченным данным
- train.py - основной файл обучения модели по подготовленному датасету

# Запуск
для воспроизведения результатов:

```python3 train.py```

# Отчет!


Этапы:
- Извлечение кадров из тестовых видео, подбор необходимого числа кадров для избегания переобучения
- Разметка датасета, выявлены следующие классы: 'teapot', 'cup_of_tea', 'meat', 'flatbread', 'sauce', 'salad1', 'salad2', 'soup1', 'soup2', 'vodka'
- Обучение модели, анализ результатов

Затраченое время:
- Подготовка данных, аугментация(~5-6 часов включая подготовку, разметку, разделение на выборки)
- Обучение модели (~3 часа на каждую итерацию с учетом подбора параметров, обучала на кагле)
- Отчет (~1-2 часа)


# Результаты обучения

## **Первая попытка обучения** (без разбития на тестовую выборку, с более жесткими параметрами аугментациии при обучении)
<div align="center">
  <img src="https://github.com/user-attachments/assets/d62e3d71-b0e0-4415-ace1-0b968292a27c" width="45%">
  <img src="https://github.com/user-attachments/assets/9bd08bf2-bbdf-42ed-b4f6-b642b778387b" width="45%">
  <p>Предсказания и разметка на валидации (Batch 1)</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/e414e1b8-072b-4ee3-82b8-6906266475fd" width="45%">
  <img src="https://github.com/user-attachments/assets/1a09168c-9b83-448a-8e18-e02f176005a6" width="45%">
  <p>Предсказания на валидации (Batch 0) и Precision Curve</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/96695142-67cb-4c16-804a-3a2455c4233c" width="45%">
  <img src="https://github.com/user-attachments/assets/c0b46e25-95f2-46a8-b988-2f3d6530383d" width="45%">
  <p>Коррелограмма меток и распределение классов</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/e8765ec6-62f8-43c9-93f6-2cf18087c312" width="45%">
  <img src="https://github.com/user-attachments/assets/ef16a7ff-98d8-438a-a358-53618bc366f7" width="45%">
  <p>F1 Curve и матрица ошибок (Confusion Matrix)</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/0aed17b8-1c39-4ca1-9bac-841492954da6" width="45%">
  <img src="https://github.com/user-attachments/assets/11d4ca68-26cf-4307-879f-dd6bbeea55f0" width="45%">
  <p>Обучающие выборки: Batch 2 и Batch 1</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/a248731f-e059-4721-b622-59850c75d797" width="45%">
  <img src="https://github.com/user-attachments/assets/1569711f-2aa5-40de-9b54-48879f7a5707" width="45%">
  <p>Метрики обучения и Recall Curve</p>
</div>




## **Вторая попытка обучения** с более гибкими параметрами аугментациии, с разбитием на train/val/test


<div align="center">
  <img src="https://github.com/user-attachments/assets/fc0043d0-5d67-4c42-b2bc-435aba01b7e2" width="45%">
  <img src="https://github.com/user-attachments/assets/45fc36a2-5a58-4a75-ba9e-3b417a8b1d73" width="45%">
  <p>Обучающие выборки: Batch 13090 и Batch 2</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/01e1ef52-6bd0-4701-93bd-734c84570075" width="45%">
  <img src="https://github.com/user-attachments/assets/f524db67-d294-4d86-a949-2fe517094a16" width="45%">
  <p>Метрики обучения и Recall Curve</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/79f44b92-bc2a-44a5-a66e-cd86e2bae267" width="45%">
  <img src="https://github.com/user-attachments/assets/e122ec24-ca14-4c60-a152-a6e092a19ab0" width="45%">
  <p>PR Curve и Precision Curve</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/b5032d59-604e-4d0f-8150-cdf93f803f04" width="45%">
  <img src="https://github.com/user-attachments/assets/ebecd911-c108-4a59-834c-666cfa4a99f7" width="45%">
  <p>Коррелограмма меток и распределение классов</p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/b0b7e5d5-13e3-4387-8756-eb34041a95d4" width="45%">
  <img src="https://github.com/user-attachments/assets/0151ea2c-9f11-48d7-88fb-3a0f39d03b2d" width="45%">
  <p>F1 Curve и матрица ошибок (Confusion Matrix)</p>
</div>

# Финальный отчёт

## Подготовка данных

### Извлечение кадров
Из видеофайлов в папке `тест/` извлекались ключевые кадры с интервалом `5 секунд` с помощью `OpenCV`:
- Учитывались только `.mov` файлы
- Использовалась частота кадров (FPS), чтобы равномерно отбирать кадры
- Скрипт: `extract_images.py`

### Разметка

Разметка bounding boxes производилась вручную по 10 классам:

    teapot, cup_of_tea, meat, flatbread, sauce

    salad1, salad2, soup1, soup2, vodka

Формат разметки — YOLO (txt-файлы с координатами).

### Аугментации

Для расширения обучающей выборки использовались следующие аугментации через Albumentations:

    HorizontalFlip, BrightnessContrast, Rotate, Blur

    Применялись 2 раза к каждому изображению

## Обучение модели
Конфигурация

    Использовались предобученные весаYOLOv11

    Обучение производилось на kagle с GPU

    Предобученные веса: yolo11x.pt






















