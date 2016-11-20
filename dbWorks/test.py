import pymysql
#
#
# data = 'ফরিদপুরের ভাঙ্গা ও পঞ্চগড়ের দেবীগঞ্জে গত বুধ ও বৃহস্পতিবার বজ্রপাতে দুটি বিদ্যালয়ের ২৬ জন ছাত্রছাত্রী আহত হয়েছে। ভাঙ্গার চান্দ্রা ইউনিয়নের মালিগ্রাম' \
#        ' পাইলট উচ্চবিদ্যালয়ে বৃহস্পতিবার বজ্রপাতে ১৫ জন শিক্ষার্থী আহত হয়। তাদের উপজেলা স্বাস্থ্য কমপ্লেক্সে ভর্তি করা হয়েছে। প্রধান শিক্ষক বিমল চন্দ্র ঘোষ ' \
#        'জানান, ‘আমরা তখন ক্লাস নিচ্ছিলাম। হঠাৎ তীব্র আলোর ঝলকানির সঙ্গে গগনবিদারী শব্দে একাধিক বজ্রপাতের ঘটনা ঘটে। এতে বিদ্যালয় ভবনের এক অংশের' \
#        ' পলেস্তারা খসে পড়ে এবং বৈদ্যুতিক লাইন পুড়ে যায়। ষষ্ঠ থেকে দশম শ্রেণী পর্যন্ত সব ক্লাসের ১৫ জন শিক্ষার্থী আহত হয়। তাঁদের শরীর ঝলসে গেছে। ' \
#        'দেবীগঞ্জের দণ্ডপাল ইউনিয়নের দেবীডুবা খুটামারায় মির্জা গোলাম হাফিজ উচ্চবিদ্যালয়ের ১১ জন শিক্ষার্থী ও একজন কর্মচারী বুধবার বজ্রপাতে আহত হয়।' \
#        ' বজ্রপাতে তাদের শরীরের বিভিন্ন অংশ ঝলসে যায়।\n'
# data = data.split('।')
#
# conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
# cur = conn.cursor()
#
# # sql = 'SELECT * FROM `division`'
# # cur.execute(sql)
# # divisions = cur.fetchall()
# #
# # sql = 'SELECT * FROM `district`'
# # cur.execute(sql)
# # districts = cur.fetchall()
#
# sql = 'SELECT * FROM `upazilla`'
# cur.execute(sql)
# sub_districts = cur.fetchall()
#
# districts_found = []
# sub_districts_found = []
#
# # for row in districts:
# #     for line in data:
# #         if 'বজ্র' in line:
# #             if row[3] in line:
# #                 districts_found.append(row[0])
# #
# # if len(districts_found) > 0:
# #     x = 0
# #     sql = "SELECT * FROM `upazilla` WHERE "
# #     for d_id in districts_found:
# #         if x == 0:
# #             x = 2
# #             sql += 'district_id = ' + repr(d_id)
# #         elif d_id:
# #             sql += ' or district_id = ' + repr(d_id)
# # cur.execute(sql)
# #
# # upazila = cur.fetchall()
# #
# # for row in upazila:
# #     for line in data:
# #         if 'বজ্র' in line:
# #             if row[3] in line:
# #                 upazila_list.append(row[0])
# #                 ul.append(row[2])
# #                 ul.append(row[3])
#
# for row in sub_districts:
#     for line in data:
#         if 'বজ্র' in line:
#             if row[3] in line:
#                 sub_districts_found.append(row[2])
#                 # ul2.append(row[2])
#                 # ul2.append(row[3])
# outstr = ''
# outstrlist = []
# # sub_districts_found = sorted(set(sub_districts_found))
# for sub_district in sub_districts_found:
#     sql = "SELECT MIN(upazilla_id) FROM `upazilla` WHERE name = " + repr(sub_district)
#     cur.execute(sql)
#     u = cur.fetchone()
#     outstrlist.append(u[0])
#
# outstrlist = sorted(set(outstrlist))
# for element in outstrlist:
#     var = '%03d' % element
#     outstr += var + ' '
#
#
# # print(sorted(set(upazila_list)))
# # print(sorted(set(ul)))
# print(sorted(set(sub_districts_found)))
# print(outstr)


# def mark_percent_unique():
#
#     import datetime
#     import dbWorks.LCS as lcs
#
#     conn = pymysql.connect(host='localhost', user='root', passwd='', db='places', charset='utf8', autocommit=True)
#     cur = conn.cursor()
#
#     sql = 'SELECT * FROM `processed_news` ORDER BY `processed_news`.`original_date` ASC'
#     cur.execute(sql)
#     data = cur.fetchall()
#
#     x = 0
#
#     for row in data:
#         row = data[x]
#         today = datetime.datetime.strftime(row[6], '%Y-%m-%d')
#         tom = row[6] + datetime.timedelta(days=1)
#         tomorrow = datetime.datetime.strftime(tom, '%Y-%m-%d')
#
#         if row[10] == 0:
#             copy_of_id = row[11]
#         else:
#             copy_of_id = row[0]
#
#         str_for_compare = row[8]
#         if len(str_for_compare) > 0:
#             sql = "SELECT id, upazilla_id_str, casualty_count FROM `processed_news` WHERE (original_date = " + repr(
#                 today) \
#                   + " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(row[0])
#             cur.execute(sql)
#             data_now = cur.fetchall()
#             for every in data_now:
#                 if len(every[1]) > 0:
#                     percent = lcs.similarity(str_for_compare, every[1])
#                     if percent > 75:
#                         sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) +\
#                               ", is_unique = 0, copy_of = " + repr(copy_of_id) + " WHERE id = " + repr(every[0])
#                         if every[2] > row[7]:
#                             sub_sql = "UPDATE `processed_news` SET casualty_count = " + repr(every[2])
#                             cur.execute(sub_sql)
#                     elif percent > 0:
#                         sql = "UPDATE `processed_news` SET match_percent = " + repr(percent) + " WHERE id = " +\
#                               repr(every[0])
#                     print(sql)
#
#                     cur.execute(sql)
#
#                     sql = "SELECT id, upazilla_id_str FROM `processed_news` WHERE (original_date = " + repr(today) \
#                           + " OR original_date = " + repr(tomorrow) + ") AND id <> " + repr(row[0])
#                     cur.execute(sql)
#                     data_now = cur.fetchall()
#         x += 1
#
#         # print(sql, str_for_compare)
#
# mark_percent_unique()
