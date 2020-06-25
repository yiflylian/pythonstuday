#https://www.liaoxuefeng.com/wiki/1016959663602400/1017100774566304

print(r'''

Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
执行这段代码，会依次打印names的每一个元素：

Michael
Bob
Tracy
所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：

>>> list(range(5))
[0, 1, 2, 3, 4]
range(101)就可以生成0-100的整数序列，计算如下：

# -*- coding: utf-8 -*-
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


''')

names=['michael','Bob','tracy']
for name in names:
    print(name)

print(r''' range()函数  比如range(5)生成的序列是从0开始小于5的整数''')
print(r''' 

for i in range(101):
    sum+=i

print(sum)
''')
sum =0
for i in range(101):
    sum+=i

print(sum)

print(r''' 
第二种循环是while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和，可以用while循环实现：
sum  =0
n=99
while n>0:
    sum = sum+n
    n=n-2
print(sum)  
''')

sum  =0
n=99
while n>0:
    sum = sum+n
    n=n-2
print(sum)

print(r'''

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,',name,'!')

''')
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,',name,'!')
print(r'''
循环是让计算机做重复任务的有效的方法。

break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

请试写一个死循环程序。
''')