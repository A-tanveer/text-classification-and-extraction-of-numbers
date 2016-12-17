import re


def content_extraction():
    out = open('content.txt', 'w', encoding='utf8')
    f = open('temp.txt', encoding="utf8")
    text = f.readlines()
    f.close()
    for line in text:
        x = line.split('\n')
        for i in x:

            i = re.sub(r'\(.+?\)', '', i)  # remove ages of people from data as this creates huge errors
            xx = i.replace('~', '').replace('#', '')  # cleaning data
            out.write(xx)
            if len(xx) > 0:
                out.write('\n')
    out.close()

content_extraction()
