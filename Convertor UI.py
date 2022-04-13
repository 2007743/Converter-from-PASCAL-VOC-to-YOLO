import os
from PIL import Image
import PySimpleGUI as sg


def datafolder():
    while True:
        sg.set_options(auto_size_buttons=True)
        sg.theme('dark grey 9')
        foldername = sg.popup_get_folder(
            'Укажите путь до путь до папки с фото.',
            title='Conventor', no_titlebar=True, grab_anywhere=True)
        if foldername == '':
            return
        folder = sg.popup_yes_no('Вы указали путь до путь до папки с фото?', no_titlebar=True, grab_anywhere=True)
        if folder == 'Yes':
            if foldername is not None:
                try:
                    print(foldername)
                    return foldername
                except:
                    sg.popup_error('Error reading file')
                    return
        elif folder == 'No':
            print(123123)
        else:
            break


def datacords():
    while True:
        sg.set_options(auto_size_buttons=True)
        sg.theme('dark grey 9')
        cordsname = sg.popup_get_file(
            'Укажите путь до файла где указаны названия фото и после кординаты.',
            title='Conventor', no_titlebar=True, grab_anywhere=True)
        if cordsname == '':
            return
        cords = sg.popup_yes_no('Вы указали путь до файла с указаными названия фото и кординатами?', no_titlebar=True, grab_anywhere=True)
        if cords == 'Yes':
            if cordsname is not None:
                try:
                    print(cordsname)
                    return cordsname
                except:
                    sg.popup_error('Error reading file')
                    return
        elif cords == 'No':
            print(123123)
        else:
            break


def dataclasses():
    while True:
        sg.set_options(auto_size_buttons=True)
        sg.theme('dark grey 9')
        classesname = sg.popup_get_file(
            'Укажите путь до файла где указаны классы которые будут использоваться у вас во время обучения нейронной '
            'сети.', title='Conventor', no_titlebar=True, grab_anywhere=True)
        if classesname == '':
            return
        classes = sg.popup_yes_no('Вы указали путь до файла где указаны классы которые будут использоваться у вас во '
                                  'время обучения нейронной?', no_titlebar=True, grab_anywhere=True)
        if classes == 'Yes':
            if classesname is not None:
                try:
                    print(classesname)
                    return classesname
                except:
                    sg.popup_error('Error reading file')
                    return
        elif classes == 'No':
            print(12321323)
        else:
            break


def dataimgclasses():
    while True:
        sg.set_options(auto_size_buttons=True)
        sg.theme('dark grey 9')
        imgclassesname = sg.popup_get_file(
            'Укажите путь до файла где указаны названия фото и классы которые вы указаны в файле classes.',
            title='Conventor', no_titlebar=True, grab_anywhere=True)
        if imgclassesname == '':
            return
        imgclasses = sg.popup_yes_no('Вы указали путь до файла где указаны названия фото и классы которые вы указаны '
                                     'в файле classes?', no_titlebar=True, grab_anywhere=True)
        if imgclasses == 'Yes':
            if imgclassesname is not None:
                try:
                    print(imgclassesname)
                    return imgclassesname
                except:
                    sg.popup_error('Error reading file')
                    break
        elif imgclasses == 'No':
            print(123121231233)
        else:
            break
        break


folder_images = datafolder()
size_images = dict()
line = open(f'{datacords()}', 'r').readlines()
naz = open(f'{dataimgclasses()}', 'r').readlines()
name1 = open(f"{dataclasses()}", 'r').readlines()


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
                for x, rt in enumerate(name1):
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
