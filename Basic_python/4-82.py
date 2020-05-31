var = 'egoism,as a form of hedonism, is the doctirne which holds that we ought each of us to pursue our own greates gappiness as our ultimate end, the doctrine will, of course, admit that sometimes the best means to the end will be to give pleasure to others; we shall, for instance, by so doing, procure for ourselves the pleasure of sympathy, of freedom from interference, and of self-esteeml and these pleasures, which we may procure by something aiming directly at the happiness of other persons, may be greater than any we could otherwise get.'

space_ps=var.split(' ')

char_frequency={}

for char in space_ps:
    char_frequency.setdefault(char,0) #setdefault: 키가 없을 땐 키를 생성해서 값을 넣고, 키가 존재할땐 어떤 작업도 안함
    char_frequency[char]+=1 #단어의 키가 있다면 0으로 값이 바뀌지 않고 +1만 된다.

print(char_frequency)