import pymysql
import dbWorks.FindUniques as FU

conn = pymysql.Connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
cur = conn.cursor()

sql = 'SELECT * FROM `processed_news` ORDER BY `processed_news`.`original_date` ASC'

cur.execute(sql)
all_data = cur.fetchall()
for row in all_data:

    text_now = repr(row[1])
    upazilla_id_str = FU.get_sub_district(text_now)

    FU.update_news_id_str(row[0], upazilla_id_str)

FU.mark_percent_unique()

cur.close()
conn.close()
