# rest_test

# Запуск
для воспроизведения результатов:
- собраный пакет с cuda/можно запустить на кагле, тогда поменять путь в dataset.yaml
- dataset/ - готовый датасет для YOLO
- images/ - папка с разметкой
- results_0/ - результаты первой иттерации
- results_1/ - результаты второй иттерации
- тест/ - исходные данные
- extract_images.py - извлечение кадров из видео, сохранение
- prepare_dataset_aug.py - подготовка датасета для YOLO по размеченным данным
- train.py - основной файл обучения модели по подготовленному датасету

**Запуск:**

```python3 train.py```

# Отчет!


Этапы:
- Извлечение кадров из тестовых видео, подбор необходимого числа кадров для избегания переобучения
- Разметка датасета, выявлены следующие классы: 'teapot', 'cup_of_tea', 'meat', 'flatbread', 'sauce', 'salad1', 'salad2', 'soup1', 'soup2', 'vodka'
- Обучение модели, анализ результатов

Затраченое время:
- Подготовка данных(~5-6 часов включая подготовку, разметку, разделение на выборки)
- Обучение модели (~3 часа на каждую итерацию с учетом подбора параметров, обучала на кагле)
- Отчет (~1-2 часа)


# Результаты обучения

## **Первая попытка обучения** (без разбития на тестовую выборку, с более жесткими параметрами аугментациии при обучении)


<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/d62e3d71-b0e0-4415-ace1-0b968292a27c" alt="val_batch1_pred" style="width: 100%;">
    <p style="text-align: center;">Предсказания на валидации (batch 1)</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/9bd08bf2-bbdf-42ed-b4f6-b642b778387b" alt="val_batch1_labels" style="width: 100%;">
    <p style="text-align: center;">Разметка валидации (batch 1)</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/e414e1b8-072b-4ee3-82b8-6906266475fd" alt="val_batch0_pred" style="width: 100%;">
    <p style="text-align: center;">Предсказания на валидации (batch 0)</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/1a09168c-9b83-448a-8e18-e02f176005a6" alt="P_curve" style="width: 100%;">
    <p style="text-align: center;">Precision Curve</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/96695142-67cb-4c16-804a-3a2455c4233c" alt="labels_correlogram" style="width: 100%;">
    <p style="text-align: center;">Коррелограмма меток</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/c0b46e25-95f2-46a8-b988-2f3d6530383d" alt="labels" style="width: 100%;">
    <p style="text-align: center;">Распределение меток</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/e8765ec6-62f8-43c9-93f6-2cf18087c312" alt="F1_curve" style="width: 100%;">
    <p style="text-align: center;">F1 Curve</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/1a09168c-9b83-448a-8e18-e02f176005a6" alt="P_curve" style="width: 100%;">
    <p style="text-align: center;">Precision Curve</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/ef16a7ff-98d8-438a-a358-53618bc366f7" alt="confusion_matrix" style="width: 100%;">
    <p style="text-align: center;">Confusion Matrix</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/0aed17b8-1c39-4ca1-9bac-841492954da6" alt="train_batch2" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 2</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/11d4ca68-26cf-4307-879f-dd6bbeea55f0" alt="train_batch1" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 1</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/cc855bf6-c4a7-4c42-a076-f1a5b809df87" alt="train_batch0" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 0</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 48%;">
    <img src="https://github.com/user-attachments/assets/a248731f-e059-4721-b622-59850c75d797" alt="results" style="width: 100%;">
    <p style="text-align: center;">Метрики обучения</p>
  </div>
  <div style="width: 48%;">
    <img src="https://github.com/user-attachments/assets/1569711f-2aa5-40de-9b54-48879f7a5707" alt="R_curve" style="width: 100%;">
    <p style="text-align: center;">Recall Curve</p>
  </div>
</div>




## **Вторая попытка обучения** с более гибкими параметрами аугментациии, с разбитием на train/val/test


<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/fc0043d0-5d67-4c42-b2bc-435aba01b7e2" alt="train_batch13090" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 13090</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/45fc36a2-5a58-4a75-ba9e-3b417a8b1d73" alt="train_batch2" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 2</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/0e345089-d94c-4305-b985-7d4e3076be3d" alt="train_batch1" style="width: 100%;">
    <p style="text-align: center;">Обучающий batch 1</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/01e1ef52-6bd0-4701-93bd-734c84570075" alt="results" style="width: 100%;">
    <p style="text-align: center;">Метрики обучения</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/f524db67-d294-4d86-a949-2fe517094a16" alt="R_curve" style="width: 100%;">
    <p style="text-align: center;">Recall Curve</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/79f44b92-bc2a-44a5-a66e-cd86e2bae267" alt="PR_curve" style="width: 100%;">
    <p style="text-align: center;">PR Curve</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/e122ec24-ca14-4c60-a152-a6e092a19ab0" alt="P_curve" style="width: 100%;">
    <p style="text-align: center;">Precision Curve</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/b5032d59-604e-4d0f-8150-cdf93f803f04" alt="labels_correlogram" style="width: 100%;">
    <p style="text-align: center;">Коррелограмма меток</p>
  </div>
  <div style="width: 32%;">
    <img src="https://github.com/user-attachments/assets/ebecd911-c108-4a59-834c-666cfa4a99f7" alt="labels" style="width: 100%;">
    <p style="text-align: center;">Распределение меток</p>
  </div>
</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-bottom: 20px;">
  <div style="width: 48%;">
    <img src="https://github.com/user-attachments/assets/b0b7e5d5-13e3-4387-8756-eb34041a95d4" alt="F1_curve" style="width: 100%;">
    <p style="text-align: center;">F1 Curve</p>
  </div>
  <div style="width: 48%;">
    <img src="https://github.com/user-attachments/assets/0151ea2c-9f11-48d7-88fb-3a0f39d03b2d" alt="confusion_matrix" style="width: 100%;">
    <p style="text-align: center;">Confusion Matrix</p>
  </div>
</div>



























