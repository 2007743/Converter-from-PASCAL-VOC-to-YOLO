import os

from bs4 import BeautifulSoup

folder_images = 'C:\\Users\Stud\PycharmProjects\Converter-from-PASCAL-VOC-to-YOLO\VOC2012\VOC2012\Annotations'
files = os.listdir(folder_images)


def spisok():
    nazv = []
    for f in files:
        if f.split('.')[-1] == "xml":
            nazv.append(f.split('.')[0])
    return nazv


d = {}
for i in spisok():
    fd = open(f'{folder_images}/{i}.xml', 'r')
    xml_file = fd.read()
    soup = BeautifulSoup(xml_file, 'lxml')
    d.update({i: [soup.find("xmin").text, soup.find("ymin").text, soup.find("xmax").text, soup.find("ymax").text]})
print(d)
