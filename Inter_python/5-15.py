class charactor:

    def __init__(self,hp,attack,defence): #생성자, 메소드 이름 앞에 언더바가 2개 있으면 생성된 객체를 호출하지 말라는 의미
        self.hp=hp
        self.attack=attack
        self.defence=defence
        print('player가 생성되었습니다.')
    
    def __call__(self): #객체를 호출할 때 실행되는 메소드, run()같은 역할 
        print("hp: %d, attack: %d, defence: %d "%(self.hp,self.attack,self.defence))
    
    def __getitem__(self,name):
        if name=='hp':
            return self.hp
        elif name=='attack':
            return self.attack
        elif name=='defence':
            return self.defence
        else:
            return "존재하지않는키값입니다."

player_a=charactor(10,20,30)
player_b=charactor(100,200,300)

player_a()
player_b()

print(player_a.hp) #속성에 접근 가능, but 메소드와 헷갈림
print(player_b.attack)

print(player_a['hp'])
print(player_b['attack'])