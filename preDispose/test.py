# author:ever
# contact: test@test.com
# datetime:2020/6/19 23:51
# software: PyCharm

"""
文件说明：对清洗好的数据分析处理并可视化
    
"""
import re
#
# print(re.sub(r'[\[\]]+',"",re.sub(r'(?<=\[)(.*?)(?=\])',"","---[gfgd]---")))
# print()
str="安徽省 - 合肥市"
print(re.findall(r'-(.*?)$',str)[0].strip())