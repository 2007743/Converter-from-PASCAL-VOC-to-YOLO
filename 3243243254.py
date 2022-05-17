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


def xymn():
    d = {}
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        d.update({i: [soup.find("xmin").text, soup.find("ymin").text, soup.find("xmax").text, soup.find("ymax").text]})
    return d


def size():
    d = {}
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        d.update({i: [soup.find("width").text, soup.find("height").text]})
    return d


def classes():
    d = {}
    if os.path.isfile(f'{folder_images}/classes.txt'):
        os.remove(f'{folder_images}/classes.txt')
    for i in spisok():
        fd = open(f'{folder_images}/{i}.xml', 'r')
        xml_file = fd.read()
        soup = BeautifulSoup(xml_file, 'lxml')
        b = soup.find("name").text
        x = open(f'{folder_images}/classes.txt', 'a+')
        x1 = open(f'{folder_images}/classes.txt', 'r+')
        x3 = x1.read().split()
        if b not in x3:
            x.write(f'{b}\n')
            d.update({i: b})
    return d


def convertor():
    x = 0
    name = {}
    s = spisok()
    d = xymn()
    sz = size()
    c = classes()
    for i in d:
        x = x + 1
        xywh = (float(d.get(i)[0]), float(d.get(i)[2]), float(d.get(i)[1]), float(d.get(i)[3]))
        if os.path.isfile(f'{folder_images}\\{s[x]}.jpg'):
            if not os.path.isfile(f'.{folder_images}\\{s[x]}'):
                height = float(sz.get(s[x])[1])
                width = float(sz.get(s[x])[0])
                sizes = (width, height)
                youlo = convert(sizes, (xywh))
                for er, rt in enumerate(open(f'{folder_images}/classes.txt', 'r')):
                    name.update({rt.rstrip(): er})
                print(name)
                print(c.get(i))
                o = open(f'{folder_images}\\{s[x]}.txt', 'w')
                o.write(f'{name[c.get(i)]} {youlo[0]} {youlo[1]} {youlo[2]} {youlo[3]}')


if __name__ == '__main__':
    convertor()
