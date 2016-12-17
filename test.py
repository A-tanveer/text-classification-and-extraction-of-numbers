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

# import re
# s = '<@ """@$ FSDF >something something (more noise)'
# x = re.sub(r'\(.+?\)', '', s)
#
# print(x)

x = 'বঙ্গোপসাগরে বজ্রপাতে ট্রলার থেকে ছিটকে পড়ে মামুন হাওলাদার নামের এক জেলে গত চার দিন ধরে নিখোঁজ রয়েছেন। এ ছাড়া বজ্রপাতে অপর দুই জেলে আহত হন। গত বৃহস্পতিবার সকাল সাড়ে আটটার দিকে সাগরের চান্দেশ্বরসংলগ্ন সুখপাড়া এলাকায় এ ঘটনা ঘটে। মামুন হাওলাদার বরগুনার পাথরঘাটা উপজেলার তাফালবাড়িয়া গ্রামের মন্নান হাওলাদারের ছেলে। বাংলাদেশ ক্ষুদ্র মৎস্যজীবী সমিতি পাথরঘাটা উপজেলা কার্যালয়ের সাধারণ সম্পাদক সিদ্দিকুর রহমান হাওলাদার ও পাথরঘাটা বিএফডিসি মৎস্য আড়তদার আবদুর রহমান ঘটনার সত্যতা নিশ্চিত করেছেন। বজ্রপাতে আহত জেলেরা হলেন নবী হোসেন  ও আবদুল লতিফ । তাঁদের বাড়ি পাথরঘাটার তাফালবাড়িয়া ও মঠেরখাল গ্রামে। xa0 ইহাতে মন্তব্য প্রদান বন্ধ রয়েছে'
tag2 = ['নিহত', 'মৃত্যু', 'মারা', 'মৃত্যুর', 'নিখোজ', 'নিখোঁজ']
x.split()
for a in tag2:
    if a in x:
        print('yes')