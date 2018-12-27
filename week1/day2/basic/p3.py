'''
단일 데이터 > 문자열 데이터
표시방법
'''
# 'abc', "abc", '''abc''',"""abc"""
'''
위와 같이 4가지 형태로 가능함
주석용이나 여러줄을 표현할 때(구조를 유지) -> SQL 쿼리 사용
'''
a = 'hi'
print(a)
a = "hello"
print(a)

a = "I'm a programmer"
print(a)

a = 'I"m" a programmer'
print(a)

a = 'I\'m a programmer' # escape 특수문자 : \(백스페이스)를 사용 
print(a)

# 여러줄 표현
a = '''
손흥민의 활약이 매섭다. 현지 언론도 손흥민을 향해 극찬을 아끼지 않고 있다. 12월에만 리그 6골을 터트린 손흥민은 프리미어리그 사무국이 수여하는 '이달의 선수' 후보로도 떠올랐다. 이제 12월 남은 한 경기는 울버햄튼과의 프리미어리그 20라운드 홈 경기. 손흥민이 울버햄튼을 상대로 3경기 연속 골을 넣고 생애 3번째 '이달의 선수' 수상에 다가갈 수 있을까. 

12월에 치른 리그 6경기에서 6골을 넣은 손흥민은 현지 언론의 찬사를 받고 있다. 프리미어리그 공식 SNS는 "손타클로스가 마을에 왔다"고 표현했고, 마우리시오 포체티노 감독도 손흥민을 '어메이징'하다고 칭찬하는 등 호평이 이어졌다.

손흥민이 날카로운 골 감각을 선보이면서 '이달의 선수' 수상 여부가 팬들의 큰 관심사가 됐다. 이번 울버햄튼전에서도 맹활약을 펼친다면 가능성은 충분하다. 현재 토트넘은 손흥민 덕분에 리그 5연승을 달리고 있고, 순위도 맨시티를 제치고 2위로 올라섰다.
'''
print(a)

# 결국 얘도 문자열이지만...
'''
asldkfndslkfjslkdfj
'''
# 어느 변수도 가르키지 않기 때문에

# 문자열 변신
# 문자열 더하기
a = 'abc'
b = '123'
print(a+b) # 상식적으로 봐도 두 문자열이 이어 붙여진다고 생각하자

# 문자열 반복
print('#'*10)

'''
인덱싱(indexing) 에 관해서
'''
a = '0123456789'
# 인덱싱은 문자열에서 '특정 문자'를 획득하는 방식
# 시퀀스 타입에서 특정 데이터를 획득하는 방법
# 값을 획득하는 작업이다 보니 => 차원축소(2차원 -> 1차원) 의미를 가진다.
# 1을 출력하시오
# 사용하는 문법 : 변수명[인덱스]
# 인덱스는 순서(0부터 시작)가 존재함을 말함
print(a[1]) # 인덱스의 정방향
print(a[-9]) # 인덱스의 역방향도 가능 