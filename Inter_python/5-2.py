
def division(x):
    if x%2:
        return True
    else:
        return False

    print("running") #return에서 종료됐으므로 출력되지 않음 

var1=division(10)
var2=division(11)

print(var1)
print(var2)

def f(x):
    print('running'+str(x))

var=f(10)
print(var) # 반환되는 값이 없으므로 None을 출력

def f(x,y=20):
    print('running '+str(x)+' '+str(y))
    return True

var1=f(10)
var2=f(10,40) #기본값을 설정했어도 전달된 인자의 값으로 출력됨
print(var1)