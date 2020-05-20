var = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
print(var.keys())
# key를 list처럼 만듦(list는 아님)

print(var.values())

print(var.items())
# (key,value)튜플 형태로 리스트처럼 만들어줌
# 위의 것들은 리스트는 아니기 때문에 인덱싱, 슬라이싱은 불가능 하지만
# 리스트처럼 반복문을 돌릴 수 있음 -> iterator
# list()를 이용하여 리스트 타입으로 바꾸는 것도 가능

values = list(var.values())  # 리스트로 변경
print(values)
print(values[0])

print('key1' in var)  # 키 존재 유무 검사 -> True
print('hello' in var)  # False
