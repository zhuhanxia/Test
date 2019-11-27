# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:48:24 2019

@author: zhuha 
"""


"""name_list=['Tom','Lily','Rose']

print(name_list.index('Lily',0,2))
print(name_list.count('Tom'))
print(len(name_list))

print("Lily" not in name_list)


for i in name_list:
    print(i)
"""

import random

name_list=[['a','b','c'],['张三','李四','王五'],['小红','小明']]
print(name_list[0][1])


teacher=['a','b','c','d','e','f','g','h']
offices=[[],[],[]]

for name in teacher:
    num=random.randint(0,2)
    offices[num].append(name)
    
i=0
for office in offices:
    print(f'办公室{i}人数是{len(office)}，老师分别是：')
    for name in office:
        print(name)
    i=i+1 

