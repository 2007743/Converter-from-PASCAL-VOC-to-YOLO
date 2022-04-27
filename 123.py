import os

files = os.listdir('VOC2012\VOC2012\Annotations')


def spisok():
    nazv = []
    for f in files:
        if f.split('.')[-1] == "xml":
            nazv.append(f.split('.')[0])
    return nazv
