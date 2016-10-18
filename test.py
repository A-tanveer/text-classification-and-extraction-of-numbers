from nltk import ngrams
import os
import datetime

dataDir = os.getcwd() + "\corpus"
for filename in os.listdir(dataDir):
    fullname = os.path.join(dataDir, filename)
    f = open(fullname, encoding="utf8")
    text = f.read()

    numericNumber = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '১০', '১১', '১২', '১৪', '১৫', '১৬', '১৭', '১৮',
                     '১৯', '২০']
    verbalNumber = ['শূন্য', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগার', 'বার', 'তের',
                    'চৌদ্দ', 'পনের', 'ষোল', 'সতের', 'আঠার', 'ঊনিশ', 'বিশ']
    taglist = ['নিহত', 'মৃত্যু', 'জন']
    taglist2 = ['দম্পতি', 'মা-মেয়ে', 'ভাই-বোন', 'মামা-ভাগ্নে']
    taglist3 = ['সভাপতি', 'গৃহবধূ', 'শিশু', 'কৃষক']
    dateList1 = ['প্রকাশ:', 'Published:']
    dateList2 = ['প্রকাশ', 'Published']

    svnGrams = ngrams(text.split(), 7)

    total = 0
    x = 0


    def check_number(number, gram):
        for i in number:
            if i in gram:
                global x
                x = number.index(i)
                # print(x)
                return True
        return False
        pass


    for gram in svnGrams:
        if gram[3] in taglist:
            # print(x)
            got_number = check_number(numericNumber, gram)
            # print(got_number, num_value)
            if not got_number:
                got_number = check_number(verbalNumber, gram)
            if got_number is True and x >= total:
                total = x
        got_number = False
        if gram[3] in dateList1:
            dateOfNews = gram[4]
        elif gram[2] in dateList2:
            dateOfNews = gram[4] + " " + gram[5] + " " + gram[6]

    output = dateOfNews + " " + repr(total) + "\n"
    out = open('output data.txt', 'a', encoding='utf8')
    out.write(output)
    # print(output)
