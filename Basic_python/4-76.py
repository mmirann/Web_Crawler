# -*- coding: utf-8 -*-

count=0

while count <5:
    print("%d "%(count))
    count+=1


for i in range (0,5):
    print("%d "%(i))
# i를 range범위대로 증가시킴

#문자열 내 요소 반복
for i in 'hello world':
    print(i)

#리스트 내 요소 반복
for i in [11,22,33,44,55]:
    print(i)

var={'key1':'value1','key2':'value'}

for key in var:
    print(key)
    print(var[key])
#딕셔너리를 이용해 키를 가져옴
# 실행시킬 때마다 키를 가져오는 순서는 달라짐(딕셔너리는 순서가 없기 때문)