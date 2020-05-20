var = [1, 2, 3, 4, 5]
var.append(10)
print(var)
var.append(20)
print(var)

# 리스트 정렬
var = ['a', 'b', 'c', 'd']
var.sort() #오름차순 정렬, 대문자와 소문자가 섞여있다면 대문자 먼저 정렬
print(var) 
var.sort(reverse=True) #내림차순 정렬
print(var)
