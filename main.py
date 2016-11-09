# BHORER_KAGOJ.

import os
import ngrammethod
import getdate

out = open('output data.txt', 'w', encoding='utf8')

corpusDir = os.getcwd() + "\corpus"

for filename in os.listdir(corpusDir):

    # out.write(filename + '\n')

    if filename.startswith('BHO') or filename.startswith('JUG') or filename.startswith('KAL'):
        dateval = 1
    elif filename.startswith('BD_'):
        dateval = 2
    elif filename.startswith('PROTHOM_ALO_ARCHIEVE.tx'):
        dateval = 3
    # elif filename.startswith('PROTHOM_ALO.tx'):
        # dateval = 1

    x = 0
    text = ""

    fullname = os.path.join(corpusDir, filename)
    f = open(fullname, encoding="utf8")
    data = f.readlines()

    for line in data:

        text += line

        if line == '#####\n':
            if x == 0:
                x = 1
            else:

                temp = open('temp.txt', 'w', encoding='utf8')
                temp.write(text)
                temp.close()

                output = ngrammethod.text_processor()
                if output > 0:
                    if dateval == 1:
                        date = getdate.get_date()
                    elif dateval == 2:
                        date = getdate.get_date2()
                    elif dateval == 3:
                        date = getdate.get_datePA()
                    datedata = date.strftime('%Y/%m/%d')
                    output = datedata + '   ' + repr(output) + '    ' + filename + '\n'
                    # output = repr(output) + '   ' + datedata + '    ' + filename + '\n'
                    # output = repr(output) + '\n'
                    out.write(output)

                text = ""
                x = 0
out.close()

# sort output file
out = open('output data.txt', 'r', encoding='utf8')
lines = out.readlines()
lines.sort()
out.close()
out = open('output data.txt', 'w', encoding='utf8')
for line in lines:
    out.write(repr(line) + '\n\n')
out.close()
