from nltk import ngrams
import os
import datetime

dataDir = os.getcwd() + "\corpus\\2016-09-20.txt"
f = open(dataDir, encoding="utf8")
text = f.read()

n = 7
numericNumber = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '১০', '১১', '১২', '১৪', '১৫', '১৬', '১৭', '১৮', '১৯',
                 '২০']
verbalNumber = ['শূন্য', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগার', 'বার', 'তের',
                'চৌদ্দ', 'পনের', 'ষোল', 'সতের', 'আঠার', 'ঊনিশ', 'বিশ']
taglist = ['নিহত', 'মৃত্যু', 'জন']

svnGrams = ngrams(text.split(), n)


for gram in svnGrams:
    print(gram)

# for gram in svnGrams:
#     if gram[3] == 'Published:':
#         datestr = gram[4]
# # datestr = datetime.datetime.strptime(datestr, '%Y-%m-%d')
# # print(datestr)
#
# dateOfNews = datestr
# total = 0
# x = 0
#
#
# def check_number(number, gram):
#     for i in number:
#         if i in gram:
#             global x
#             x = number.index(i)
#             # print(x)
#             return True
#     return False
#     pass
#
#
# for gram in svnGrams:
#     if gram[3] in taglist:
#         # print(x)
#         got_number = check_number(numericNumber, gram)
#         # print(got_number, num_value)
#         if not got_number:
#             got_number = check_number(verbalNumber, gram)
#         if got_number is True and x >= total:
#             total = x
#     got_number = False
#
# print(total)
# output = dateOfNews + ' ' + repr(total)
# print(output)
