# 리스트의 요소를 삭제하는 방법
# 1. 인덱스 이용 -> del 객체
# 2. 슬라이싱 이용 -> []으로 수정
# 3. Remove 이용 -> 해당하는 요소를 find해서 제거, 중복되ㅡㄴ 게 있을 경우 먼저 등장하는 것 제거

var1 = [1, 2, 3, 4, 5]
var2 = [1, 2, 3, 4, 5]
var3 = [1, 2, 3, 4, 5]
del var1[1]
var2[0:3] = []
var3.remove(4) #4

print(var1)
print(var2)
print(var3)