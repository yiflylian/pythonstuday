print(r'''条件判断可以让计算机自己做选择，Python的if...elif...else很灵活。

条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。''')
bmi = 50.5/(1.75*1.75)
print(bmi)

if bmi<18:
    print('过轻')
elif bmi<25:
    print('正常')
elif bmi<32:
    print('肥胖')
else :
    print('严重肥胖')
