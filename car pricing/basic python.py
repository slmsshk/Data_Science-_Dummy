# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:51:57 2022

@author: Slmss
# """
# # VAriable - container to store values

# # salem = "Salem"
# # Read about variable naming conventions

# # print("salem",2,3)

# # Data Types
# # print(type("salem")) #string https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# # print(type(1)) #integer
# # print(type(1.5)) #float

# # List https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# x=[45,85,"Salem",1.5]

# print(x[1:3])

# # Conditions
# # https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
# # https://docs.python.org/3/library/stdtypes.html#comparisons
# a=1
# b=2

# if a>b:
#     print('greater')
# elif b==a:
#     print('equal')
# else:
#     print('b is greater')
    
# # Loops
# # For loop

# # for i in range(0,9):
# #     print(i)

# for i in x:
#     print(i)
#     if i==45:break

# y=0
# while True:
#     print('a')
#     y=y+1
#     if y==5:break

# # 

# for i in range(1,21,2):
#     print(i)

# import pandas as pd
data =pd.read_csv(r"\Users\Slmss\Desktop\excelr\Cars.csv")
    
