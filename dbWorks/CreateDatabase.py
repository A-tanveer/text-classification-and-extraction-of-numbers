# initial database creation and populating places tables
import pymysql
import dbWorks.ExecuteSqlFile as fileexec

# fileexec.execute_scripts_from_file('database.sql')

conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)

cur = conn.cursor()


# # cur.execute("select * from `district`")
# # # print(cur.description)
# #
# # for row in cur:
# #     print(row)
cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
cur.execute("TRUNCATE `district`;")
cur.execute("ALTER TABLE `district` AUTO_INCREMENT = 1;")

f = open('../places/201314zilla.txt', encoding='utf8')
lines = f.readlines()
# print(lines)
f.close()
a = 0
for line in lines:
    a += 1
    values = line.split(',')
    x = values[0].split()
    y = values[1]
    # print(x[0] + "   " + y[:len(y)-1] + "    " + values[0])
    if x[0].startswith('Cox'):
        z = x[0] + " " + x[1]
    else:
        z = x[0]
    div = values[2]
    sql = "SELECT division_id FROM `division` WHERE name = " + repr(div[:len(div)-1])
    cur.execute(sql)
    for row in cur:
        for val in row:
            sql = "INSERT INTO `district` (`division_id`, `name`, `bangla_name`) VALUES (" + repr(val) + ", "\
                  + repr(z) + ", " + repr(y) + ");"
    # print(a, sql)
    cur.execute(sql)


f = open('../places/201314upazilawithzila.txt', encoding='utf8')
lines = f.readlines()
f.close()
a = 0
for line in lines:
    value = line.split(',')
    x = value[0].split()
    y = value[1]
    if x[0].startswith('Cox') or x[0].startswith('matlab') or x[0].startswith('Char'):
        z = x[0] + " " + x[1]
    else:
        z = x[0]
    dist = value[2]
    sql = "SELECT district_id FROM `district` WHERE name = " + repr(dist)
    cur.execute(sql)
    # d = cur.fetchone()
    for i in cur:
        for d_id in i:
            # print(d_id)
            sql = "INSERT INTO `upazilla` (`district_id`, `name`, `bangla_name`) VALUES (" + repr(d_id) + ", " + \
                  repr(z) + ", " + repr(y) + ");"
            a += 1
            # print(a, sql)
            cur.execute(sql)

cur.close()
conn.close()
