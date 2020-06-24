#!/usr/bin/env python3
# _*_coding:utf-8 _*_
print('字符串 跟 编码')
print('包含中文的str')
print('对于单个字符的编码，Python提供了:\n ')

print('ord()函数获取字符的整数表示:\n ')
print(r'''ord('A')''',ord('A'))


print('chr()函数把编码转换为对应的字符:\n ')
print(r'''chr('66')''',chr(66))


print(r''''ABC'.encode('ascii')''','ABC'.encode('ascii'),'\n')
print(r''''b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')''',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'),'\n')


print('如果知道字符的整数编码，还可以用十六进制这么写str：\n')
print(r''''\u4e2d\u6587''','\u4e2d\u6587')

print(r'''如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：''','\n')
print(r''' b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')''', b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

print(r'''要计算str包含多少个字符，可以用len()函数：''')
print(r'''len(b'ABC')''',len(b'ABC'))

print(r'''len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：''')
print(r'''len(b'\xe4\xb8\xad\xe6\x96\x87')''',len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(r'''如果.py文件本身使用UTF-8编码，并且也申明了# -*- coding: utf-8 -*-，打开命令提示符测试就可以正常显示中文：''','\n')
print(r'''在Python中，采用的格式化方式和C语言是一致的，用%实现''','\n')
print(r''''Hi, %s, you have $%d.' % ('Michael', 1000000)''','\n','Hi, %s, you have $%d.' % ('Michael', 1000000),'\n')


