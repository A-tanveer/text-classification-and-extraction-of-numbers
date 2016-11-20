# divides text into lines and each line into seven grams(nGram). Then calls method to check if there is number
def text_processor():
    from nltk import ngrams
    import NumberFinder

    total = 0

    tag2 = ['নিহত', 'মৃত্যু', 'মারা', 'জন']
    tag = ['বজ্র', 'বজ্রপাত', 'বজ্রপাতে', 'বজ্রপাত,', 'বজ্রাঘাতে', 'বজ্রাঘাত']
    tag = set(tag)

    f = open('content.txt', encoding="utf8")
    full_text = f.readlines()
    f.close()
    head = full_text[4]
    text = head + ' । ' + full_text[6]

    # only if the news content contains information about Lightning then continue.
    is_thunder = False
    for i in tag:
        if i in text:
            is_thunder = True
            break
    if is_thunder:

        next_line = ''
        next_next_line = ''

        lines = text.split('।')
        num_of_lines = len(lines)
        x = 0

        for line in lines:

            # content of each line must contain information about Lightning to continue.
            is_thunder = False
            for i in tag:
                if i in repr(line):
                    is_thunder = True
                    break
            if is_thunder:

                if (x + 1) < num_of_lines:
                    next_line = lines[x+1]
                if (x+2) < num_of_lines:
                    next_next_line = lines[x+2]

                text_to_gram = line + next_line + next_next_line
                # split text of line into seven grams (nGrams)
                svn_grams = ngrams(text_to_gram.split(), 7)

                # finding result
                for gram in svn_grams:

                    # only seven gram containing casualty information are further processed
                    if gram[3] in tag2:

                        # look for number of casualties
                        num_in_gram = NumberFinder.find_number(gram)

                        if num_in_gram > total:
                            total = num_in_gram

            next_line = ''
            next_next_line = ''

    return total

