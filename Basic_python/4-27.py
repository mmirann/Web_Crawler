
var1 = "hello world"
var2 = "HELLO WORLD"
var3 = "HELLO world"

print(var1.upper())
print(var2.lower())
print(var3.upper())  # 소문자만 찾아서 대문자로 변환

print(len(var1))  # len(변수) 형태

var4 = "   Hello world    "
print(var4.rstrip())  # 우측 공백 제거
print(var4.lstrip())  # 좌측 공백 제거
print(var4.strip())  # 양쪽 공백 제거
