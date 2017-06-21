# -*- coding: utf-8 -*- 
# 类化，以备模块使用module调用（module）
import csv
"""创建一个类"""
class gd_school(object):

    def __init__(self, fn='data//uni.csv'):
        data = []

        with open(fn, 'r', encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            fieldnames = reader.fieldnames
            for row in reader:
                data.append(dict(row))

        # clean data 院校名称
        for d in data:
            d['院校名称'] = d['院校名称'].strip()

        list_school_names = [d['院校名称'] for d in data]


        #test
        #print(list_school_names)
        #print(data)

        self.data = data
        self.list_names = list_school_names
        




#測試   
#gd_s = gd_school()
#print(gd_s.data)
#print(gd_s.list_names)
