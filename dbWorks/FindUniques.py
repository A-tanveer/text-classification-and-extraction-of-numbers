import pymysql


def get_sub_district(content):
    data = content.split('।')

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    sql = 'SELECT * FROM `upazilla`'
    cur.execute(sql)
    sub_districts = cur.fetchall()

    sub_districts_found = []
    # this list is to be populated with sub-districts names(in english) present in the news and related with lightning

    # looking for any sub divisions only in the lines containing lightning info.
    for row in sub_districts:
        for line in data:
            if 'বজ্র' in line:
                if row[3] in line:
                    sub_districts_found.append(row[2])

    outstr = ''
    outstrlist = []

    # id of every sub district that is in the content and related with lighting is appended to a list
    for sub_district in sub_districts_found:
        sql = "SELECT MIN(upazilla_id) FROM `upazilla` WHERE name = " + repr(sub_district)
        cur.execute(sql)
        u = cur.fetchone()
        outstrlist.append(u[0])
    # keeping unique id's in sorted order
    outstrlist = sorted(set(outstrlist))

    # adding id's into string with every integer to three digit string to avoid misleading result
    for element in outstrlist:
        var = '%03d' % element
        outstr += var

    cur.close()
    conn.close()

    return outstr


def update_news_id_str(u_id, id_str):

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    sql = "UPDATE `processed_news` SET upazilla_id_str = " + repr(id_str) + " WHERE id = " + repr(u_id)

    cur.execute(sql)

    # mark_percent_unique()

    cur.close()
    conn.close()


def duplicate_url():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    sql = 'SELECT id, url FROM `processed_news` WHERE is_unique = 1'
    cur.execute(sql)
    data = cur.fetchall()
    for each_url in data:
        sql = "SELECT is_unique FROM `processed_news` WHERE id = " + repr(each_url[0])
        cur.execute(sql)
        x = cur.fetchone()
        if x[0] == 1:
            sql = "SELECT id FROM `processed_news` WHERE id <> " + repr(each_url[0]) + " AND url = " + repr(each_url[1])
            cur.execute(sql)
            data_now = cur.fetchall()
            sql = "SELECT COUNT(id) FROM `processed_news` WHERE id <> " + repr(each_url[0]) + " AND url = " \
                  + repr(each_url[1])
            cur.execute(sql)
            count = cur.fetchone()
            if count[0] > 0:
                for i in range(count[0]):
                    duplicate_url_data = data_now[i]
                    sql = "UPDATE `processed_news`" \
                          "SET upazilla_id_str = 'duplicate url', " \
                          "match_percent = 100, " \
                          "is_unique = 0, " \
                          "copy_of = " + repr(each_url[0]) + \
                          " WHERE id = " + repr(duplicate_url_data[0])
                    # print(sql)
                    cur.execute(sql)
                sql = 'SELECT id, url FROM `processed_news` WHERE is_unique = 1'
                cur.execute(sql)
                data = cur.fetchall()


