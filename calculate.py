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