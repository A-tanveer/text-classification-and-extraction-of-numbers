# x = [1, 4, 5, 7, 3, 172]
# x.extend([7])
# print(x)
# x = sorted(x)
# x = set(x)
# outstr = ''
# for i in x:
#     a = '%03d' % i
#     outstr += a
# print(outstr)
# one_list = ['কৃষক', 'স্কুলছাত্র', ]
#
# f = open('temp.txt', encoding="utf8")
# text = f.readlines()
# for line in text:
#     data = repr(line)
#     x = line.split('।')
#     for i in x:
#         print(i.replace('~', '').replace('#', ''))
#
#

#
# import re
# f = open('content.txt', encoding='utf8')
# mystring = f.readlines()
# f.close()
# # regex = re.compile(".*?\((.*?)\)")
#
# for line in mystring:
#     result = re.sub('([^>]+)', '', repr(line))
#
#     print(result)
# f = open('content.txt', 'w', encoding='utf8')
# f.write(result)
# f.close()

import re
s = '<@ """@$ FSDF >something something (more noise)'
x = re.sub(r'\(.+?\)', '', s)

print(x)
