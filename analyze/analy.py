# author:ever
# contact: test@test.com
# datetime:2020/6/22 18:14
# software: PyCharm

"""
文件说明：
    
"""
import pyecharts
from snownlp import SnowNLP
import pandas as pd
import numpy as np
import csv


def get_content():
    '''

    @return:
    '''
    lists=[]
    f=open("../preDispose/disposed.csv",'r',encoding="utf-8")
    file=csv.reader(f)
    count=0
    for i in file:
        if count!=0:
            print(i[10])
            s = SnowNLP(i[10])
            print(str(s.sentiments))
            lists.append(s.sentiments)
        count+=1;
    return lists

def draw_line_sentiment(lists):
    line = pyecharts.Line("情感分析得分走势图", width=1200, height=600)
    line.add("情感分析得分",list(range(1,len(lists)+1)),lists, mark_point=['average'], is_datazoom_show=True,is_smooth=True)
    line.render('line_sentiments.html')

#-----------------------------------
def draw_pie_sentiment(lists):
    s = np.arange(0, 1.1, 0.1)
    fenzu = pd.cut(lists, s, right=False)  # 分组区间,长度91
    pinshu = fenzu.value_counts()  # series,区间-个数
    print(fenzu.categories)
    list_label=["(0.0-0.1)", "(0.1-0.2)", "(0.2-0.3)", "(0.3-0.4)", "(0.4-0.5)", "(0.5-0.6)", "(0.6-0.7)", "(0.7-0.8)", "(0.8-0.9)", "(0.9-1.0)"]
    pie = pyecharts.Pie("评论情感色彩评分", '0->1（消极->积极）', title_pos='center')
    pie.add('天气类型', list_label, pinshu.tolist(),radius=[20,70],is_label_show=True,legend_pos = 'left', label_text_color = None, legend_orient = 'vertical')
    pie.render('pie_sentiments.html')