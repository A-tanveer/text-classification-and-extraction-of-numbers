import ContentExtraction
import GetDate
import NgramMethod
import os
import pymysql

# connect database
conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
cur = conn.cursor()

cur.execute("TRUNCATE `processed_news`;")
cur.execute("ALTER TABLE `processed_news` AUTO_INCREMENT = 1;")

out = open('output data.txt', 'w', encoding='utf8')
xyz = 0
a = 0

corpusDir = os.getcwd() + "\corpus"
# reading every file in the corpus directory
for filename in os.listdir(corpusDir):

    x = 0
    text = ""

    fullname = os.path.join(corpusDir, filename)
    f = open(fullname, encoding="utf8")
    data = f.readlines()

    for line in data:
        text += line

        if line == '#####\n':
            x += 1
        if x == 2:
            x = 0
            a += 1
            temp = open('temp.txt', 'w', encoding='utf8')
            temp.write(text)
            temp.close()

            ContentExtraction.content_extraction()

            death_count = 0
            death_count = NgramMethod.text_processor()

            if death_count > 0:
                cont = open('content.txt', encoding='utf8')
                lns = cont.readlines()
                cont.close()
                content = lns[6]
                domain = lns[0]
                url = lns[2]
                title = lns[4]

                if filename.startswith('BHO') or filename.startswith('SOM') or filename.startswith(
                        'JUG') or filename.startswith('KAL'):
                    publish_date = GetDate.get_date(2, 1)
                elif filename.startswith('BD_'):
                    publish_date = GetDate.get_date(5, 2)
                elif filename.startswith('PROTHOM_ALO'):
                    publish_date = GetDate.get_date(2, 2)  # get_date3 can be used here
                elif filename.startswith('PROTHOM-ALO'):
                    publish_date = GetDate.get_date_bangla()

                incident_date = GetDate.get_date_of_incident(publish_date)
                published = publish_date.strftime('%Y/%m/%d')
                occured_on = incident_date.strftime('%Y/%m/%d')

                output = published + '   ' + repr(death_count) + '    ' + filename + '\n'
                out.write(output)

                sql = "INSERT INTO `processed_news` (`content`, `domain`, `url`, `title`, `news_date`," \
                      " `original_date`, `casualty_count`) VALUES (" + repr(content) + ", " + repr(domain)\
                      + ", " + repr(url) + ", " + repr(title) + ", " + repr(published) + ", " + repr(occured_on)\
                      + ", " + repr(death_count) + ");"
                cur.execute(sql)

            xyz += death_count
            text = ""


cur.close()
conn.close()

# # sort output file
out = open('output data.txt', 'r', encoding='utf8')
lines = out.readlines()
lines.sort()
out.close()
out = open('output data.txt', 'w', encoding='utf8')
for line in lines:
    out.write(repr(line) + '\n')
out.close()
print(xyz)
print(a)

import dbWorks.DbMain

