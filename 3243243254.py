from bs4 import BeautifulSoup
import os
import PySimpleGUI as sg

fd = open('VOC2012/VOC2012/Annotations/2007_000027.xml', 'r')
xml_file = fd.read()
soup = BeautifulSoup(xml_file, 'lxml')
for tag in soup.findAll("xmin"):
    print(tag)
for tag in soup.findAll("ymin"):
    print(tag)
for tag in soup.findAll("xmax"):
    print(tag)
for tag in soup.findAll("ymax"):
    print(tag)
fd.close()


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


folder_images = datafolder()
files = os.listdir(folder_images)


def spisok():
    nazv = []
    for f in files:
        if f.split('.')[-1] == "xml":
            nazv.append(f.split('.')[0])
    return nazv

def size(nazv):
    fd = open(f'{folder_images}/{nazv}.xml', 'r')
    xml_file = fd.read()
    soup = BeautifulSoup(xml_file, 'lxml')
    return soup.findAll("width"), soup.findAll("height")


def convertor():
    xywh = "546"
    if os.path.isfile(f'{folder_images}\{nazvanie}.jpg'):
        x = x + 1
        if not os.path.isfile(f'.{folder_images}\{spisok[x]}'):
            youlo = convert(size(nazvanie), (xywh))
            nazv3 = nazv1()[nazvanie]
            for x, rt in enumerate(name1):
                name.update({rt.rstrip(): x})
                if x == 69:
                    name23 = name[nazv3]
                    o = open(f'{folder_images}\{nazvanie}.txt', 'w')
                    o1 = o.write(f'{name23} {youlo[0]} {youlo[1]} {youlo[2]} {youlo[3]}')
        else:
            v = 0