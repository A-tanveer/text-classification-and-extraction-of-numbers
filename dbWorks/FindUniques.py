import pymysql


def get_sub_district(content):
    data = content.split('।')

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
    cur = conn.cursor()

    sql = 'SELECT * FROM `upazilla`'
    cur.execute(sql)
    sub_districts = cur.fetchall()

    sub_districts_found = []

    # looking for any sub divisions only in the lines having lightning info.
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


def mark_percent_unique():

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

        current_data = data[x]
        today = datetime.datetime.strftime(current_data[6], '%Y-%m-%d')
        tom = current_data[6] + datetime.timedelta(days=1)
        tomorrow = datetime.datetime.strftime(tom, '%Y-%m-%d')

        if current_data[10] == 0:
            copy_of_id = current_data[11]
        else:
            copy_of_id = current_data[0]

        str_for_compare = current_data[8]
        if len(str_for_compare) > 0:

            sql = "SELECT id, upazilla_id_str, casualty_count FROM `processed_news` WHERE (original_date = " +\
                  repr(today) + " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(current_data[0])
            cur.execute(sql)
            data_now = cur.fetchall()

            sql = "SELECT COUNT(*) FROM `processed_news` WHERE (original_date = " + repr(today) +\
                  " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(current_data[0])
            cur.execute(sql)
            y = cur.fetchone()

            for i in range(0, y[0]):

                every = data_now[i]
                print(every)
                if len(every[1]) > 0:
                    percent = lcs.similarity(str_for_compare, every[1])
                    if percent > 75:
                        sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) +\
                              ", is_unique = 0, copy_of = " + repr(copy_of_id) + " WHERE id = " + repr(every[0])
                        cur.execute(sql)
                        if every[2] > current_data[7]:
                            sub_sql = "UPDATE `processed_news` SET casualty_count = " + repr(every[2])
                            cur.execute(sub_sql)
                    elif percent > 0:
                        sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) + " WHERE id = " +\
                              repr(every[0])
                        cur.execute(sql)

                sql = "SELECT id, upazilla_id_str, casualty_count FROM `processed_news` WHERE (original_date = " + \
                      repr(today) + " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(current_data[0])
                cur.execute(sql)
                data_now = cur.fetchall()

        sql = 'SELECT * FROM `processed_news` ORDER BY `processed_news`.`original_date` ASC'
        cur.execute(sql)
        data = cur.fetchall()


# mark_percent_unique()



