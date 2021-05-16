# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 0026 11:22
# @Author  : Yang
# @Email   : 2635681517@qq.com
# @File    : test3.py
# @Software: PyChar
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

excel_file_path = 'paper_publish.xls'
new_df = pd.read_excel(excel_file_path)
columns = ['employee_no', 'publication_category', 'audi_status', 'author_order', 'sign_no', 'person_rank',
           'exam_status', 'real_name',
           'publish_time']
df = pd.DataFrame(new_df, columns=columns)
df1 = df.groupby('employee_no').first().reset_index()
df2 = df.groupby('employee_no')['real_name'].count().to_frame().reset_index()
df2.rename(columns={"real_name": "nums"}, inplace=True)
df1.insert(9, 'nums', df2['nums'])

print(df1)

# # 二种标记法
# sign_no_mapping = {'一人': 1, '二人': 2, '三人': 3, '四人': 4, '五人': 5, '六人': 6, '七人': 7, '八人': 8,
#                    '九人': 9, '十人': 10, '十一人': 11, '十二人': 12, '十三人': 13, '十四人': 14, '十五人': 15, '十六人': 16,
#                    '十七人': 17, '十八人': 18, '十九人': 19, '二十人': 20,
#                    '二十一': 21, '二十二人': 22, '二十三人': 23, '二十四人': 24, '二十五人': 25, '三十六人': 36}
#
# df1['sign_no'] = df1['sign_no'].map(sign_no_mapping)
# person_rank_mapping = {'第一': 1, '第二': 2, '第三': 3, '第四': 4, '第五': 5, '第六 ': 6, '第七 ': 7,
#                        '第八 ': 8, '第九 ': 9, '第十 ': 10,
#                        '第十一 ': 11, '第十二 ': 12, '第十三 ': 13, '第十四 ': 14, '第十五 ': 15, '第十六 ': 16,
#                        '第十七 ': 17, '第十八 ': 18, '第十九 ': 19, '第二十 ': 20, '第二十一': 21, '第二十二 ': 22}
#
# df1['person_rank'] = df1['person_rank'].map(person_rank_mapping)
# publish_time_list = []
# for pub_time_list in list(df1['publish_time']):
#     publish_time_list.append(int(pub_time_list[0:4]))
#
# df1['publish_time'] = publish_time_list
#
# publication_category_mapping = {'一般期刊': 5, "一般期刊（长江大学学报）": 6, '国外期刊': 8, '核心期刊': 10, '学科权威期刊': 15,
#                                 '核心期刊 [长江油气/长江医学(英文刊)]': 7}
# df1['publication_category'] = df1['publication_category'].map(publication_category_mapping)
#
# author_order_mapping = {'第一作者': 10, '第二作者': 5, '通讯作者': 3}
# df1['author_order'] = df1['author_order'].map(author_order_mapping)
# audi_status_mapping = {'院(处)审核未通过': 0.5, '学校审核未通过': 1, "未审核": 2, "院(处)审核通过": 5, '学校审核通过': 10}
# df1['audi_status'] = df1['audi_status'].map(audi_status_mapping)
# df1['publish_time'] = LabelEncoder().fit_transform(df1['publish_time'])
# exam_status_mapping = {'不参加考核仅作绩效统计': 2, '参加考核不作绩效统计': 10, '参加考核与绩效统计': 20}
# df1['exam_status'] = df1['exam_status'].map(exam_status_mapping)
# print(df1.corr())
# df1.corr().to_csv('corr.csv')
#
# # data_corr
# colormap = plt.cm.RdBu
# plt.figure(figsize=(20, 20))
# # plt.title('Pearson Correlation of Features', y=1.05, size=15)
# sns.heatmap(df1.corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
# plt.show()
