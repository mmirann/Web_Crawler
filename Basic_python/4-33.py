var = list([1, 2, 3, 4, 5])
print(var)
var = [1, 2, 3, 4, 5]
print(var)

a = ["1", "2", "3", "4", "5"]
b = ".".join(a)  # 리스트 각각의 요소가 문자형일 때만 사용 가능!
print(b)

var2 = [6, 7, 8, 9, 10]
print(var2*3)  # 3번의 리스트 반복
print(var+var2)

var[2:4] = [0, -1]
print(var)
var2[2:4] = [0, -1, -2]  # 2,3번째 인덱스만 수정되는 게 아닌 -2가 추가되어 수정됨
print(var2)

