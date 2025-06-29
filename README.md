![confusion_matrix](https://github.com/user-attachments/assets/b89e631f-7085-450f-adba-aa4c210db9c0)# rest_test

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

**Первая попытка обучения** (без разбития на тестовую выборку, с более жесткими параметрами аугментациии при обучении)

![val_batch1_pred](https://github.com/user-attachments/assets/d62e3d71-b0e0-4415-ace1-0b968292a27c)
![val_batch1_labels](https://github.com/user-attachments/assets/9bd08bf2-bbdf-42ed-b4f6-b642b778387b)
![val_batch0_pred](https://github.com/user-attachments/assets/e414e1b8-072b-4ee3-82b8-6906266475fd)
![P_curve](https://github.com/user-attachments/assets/1a09168c-9b83-448a-8e18-e02f176005a6)
![labels_correlogram](https://github.com/user-attachments/assets/96695142-67cb-4c16-804a-3a2455c4233c)
![labels](https://github.com/user-attachments/assets/c0b46e25-95f2-46a8-b988-2f3d6530383d)
![F1_curve](https://github.com/user-attachments/assets/e8765ec6-62f8-43c9-93f6-2cf18087c312)
![confusion_matrix_normalized](https://github.com/user-attachments/assets/1e0c8ba1-d3a6-4304-b3ca-fd72f8e2a1e9)
![confusion_matrix](https://github.com/user-attachments/assets/ef16a7ff-98d8-438a-a358-53618bc366f7)
[val_batch0_labels](https://github.com/user-attachments/assets/2c80d258-c051-4298-a27c-abac8c992ef8)
![train_batch2](https://github.com/user-attachments/assets/0aed17b8-1c39-4ca1-9bac-841492954da6)
![train_batch1](https://github.com/user-attachments/assets/11d4ca68-26cf-4307-879f-dd6bbeea55f0)
![train_batch0](https://github.com/user-attachments/assets/cc855bf6-c4a7-4c42-a076-f1a5b809df87)
![results](https://github.com/user-attachments/assets/a248731f-e059-4721-b622-59850c75d797)
![R_curve](https://github.com/user-attachments/assets/1569711f-2aa5-40de-9b54-48879f7a5707)
![PR_curve](https://github.com/user-attachments/assets/379da81c-6b29-4c5a-bdf5-ae7b002983a6)





**Вторая попытка обучения** с более гибкими параметрами аугментациии, с разбитием на train/val/test

![train_batch13090](https://github.com/user-attachments/assets/fc0043d0-5d67-4c42-b2bc-435aba01b7e2)
![train_batch2](https://github.com/user-attachments/assets/45fc36a2-5a58-4a75-ba9e-3b417a8b1d73)
![train_batch1](https://github.com/user-attachments/assets/0e345089-d94c-4305-b985-7d4e3076be3d)
![train_batch0](https://github.com/user-attachments/assets/fddcfb67-7f53-4981-9c72-c5240011cf9d)
![results](https://github.com/user-attachments/assets/01e1ef52-6bd0-4701-93bd-734c84570075)
![R_curve](https://github.com/user-attachments/assets/f524db67-d294-4d86-a949-2fe517094a16)
![PR_curve](https://github.com/user-attachments/assets/79f44b92-bc2a-44a5-a66e-cd86e2bae267)
![P_curve](https://github.com/user-attachments/assets/e122ec24-ca14-4c60-a152-a6e092a19ab0)
![labels_correlogram](https://github.com/user-attachments/assets/b5032d59-604e-4d0f-8150-cdf93f803f04)
![labels](https://github.com/user-attachments/assets/ebecd911-c108-4a59-834c-666cfa4a99f7)
![F1_curve](https://github.com/user-attachments/assets/b0b7e5d5-13e3-4387-8756-eb34041a95d4)
![confusion_matrix_normalized](https://github.com/user-attachments/assets/014f2680-801e-44a2-b7d4-c5daf9736a27)
![confusion_matrix](https://github.com/user-attachments/assets/0151ea2c-9f11-48d7-88fb-3a0f39d03b2d)



























