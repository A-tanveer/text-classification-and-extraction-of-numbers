from nltk import ngrams
import os
# import datetime

out = open('output data.txt', 'w', encoding='utf8')

# getting direction of corpus inside the working directory. all data files should be kept in the corpur folder

corpusDir = os.getcwd() + "\corpus"

# listing all files in the corpus folder and processing them one by one

for filename in os.listdir(corpusDir):
    fullname = os.path.join(corpusDir, filename)
    f = open(fullname, encoding="utf8")
    text = f.read()

    numericNumber = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '১০', '১১', '১২', '১৪', '১৫', '১৬', '১৭', '১৮',
                     '১৯', '২০']
    verbalNumber = ['শূন্য', 'এক', 'দুই', 'তিন', 'চার', 'পাঁচ', 'ছয়', 'সাত', 'আট', 'নয়', 'দশ', 'এগার', 'বার', 'তের',
                    'চৌদ্দ', 'পনের', 'ষোল', 'সতের', 'আঠার', 'ঊনিশ', 'বিশ']
    taglist = ['নিহত', 'মৃত্যু', 'জন']
    # tgalist2 and taglist3 is to resolve the cases where number of casualties is not provided
    taglist2 = ['দম্পতি', 'মা-মেয়ে', 'ভাই-বোন', 'মামা-ভাগ্নে']
    taglist3 = ['সভাপতি', 'গৃহবধূ', 'শিশু', 'কৃষক']

    dateList1 = ['প্রকাশ:', 'Published:']
    dateList2 = ['প্রকাশ', 'Published']
    # split text into nGrams(7)
    svnGrams = ngrams(text.split(), 7)

    total = 0
    x = 0

    # this method checks if there a number present in the gram

    def check_number(number, gram):
        for i in number:
            if i in gram:
                global x
                x = number.index(i)
                # print(x)
                return True
        return False
        pass

    # finding result
    for gram in svnGrams:
        # looking for casualty determining words
        if gram[3] in taglist:
            # look for number of casualties
            got_number = check_number(numericNumber, gram)
            if not got_number:
                got_number = check_number(verbalNumber, gram)

            if got_number is True and x >= total:
                total = x

        got_number = False

        # getting date of publication
        if gram[3] in dateList1:
            dateOfNews = gram[4]
        elif gram[2] in dateList2:
            dateOfNews = gram[4] + " " + gram[5] + " " + gram[6]

    output = dateOfNews + " " + repr(total) + "\n"
    # outputting data to a text file to use this information for finding a statistics later
    out.write(output)
