# -*- coding: utf-8 -*- 



# 列表推导只取有:的
data_school = [x for x in data if ":" in x]
# 字典推导，用:前的国家代码当成键
dict_school = {x.split(":")[0]:x.split(":")[1] for x in data_school}
print (dict_school)
# 列表推导包字典，用:前的国家代码当成键
list_dict_school = [{'c_code': k, 'c_name': v} for k,v in dict_school.items()]
print (list_dict_school)
# ---------------------------------------------------


# 使用csv模块，将国家代码及简中国家名称数据输出至data\class.tsv备用
# 英： https://docs.python.org/3/library/csv.html#csv.DictWriter
# 中： http://python.usyiyi.cn/translate/python_352/library/csv.html
import csv
with open('data\基本情况.tsv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['c_code', 'c_name']
    writer = csv.DictWriter(csvfile, fieldnames=['c_code', 'c_name'])
    writer.writerows (list_dict_school)
