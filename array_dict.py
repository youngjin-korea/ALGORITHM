# number 리스트의 값을 counter 객체에 초기화하고 값을 카운트하기
numbers =[1,2,6,8,4,3,2,1,9,5]
counter={}

for number in numbers: 
    if number not in counter:
        counter[number] = 0
    counter[number] +=1

print(counter)

# range(a) 0~a 까지 a를 포함하지 않고
for _ in range(5):
    print(_)

# range(a,b) a~b b포함하지 않고
for _ in range(2,10):
    print(_)

# range(a,b,c) a~b b포함하지 않고 c만큼 건너띄며
for _ in range(2,8,-1):
    print(_)