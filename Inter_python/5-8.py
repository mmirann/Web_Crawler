
class charactor:
    def move(self):
        print(self,'move') #self=this, 객체가 메소드를 호출할 때 어느 객체가 호출한 건지 알려줌
        self.attack() # 객체로부터 직접 호출된 메소드가 다른 메소드를 호출할 때는 self를 명시해주어야 사용가능
    def attack(self):
        print(self,'attack')

player_a=charactor()
player_b=charactor() #객체 생성 

player_a.move()
player_b.attack() #self를 프린트했을 때 at ~숫자가 나타남, 객체의 메모리 주소값을 의미 => self