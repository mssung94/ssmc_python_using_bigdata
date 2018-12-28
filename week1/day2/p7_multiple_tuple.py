'''
2. 여러개의 데이터 ( 연속 데이터, 시퀀스 데이터 )
     - 튜플 : ()
        - 순서가 없다
        - 인덱스가 존재
        - 값의 중복 ok
        - 값을 묶는다에 의미를 두고 쓴다
        - 값 변경불가
'''

# 리스트와 별반 다를바 없지만 유일한 차이는 값을 묶는다에 차이가 있다

tu = () # 소괄호 안에 아무것도 안쓰면 소괄호랑 헷갈릴 수 있음
print(tu,type(tu),len(tu))
tu = tuple()
print(tu,type(tu),len(tu))

####################################################################################

# 값을 여러개 묶는다!!
tu = (1) # 이렇게 된다면 tuple일까? 정수일까?
print(tu,type(tu)) # int를 출력해버림

#값이 한개일때는 항상 그래서 콤마(,)를 넣어주자!!!
tu = (1,)
print(tu,type(tu))

####################################################################################

# 값의 변경이 불가, 삭제 불가 => immutable
tu = (1,2,3,4)
print(tu[0])
print(tu[:2])
# 함수 내부에서 여러개의 값을 리턴할때 주로 많이 사용
a,b,c,d = tu # 이렇게 되면 tuple에 있는 구성원이 순서대로 하나씩 대입됨
# 이렇게 안하면 a = tu[0], b = tu[1], ... 이런식으로 해야하는 최악의 경우가 있었을수도
print(d) # 4 출력