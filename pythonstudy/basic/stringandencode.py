print('包含中文的str')
print('对于单个字符的编码，Python提供了:\n ')

print('ord()函数获取字符的整数表示:\n ')
print(r'''ord('A')''',ord('A'))


print('chr()函数把编码转换为对应的字符:\n ')
print(r'''chr('66')''',chr(66))


print(r''''ABC'.encode('ascii')''','ABC'.encode('ascii'),'\n')
print(r''''b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')''',b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'),'\n')

