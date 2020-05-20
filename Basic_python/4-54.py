var = {}
var["key1"] = 10
var["key2"] = 20
print(var)

var = {}
var.setdefault('key1', 10)
print(var)
var.setdefault('key1', 20) #key1의 값이 바뀌지 않음 
var.setdefault('key2', 30)
print(var)

