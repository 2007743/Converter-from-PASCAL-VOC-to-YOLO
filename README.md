# Converter-from-PASCAL-VOC-to-YOLO
**Этот конвертор кординат разметки изображений из PASCAL VOC в YOLO.**
# Установка.
Копировать 
```
git clone https://github.com/2007743/Converter-from-PASCAL-VOC-to-YOLO  # clone
cd Converter-from-PASCAL-VOC-to-YOLO
pip install -r requirements.txt
```
# Запуск без графического интерфейса.
**Для запуска конвертора вам нужно указать параметры ```--img, --cords, --classes, --imgclasses ```**
### Параметры.
```
В параметре --img вы указываете путь до папки с фото.
В параметре --cords вы указываете путь до файла где указаны названия фото и после кординаты.
В параметре --classes вы указываете путь до файла где указаны классы которые будут использоваться у вас во время обучения нейронной сети.
В параметре --imgclasses вы указываете путь до файла где указаны названия фото и классы которые вы указали в параметре --classes.
```
### Пример запуска.
```
python Convertor.py --img data\images --cords data\images_box.txt --classes \data\classes.txt --imgclasses data\imgclasses.txt
```
# Запуск без графического интерфейса.
**Для запуска конвертора вам нужно запустить файл Convertor UI.py .**
### Пример запуска с графическим интерфейсом.
```
python Convertor UI.py 
```
# Выходные данные.
**Если вы все указали правильно то в папке с фотографиями будут создаваться txt файлы с названиями фото и в формате yolo.**
# Лицензия.
Пожалуйста, обратитесь к [LICENSE](https://github.com/2007743/Converter-from-PASCAL-VOC-to-YOLO/blob/main/LICENSE)  для получения всей информации о лицензировании.
