name='  aleX'
#01.移除 name 变量对应的值两边的空格，并输入移除后的内容
print(name.strip())

#02.判断 name 变量对应的值是否以  "al"  开头，并输出结果
l=list(name)
if l[0:2]=='al':
    print(True)
else:
    print(False)
print(name.startswith('al'))

#03.判断 name 变量对应的值是否以  "X"  结尾，并输出结果
if l[-1]=='X':
    print(True)
else:
    print(False)
print(name.endswith('X'))

#04.将 name 变量对应的值中的  “l”  替换为  “p”，并输出结果
print(name.replace('l','p'))

#05.将 name 变量对应的值根据  “l”  分割，并输出结果。
print(name.split('l'))
print(type(name.split('l')))

#06.将 name 变量对应的值变大写，并输出结果
print(name.upper())

#07.将 name 变量对应的值变小写，并输出结果
print(name.lower())

#08.请输出 name 变量对应的值的第 2 个字符？
print(l[2])

#09.请输出 name 变量对应的值的前 4 个字符？
print(name[0:4])

#10.请输出 name 变量对应的值的后 2 个字符？
print(name[-2:])

#11.请输出 name 变量对应的值中  “e”  所在索引位置？
print(name.index('e'))

#12.字符串是否可迭代？如可以请使用 for 循环每一个元素？
for item in name:
    print(item)

#13.请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li  ＝  ['alex',  'eric',  'rain']
li  =  ['alex',  'eric',  'rain']
print(li[0],'_',li[1],'_',li[2])
for q in li:
    print(q,'_ ',end='')
    print()

#14.计算列表长度并输出
print(len(li))

#15. 列表中追加元素 “seven”，并输出添加后的列表
li.append('seven')
print(li)

#16.请在列表的第 1 个位置插入元素 “Tony”，并输出添加后的列表
li.insert(0,'Tony')
print(li)

#17.请修改列表第 2 个位置的元素为 “Kelly”，并输出修改后的列表
# del (li[1])
# li.insert(1,'Kelly')
# print(li)
li[1]='Kelly'
print(li)

#18. 请删除列表中的元素 “eric”，并输出修改后的列表
li.remove('eric')
print(li)

#19.请删除列表中的第 2 个元素，并输出删除的元素的值和删除元素后的列表
del (li[1])
print(li[1])
print(li)

#20.请删除列表中的第 3 个元素，并输出删除元素后的列表
li.pop(2)
print(li)

#21.请删除列表中的第 2至4个元素，并输出删除元素后的列表
del (li[1:4])
print(li)

#22.请将列表所有的元素反转，并输出反转后的列表
li=['tony','alex','eric','rain','seven']
print(li[::-1])

#23.请使用for、len、range输出列表的索引
li=['tony','alex','eric','rain','seven']

for i in range(len(li)):
    print(i,li[i])

#24.请输出 “Kelly”
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][1][1])

#25. 请使用索引找到 'all' 元素并将其修改为 “ALL”
li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][2].upper())
