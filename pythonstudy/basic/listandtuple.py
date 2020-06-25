#!/usr/bin/env python3
# _*_coding:utf-8 _*_
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017092876846880
#list  可变 append追加  insert插入  pop删除  默认最后一个元素  【index】
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print('取出第一个（index为0） 的元素')
# classmates[0]#取出第一个（index为0） 的元素classmates[0] ='sdf'
print(classmates[0])

print('修改第一个（index为0） 的元素 ',r'''classmates[0] ='sdf''')
#修改第一个（index为0） 的元素
classmates[0] ='sdf'
print(classmates[0] )

print('取出第一个（index为0） 的元素')
print(classmates[-1])#取出第一个（index为0） 的元素



print(r'''classmates[0]='ZQQ''')
classmates[0]='ZQQ'
print(classmates)


print('classmates.insert(0,\'Job\')')
classmates.insert(0,'Job')
print(classmates)

print('classmates.pop()')
classmates.pop()
print(classmates)

print('classmates.pop(1)')
classmates.pop(1)
print(classmates)

#tuple 不可变
t=() #空tuple
s=(1,) #单一元素
y =(1,2,3)#多元素