var0 = 'I am'+'미란'
print(var0)

var1 = "I am {name}".format(name="미란")
print(var1)

var2 = "I am {0}".format("미란")
print(var2)

var3 = "I am {} I am {}".format("미란", "동국")
print(var3)

# + 연산을 이용하여 문자열을 만들 경우 문자형 + 숫자인 경우 에러 발생

age = 25
var0 = 'I am age '+str(age)  # str을 사용하여 형변환을 해줘야 함
var1 = 'I am age {0}'.format(age)  # 자료형 상관없이 합치기 가능

print(var0)
print(var1)
