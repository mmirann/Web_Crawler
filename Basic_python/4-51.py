# 딕셔너리 -> 리스트와 다르게 순서가 존재하지 않음
# 리스트는 0,1,2.. 순서가 존재하지만 딕셔너리는 저장되는 순서와 상관없이 데이터를 읽고 쓸 수 있음
# {} 중괄호로 감싸서 표현하고 key-data형태로 데이터를 저장

var1 = dict({"key1": "value1", "key2": "value2"})
var2 = {"key1": "value1", "key2": "value2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])

print(var1["key3"])
# 인덱스로 접근할 때 존재하지 않는 인덱스에 접근하려고 하면 에러 발생

# get()을 이용하면 됨

print(var1.get("key1"))
print(var1.get("key3"))  # 키가 없으면 None을 출력
print(var1.get("key3", "default value"))  # 키가 없으면 기본 값을 설정
