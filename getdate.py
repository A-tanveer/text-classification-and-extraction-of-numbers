import re
import datetime


def get_date():
    f = open('temp.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 3:
            data = repr(line)
            # print(data)
            match = re.search(r'\d{4}/\d{2}/\d{2}', data)
            # print(match)
            date = datetime.datetime.strptime(match.group(), '%Y/%m/%d')
            break
    return date


def get_date2():
    f = open('temp.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 6:
            data = repr(line)
            match = re.search(r'\d{4}-\d{2}-\d{2}', data)
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d')
            break
    return date


def get_datePA():
    f = open('temp.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 3:
            data = repr(line)
            match = re.search(r'\d{4}-\d{2}-\d{2}', data)
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d')
            break
    return date


def get_date3():
    f = open('temp.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 6:
            data = repr(line)
            bang = '০১২৩৪৫৬৭৮৯'
            eng = '0123456789'
            ddata = data.translate({ord(x): y for (x, y) in zip(bang, eng)}) # http://stackoverflow.com/questions/3031045/how-come-string-maketrans-does-not-work-in-python-3-1
            print(ddata)
            match = re.search(r'\d{4}-\d{2}-\d{2}', ddata)

            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d')
            break
    return date


# d = get_date3()
# print(d)
# get_date3()
