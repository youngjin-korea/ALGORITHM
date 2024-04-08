# 문자열[인덱스] -> 인덱스 번째 문자 (용어: 인덱싱)
# 문자열[인덱스,인덱스] -> 인덱스 번째 문자 ~ 인덱스-1 번째 (슬라이싱)
# 문자열[인덱스,인덱스,스탭] -> 인덱스 번째 문자 ~ 인덱스-1 번째 범위에서 스탭 만큼 보폭 (슬라이싱)

# escape 역슬래쉬 \', \", \\, \n

# 문자열 연결
print('kim'+'is'+'name')

# 문자열 반복
print('kim'*3)

# 문자열을 뒤집는 결과 
print('0123456789'[::-1])

# 슬라이싱 [startIndex:endIndex] -> startIndex 부터 endIndex-1 번째 까지
print('01234'[:3])

print('01234'[1:])

# 슬라이싱 with 스탭 [startIndex:endIndex:step] -> startIndex 부터 endIndex-1 번째 까지 범위에서 step씩 띄어서 출력
print('0123456789'[::3])


# 타입 확인하는 메소드 type()
print(type(5),
type(5.0),
type('isString?'))

 #split() -> 문자열을 배열로 분리
print('a b c d'.split())
print('a.b.c.d'.split('.'))

# f문자열 
print(f'{1997}+{8}={1997+8}')
print('{}+{}={}'.format(1997,8,1997+8))