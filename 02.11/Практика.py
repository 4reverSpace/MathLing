import re
import pymorphy2
a=re.split("\b\w+\b",input(),maxsplit=0)
#или без знаков -a=input().split() 
for i in a:
    print(i,"1")
    print((pymorphy2.MorphAnalyzer()).parse(i))#разбор
    print(morph.parse(i)[0].normal_form)#обычная форма
Может быть никто из живущих в Москве 
