from bs4 import BeautifulSoup
import os
import PySimpleGUI as sg


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
    sg.set_options(auto_size_buttons=True)
    sg.theme('dark grey 9')
    foldername = sg.popup_get_folder('Укажите путь до путь до папки с фото.',
                                     title='Conventor', grab_anywhere=True)
    if foldername == '':
        return
    folder = sg.popup_yes_no('Вы указали путь до путь до папки с фото?', grab_anywhere=True)
    if folder == 'Yes':
        if foldername is not None:
            try:
                print(foldername)
                return foldername
            except:
                sg.popup_error('Error reading file')
                return


folder_images = datafolder()
files = os.listdir(folder_images)


def spisok():
    nazv = []
    for f in files:
        if f.split('.')[-1] == "xml":
            nazv.append(f.split('.')[0])
    return nazv


def size():
    d = {}
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        d.update({i: [soup.find("xmin").text, soup.find("ymin").text, soup.find("xmax").text, soup.find("ymax").text]})
    print(d)
    return d


def xymn():
    d = {}
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        d.update({i: [soup.find("width").text, soup.find("height").text]})
    return d


def classes():
    a = 0
    l = {}
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        b = soup.find("name").text
        x = open(f'{folder_images}/classes.txt', 'a+')
        a = a+1
        if l.get(b) != 1:
            l.update({b : "1"})
            x.write(f"\n {b}")


def convertor():
    x = 0
    s = spisok()
    for i in xymn():
        x = x+1
        print(i)
        xywh = (i[1], i[3], i[2], i[4])
        if os.path.isfile(f'{folder_images}\\{s[x]}.jpg'):
            if not os.path.isfile(f'.{folder_images}\\{s[x]}'):
                height = size().get(s[x])[1]
                width = size().get(s[x])[0]
                sizes = (width, height)
                print(sizes)
                youlo = convert(sizes, (xywh))
                print(youlo)
                o = open(f'{folder_images}\\{s[x]}.txt', 'w')
                o.write(f'{classes} {youlo[0]} {youlo[1]} {youlo[2]} {youlo[3]}')

if __name__ == '__main__':
    classes()
