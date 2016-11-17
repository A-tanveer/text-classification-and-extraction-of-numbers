import os
import NgramMethod
import GetDate

out = open('output data.txt', 'w', encoding='utf8')

corpusDir = os.getcwd() + "\corpus"

for filename in os.listdir(corpusDir):

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

                output = NgramMethod.text_processor()
                if output > 0:

                    if filename.startswith('BHO') or filename.startswith('SOM') or filename.startswith(
                            'JUG') or filename.startswith('KAL'):
                        date = GetDate.get_date(2, 1)
                    elif filename.startswith('BD_'):
                        date = GetDate.get_date(5, 2)
                    elif filename.startswith('PROTHOM_ALO_A'):
                        date = GetDate.get_date(2, 2)  # get_date3 can be used here
                    elif filename.startswith('PROTHOM_ALO_C'):
                        date = GetDate.get_date_bangla()

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
    out.write(repr(line) + '\n')
out.close()