# comments pending. i'm too tired to comment now. i'll do it later :P. did it ;)
def mark_percent_unique():

    # remove duplicate urls.
    duplicate_url()

    import datetime
    import dbWorks.LCS as lcs

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    sql = 'SELECT * FROM `processed_news` ORDER BY `processed_news`.`original_date` ASC'
    cur.execute(sql)
    data = cur.fetchall()

    cur.execute("SELECT COUNT(id) FROM `processed_news`")
    items = cur.fetchone()

    for x in range(0, items[0]):

        # getting date of news as today and after the day  as tomorrow
        current_data = data[x]

        # only if data marked as unique will be processed
        if current_data[11] == 1:

            # get generated string containing sub-district ids and if it exists then continue
            str_for_compare = current_data[9]
            if len(str_for_compare) > 0:

                today = datetime.datetime.strftime(current_data[6], '%Y-%m-%d')
                tom = current_data[6] + datetime.timedelta(days=1)
                tomorrow = datetime.datetime.strftime(tom, '%Y-%m-%d')

                # if current new is already marked as duplicate then mark its original news id as current original news
                # if current_data[11] == 0:
                #     copy_of_id = current_data[12]
                # else:
                #     copy_of_id = current_data[0]
                copy_of_id = current_data[0]

                # omitting current test data and marked unique of test data to avoid confusion.
                # if current_data[0] != copy_of_id:
                #     sql = "SELECT id, upazilla_id_str, casualty_count, injury_count FROM `processed_news` WHERE " \
                #           "(original_date = " + repr(today) + " OR original_date = " + repr(tomorrow) + ") AND
                # (id <> "+ repr(current_data[0]) + " AND id <> " + repr(copy_of_id) + ")"
                # elif current_data[0] == copy_of_id:
                sql = "SELECT id, upazilla_id_str, casualty_count, injury_count, is_unique,  original_date, match_percent FROM" \
                      " `processed_news` WHERE (original_date = " + repr(today) + " OR original_date = " + \
                      repr(tomorrow) + ") AND id <> " + repr(current_data[0])
                # print(sql)
                cur.execute(sql)
                data_now = cur.fetchall()

                # omitting current test data and marked unique of test data to avoid confusion.
                # if current_data[0] == copy_of_id:
                sql = "SELECT COUNT(*) FROM `processed_news` WHERE (original_date = " + repr(today) +\
                      " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(current_data[0])
                # elif current_data[0] != copy_of_id:
                #     sql = "SELECT COUNT(*) FROM `processed_news` WHERE (original_date = " + repr(today) + \
                #           " OR original_date = " + repr(tomorrow) + ") AND (id <> " + repr(current_data[0]) +\
                #           " AND id <> " + repr(copy_of_id) + ")"
                cur.execute(sql)
                y = cur.fetchone()
                # print(y)

                if y[0] > 0:
                    for i in range(0, y[0]):
                        # compare every news data within the given two days
                        every = data_now[i]
                        # continue for unique news only
                        if every[4] == 1:
                            if len(every[1]) > 0:
                                # find match percentage between two strings using LCS
                                percent = lcs.similarity(str_for_compare, every[1])

                                # if a string is more than 75% match than marking it as duplicate news of lightning
                                if percent > 75:
                                    sql = "UPDATE `processed_news` SET match_percent = " + repr(percent)\
                                          + ", is_unique = 0, copy_of = " + repr(copy_of_id) + \
                                          " WHERE id = " + repr(every[0])
                                    cur.execute(sql)

                                    # update original news's death count and injury
                                    # count if duplicate news contains higher value
                                    sql = "SELECT casualty_count, injury_count FROM `processed_news` WHERE id = " \
                                          + repr(copy_of_id)
                                    cur.execute(sql)
                                    count_vals = cur.fetchone()
                                    death_count = count_vals[0]
                                    injured_count = count_vals[1]
                                    if every[2] > death_count or every[3] > injured_count:
                                        if every[2] > death_count:
                                            death_count = every[2]
                                        if every[3] > injured_count:
                                            injured_count = every[3]
                                        sub_sql = "UPDATE `processed_news` SET casualty_count = " + repr(death_count) +\
                                                  ", injury_count = " + repr(injured_count) + " WHERE id = " + repr(copy_of_id)
                                        # print(sub_sql)
                                        cur.execute(sub_sql)

                                # mark as unique if not duplicate
                                elif percent > 0 and percent > every[6]:

                                    if current_data[6] == every [5] and percent >= 50:
                                        if current_data[7] == every[2] or current_data[8] == every[3]:
                                            sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) \
                                                  + ", is_unique = 0, copy_of = " + repr(copy_of_id) + \
                                                  " WHERE id = " + repr(every[0])
                                            cur.execute(sql)
                                    else:
                                        sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) +\
                                              " WHERE id = " + repr(every[0])
                                        cur.execute(sql)

                                 # update data as data has been modified every time a duplicate news is found in the loop
                            # if current_data[0] != copy_of_id:
                            #     sql = "SELECT id, upazilla_id_str, casualty_count, injury_count FROM `processed
                            # _news` WHERE (original_date = " + repr(today) + " OR original_date = " + repr(tomorrow)
                            #  + ") AND (id <> " + repr(current_data[0]) + " AND id <> " + repr(copy_of_id) + ")"
                            # elif current_data[0] == copy_of_id:
                                sql = "SELECT id, upazilla_id_str, casualty_count, injury_count, is_unique, " \
                                      "original_date, match_percent FROM `processed_news` WHERE (original_date = "\
                                      + repr(today) + " OR original_date = " + repr(tomorrow) + ") AND id <> "\
                                      + repr(current_data[0])
                                # print(sql)
                                cur.execute(sql)
                                data_now = cur.fetchall()

            # update data as data has been modified every time a duplicate news is found in the inside loop
            sql = 'SELECT * FROM `processed_news` ORDER BY `processed_news`.`original_date` ASC'
            cur.execute(sql)
            data = cur.fetchall()


# mark_percent_unique()
