# author:ever
# contact: test@test.com
# datetime:2020/6/19 23:51
# software: PyCharm

"""
文件说明：对清洗好的数据分析处理并可视化
    
"""
# TODO tooltip->悬浮框组件，用于移动或点击鼠标鼠标时候弹出数据内容
import pyecharts
from Demos.win32cred_demo import env

line = pyecharts.Line("tooltip提示框配置信息测试")
line.add("line",["测试1","测试2","测试3"],[10,80,0],
         tooltip_trigger="axis" , # 触发类型，item=数据项触发，默认，主要在散点图，饼图等无类目图中使用，xais=坐标轴触发，主要在柱状图，折线图等有类目的途中使用，none=什么都不触发
         tooltip_trigger_on="click", # 触发条件, mousemove=鼠标移动的时候，click=电机的时候，mousemove|click=点击或移动的时候，none=不触发
         tooltip_axispointer_type="cross", # 指示器类型，默认=line，直线，shadow=隐形，cross=十字准星
         tooltip_formatter= '{c}', # str类型，{a}=系列名称add第一个参数，{b}=对应的x轴值，{c}=x,y坐标
         tooltip_text_color= "red", # 提示框文本的颜色
         tooltip_font_size=20, # 提示框字体的大小
         tooltip_background_color="pink", # 提示框背景色
         tooltip_border_color="green", # 提示框边框的颜色
         tooltip_border_width=10, # 边框的宽度
         )
line.render_chart_to_file(line,path="提示框配置项.html")