#!/use/bin/env python
# -*- coding:utf-8 -*-
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
def abs_pro(x):
    pre_x=x
    new_x=my_abs(x)
    return pre_x,new_x
n=0
while n==0:
    x=int(input("请输入一个数判断其绝对值:"))
    pre_x,new_x=abs_pro(x)
    print(pre_x,"的绝对值是",new_x)
    print("是否继续判断？输入0为继续，反之停止")
    n=int(input())
    if n!=0:break

