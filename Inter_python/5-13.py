class charactor:

    def __init__(self,hp,attack,defence): #생성자, 메소드 이름 앞에 언더바가 2개 있으면 생성된 객체를 호출하지 말라는 의미
        self.hp=hp
        self.attack=attack
        self.defence=defence
        print('player가 생성되었습니다.')

    def move(self):
        print(self,'move')
        self.attack()
    
    def attack(self):
        print(self,'attack')
    
    def show_info(self):
        print("hp: %d, attack: %d, defence: %d " %(self.hp,self.attack, self.defence))
    
    def __del__(self): #소멸자
        print('player가 죽었습니다.')



player_a=charactor(10,20,30) #클래스 생성과 동시에 생성자 호출
player_b=charactor(100,200,300)

player_a.show_info()
player_b.show_info()

del player_a

print("=====program end=======")

#후에 프로그램이 종료될 때 소멸자를 호출함
    