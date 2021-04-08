# dict.copy()
# dictionary의 얕은 복사본을 반환한다.
# = 을 사용해서 복사하면 dictionary의 내용이 바뀌게 되는 경우, 원본과 복사본 모두 바뀌게 된다.
# copy()를 사용해서 복사하면 원본의 내용을 건드려도, 복사본의 내용은 바뀌지 않는다.

a = {1:"one", 2:"two"}
b = a # 그냥 복제
c = a.copy() # copy로 복제
a.clear()
print(b)
# {}
print(c)
# {1: 'one', 2: 'two'}