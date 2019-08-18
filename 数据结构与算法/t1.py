import json
stus={'xiaojun':'123456','xiaohei':'7891','abc':'11111'}
#先把字典转成json
res2=json.dumps(stus)
print(res2)#打印字符串
print(type(res2))#打印res2类型
for i in stus:
    print(stus[i].value)
