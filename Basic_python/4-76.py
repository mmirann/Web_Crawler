# -*- coding: utf-8 -*-

count=0

while count <5:
    print("%d "%(count))
    count+=1


for i in range (0,5):
    print("%d "%(i))
# i�� range������� ������Ŵ

#���ڿ� �� ��� �ݺ�
for i in 'hello world':
    print(i)

#����Ʈ �� ��� �ݺ�
for i in [11,22,33,44,55]:
    print(i)

var={'key1':'value1','key2':'value'}

for key in var:
    print(key)
    print(var[key])
#��ųʸ��� �̿��� Ű�� ������
# �����ų ������ Ű�� �������� ������ �޶���(��ųʸ��� ������ ���� ����)