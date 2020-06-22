# author:ever
# contact: test@test.com
# datetime:2020/6/19 22:23
# software: PyCharm

"""
文件说明：数据清洗
    
"""
# import pandas as pd
import re
# import numpy as np
# df=pd.read_csv('../dataSource/backlighting.csv',header=None,sep=',') #filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符，如果分隔符是逗号，只需换成 ‘，'即可。
# df = pd.read_csv("../dataSource/backlighting.csv")

# print(df.columns)                         #返回全部列名
# print(df.shape)
# print(df.shape[0])
# print(re.search(r'[\[\]]+',df))
# print(df.columns)
# df.drop(index=(df.loc[(re.search(r'[\[\]]+',df[""])!=None)].index))
import csv
import collections
import pyecharts
from bean.item import comment_item
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
import matplotlib.pyplot as plt # 图像展示库

def make_list():
    f=open("../dataSource/country.csv",'r',encoding="utf-8")
    file=csv.reader(f)
    list=[]
    i=0
    for temp in file:
        if i!=0 and len(temp)==11:
            #把是否是VIP转换成True or False
            flag=False
            # print(temp)
            if temp[1]=="是":
                flag=True
            #利用正则表达式去除表情等有关的无用字符
            if re.sub(r'[\[\]]+',"",re.sub(r'(?<=\[)(.*?)(?=\])',"",temp[10]))!="":
                #替换评论内容中的换行符
                i=comment_item(temp[0],flag,temp[2],temp[3],temp[4],temp[5],temp[6],int(temp[7]), temp[8], temp[9], re.sub(r'\n',"",temp[10]))
                # print(i)
                list.append(i)
            # else:
                # print(temp[5])
        i=1
    return list

def write():
    f = open('disposed.csv', 'w', encoding='utf-8')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f, lineterminator='\n')
    csv_writer.writerow(["user", "VIP", "dynamic", "foucs", "fans", "district", "listen_songs", "acclaim", "comment", "time", "content"])
    for temp in make_list():
        print(temp)
        csv_writer.writerow([temp.name, temp.vip, temp.dynamic, temp.foucs_num, temp.fans, temp.district, temp.listen_songs, temp.acclaim, temp.commented_num, temp.time, temp.content])
    print("ok")
    f.close()
write()
def make_wordCloud():
    object_list=[]
    for temp in make_list():
        object_list.append(temp.content)
    print(len(object_list))
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查
    wc = wordcloud.WordCloud(
        font_path = 'C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        max_words = 200,  # 最多显示词数
        max_font_size = 100  # 字体最大值
    )
    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    # image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    # wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()  # 显示图像

# make_wordCloud()

def VIP_rate():
    true=0
    false=0
    for temp in make_list():
        if temp.vip:
            true+=1
        else:
            false+=1
    pie = pyecharts.Pie("评论用户中是否VIP比列", '逆光-孙燕姿', title_pos='center')
    pie.add('天气类型', ["vip用户","非vip用户"], [true,false],is_label_show=True,legend_pos = 'left', label_text_color = None, legend_orient = 'vertical', radius = [30, 75])
    pie.render('Pie-weather.html')