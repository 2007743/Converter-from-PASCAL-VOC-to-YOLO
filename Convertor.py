import os
from PIL import Image
import PySimpleGUI as sg


# import argparse
# parser = argparse.ArgumentParser(description='Converter-from-PASCAL-VOC-to-YOLO')
# parser.add_argument("--img", help="Specify the path to the folder with photos")
# parser.add_argument("--cords", help="Specify the path to the file with coordinates")
# parser.add_argument("--classes", help="Specify the path to the file classes")
# parser.add_argument("--imgclasses", help="Specify the path to the file that contains the name of the "
# "image and the name of the class to which this image belongs")
# args = parser.parse_args()
# folder_images = args.img
# size_images = dict()
# f = open(f'{args.cords}', 'r')
# line = f.readlines()
# n = open(f'{args.imgclasses}',
#         'r')  # Specify the path to the file that contains the name of the image and the name of the class to which this image belongs
# naz = n.readlines()
# name1 = open(f"{args.classes}", 'r')
# name2 = name1.readlines()
def datafolder():
    while True:
        sg.set_options(auto_size_buttons=True)
        foldername = sg.popup_get_folder(
            'Укажите путь до путь до папки с фото.',
            title='Conventor')
        if foldername == '':
            return
        folder = sg.popup_yes_no('Вы указали путь до путь до папки с фото?')
        if folder == 'Yes':
            if foldername is not None:
                try:
                    print(foldername)
                    return foldername
                except:
                    sg.popup_error('Error reading file')
                    return
        else:
            print(123123)


def datacords():
    while True:
        sg.set_options(auto_size_buttons=True)
        cordsname = sg.popup_get_file(
            'Укажите путь до файла где указаны названия фото и после кординаты.',
            title='Conventor')
        if cordsname == '':
            return
        cords = sg.popup_yes_no('Вы указали путь до файла с указаными названия фото и кординатами?')
        if cords == 'Yes':
            if cordsname is not None:
                try:
                    print(cordsname)
                    return cordsname
                except:
                    sg.popup_error('Error reading file')
                    return
        else:
            print(123123)


def dataclasses():
    while True:
        sg.set_options(auto_size_buttons=True)
        classesname = sg.popup_get_file(
            'Укажите путь до файла где указаны классы которые будут использоваться у вас во время обучения нейронной '
            'сети.',
            title='Conventor')
        if classesname == '':
            return
        classes = sg.popup_yes_no('Вы указали путь до файла где указаны классы которые будут использоваться у вас во '
                                  'время обучения нейронной?')
        if classes == 'Yes':
            if classesname is not None:
                try:
                    print(classesname)
                    return classesname
                except:
                    sg.popup_error('Error reading file')
                    return
        else:
            print(123123)


def dataimgclasses():
    while True:
        sg.set_options(auto_size_buttons=True)
        imgclassesname = sg.popup_get_file(
            'Укажите путь до файла где указаны названия фото и классы которые вы указаны в файле classes.',
            title='Conventor')
        if imgclassesname == '':
            return
        imgclasses = sg.popup_yes_no('Вы указали путь до файла где указаны названия фото и классы которые вы указаны '
                                     'в файле classes?')
        if imgclasses == 'Yes':
            if imgclassesname is not None:
                try:
                    print(imgclassesname)
                    return imgclassesname
                except:
                    sg.popup_error('Error reading file')
                    return
        else:
            print(123123)


folder_images = datafolder()
size_images = dict()

f = open(f'{datacords()}', 'r')
line = f.readlines()

n = open(f'{dataimgclasses()}',
         'r')  # Specify the path to the file that contains the name of the image and the name of the class to which this image belongs
naz = n.readlines()

name1 = open(f"{dataclasses()}", 'r')
name2 = name1.readlines()


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def razresh(name):
    try:
        for dirpath, _, filenames in os.walk(folder_images):
            for path_image in filenames:
                image = os.path.abspath(os.path.join(dirpath, path_image))
                try:
                    with Image.open(image) as img:
                        width, heigth = img.size
                        size_images[path_image] = {'width': width, 'heigth': heigth}
                except:
                    a = 'wqewqeqwe'
        s = size_images.get(f'{name}.jpg')
        return s.get("width"), s.get("heigth")
    except:
        a = "qweqwewqe"


def nazv1():
    nazv = {}
    for x in naz:
        t = x.split(" ", maxsplit=1)
        nazv.update({str(t[0]): str(t[1].rstrip())})
    return nazv


def convertor():
    for f in line:
        name = {}
        i = f.rstrip().split(' ')
        xywh = float(i[1]), float(i[3]), float(i[2]), float(i[4])
        nazvanie = i[0]
        print(nazvanie)
        if os.path.isfile(
                f'{folder_images}\{nazvanie}.jpg'):  # Specify the path to the folder where the images are located
            if not os.path.isfile(
                    f'.{folder_images}\{nazvanie}.txt'):  # Specify the path to the folder where the pictures are located to save the description of the photo to this folder already in YOLO format
                youlo = convert(razresh(nazvanie), (xywh))
                nazv2 = nazv1()
                nazv3 = nazv2[nazvanie]
                for x, rt in enumerate(name2):
                    name.update({rt.rstrip(): x})
                    if x == 69:
                        name23 = name[nazv3]
                        o = open(f'{folder_images}\{nazvanie}.txt',
                                 'w')  # Specify the path the same path that you specified before
                        o1 = o.write(f'{name23} {youlo[0]} {youlo[1]} {youlo[2]} {youlo[3]}')
        else:
            v = 0


if __name__ == '__main__':
    datacords()
    dataclasses()
    dataimgclasses()
    convertor()
