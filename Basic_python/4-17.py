var = '19,000원'
var = var.replace(',', '')
print(var)
var = var.replace('원', '')
print(var)

var = '19,000원'
var = var.replace(',', '').replace('원', '')  # 한줄로 표현 가능
print(var)
