# 파괴적 연산자

# 요소 추가 : append(), insert(), extend()
a= [1,2,3,4] 
a.append(10) # 가장 마지막에 숫자 추가
a.insert(0,1) # (넣을 인덱스, 넣을 값)
a.extend([1,2,3,4]) # 가장 마지막에 요소를 추가

# 요소 제거 : del, pop(), remove(), clear()
del a[0] # 제거하고 싶은 인덱스 입력
a.pop() # 제거하고 싶은 인덱스 입력, 기본 -1 (뒤에서 삭제)
a.remove(3) #제거하고 싶은 요소를 입력
a.clear() # 모두 제거

# 요소 정렬 : sort()
b=[52,273,211]
b.sort() # 오름차순
b.sort(reverse=True) # 내림차순

# 요소 존재를 확인 : in, not in
print(52 in b)
print(0 not in b)

# ========   반복문 ===============

# for 반복변수 in 리스트:
#   복합구문 
v = [1,2,3,4,5]

for it in v:
    print(it)

# 반복문 총합
sum = 0 # 합의 항등원 0(연산을 해서 자기 자신)
for it in v:
    sum += it
print(sum)

# 반복문 총곱
multiple = 1 # 곱의 항등원 1(연산을 해서 자기 자신)
for it in v:
    multiple *= it
print(multiple)

# dictionary 
product = {"name": "7D 건조망고", "type": "당절임"}

# 키의 존재 확인하는 법
if "price" in product: 
    print(product["price"])
else:
    print("아직 가격 요소가 없습니다")

#get()
if product.get("price") != None:
    print(product['price'])
else:
    print("아직 가격 요소가 없습니다.")

# pets 딕셔너리를 빼서 프린트 찍기
pets =[{"name": "구름", "age":5},{"name": "초코", "age":3},{"name": "아지", "age":1},{"name": "호랑이", "age":1},]

print("# 우리 동네 애완 동물들")
for pet in pets: 
    print(f'{pet["name"]} {pet["age"]}살')
