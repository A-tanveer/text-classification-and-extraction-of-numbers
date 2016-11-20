import re
import datetime


# just found out following three methods can be done in just one method if
# i include an argument variable. what a fool i am.
# OK now its done :)
# extract date from url if url is in the third line.
# x = url line no (starts from zero) and y = date separation character 1 for / and 2 for -
def get_date(x, y):
    f = open('content.txt', encoding="utf8")
    text = f.readlines()
    data = repr(text[x])

    if y == 1:
        match = re.search(r'\d{4}/\d{2}/\d{2}', data)
        date = datetime.datetime.strptime(match.group(), '%Y/%m/%d').date()
    elif y == 2:
        match = re.search(r'\d{4}-\d{2}-\d{2}', data)
        date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    # print('------------')
    return date


# extract date from url if url is in the sixth line date separated by / #not needed anymore
def get_date2():
    f = open('content.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 6:
            data = repr(line)
            match = re.search(r'\d{4}-\d{2}-\d{2}', data)
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
            break
    return date


# extract date from url if url is in the third line date separated by - #not needed anymore
def get_date_p_a():
    f = open('content.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 3:
            data = repr(line)
            match = re.search(r'\d{4}-\d{2}-\d{2}', data)
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
            break
    return date


# extract date from text. if date is in bangla numeric form and separated by - #can be used
def get_date3():
    f = open('content.txt', encoding="utf8")
    text = f.readlines()
    x = 0
    for line in text:
        x += 1
        if x == 6:
            data = repr(line)
            bang = '০১২৩৪৫৬৭৮৯'
            eng = '0123456789'
            # http://stackoverflow.com/questions/3031045/how-come-string-maketrans-does-not-work-in-python-3-1
            ddata = data.translate({ord(x): y for (x, y) in zip(bang, eng)})
            # print(ddata)
            match = re.search(r'\d{4}-\d{2}-\d{2}', ddata)

            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
            break
    return date


# extract date from bangla text. if date is like জানুয়ারি ০৫, ২০১৫ #hardest one
def get_date_bangla():

    months = [' ', 'জানুয়ারি', 'ফেব্রুয়ারি', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগস্ট', 'সেপ্টেম্বর',
              'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর']
    f = open('content.txt', encoding='utf8')
    text = f.readlines()
    f.close()

    data = repr(text[5])
    bang = '০১২৩৪৫৬৭৮৯'
    eng = '0123456789'
    date_data = data.translate({ord(x): y for (x, y) in zip(bang, eng)})

    f = open('temp', 'w', encoding='utf8')
    f.write(date_data)
    f.close()
    f = open('temp', encoding='utf8')
    text = f.read()
    # print(text)
    x = text.split()
    for i in months:
        if i in x:
            month = repr(months.index(i))
            break

    d = repr(x[3])
    y = repr(x[4])
    day = d[1:3]

    year = y[1:5]
    datestr = year + '-' + month + '-' + day
    date = datetime.datetime.strptime(datestr, '%Y-%m-%d').date()
    return date


def get_date_of_incident(date):
    f = open('content.txt', encoding='utf8')
    lines = f.readlines()
    x = 0
    content = lines[6].split('।')
    for line in content:
        for word in line.split():
            if 'পরশু' in repr(word):
                x = 2
                break
            elif 'কালকে' in repr(word):
                x = 1
                break
            elif 'গতকাল' in repr(word):
                x = 1
                break
            elif 'আজ' in repr(word):
                x = 0
                break

    # date = datetime.datetime.strptime(datestr, '%Y/%m/%d')
    incident_date = date - datetime.timedelta(days=x)
    return incident_date

