# set_a.update(*other_sets)
# 집합 a와 다른 집합들의 합집합을 집합 a에 갱신한다.

a = {1,2,3,4}
b = {3,4,5,6}
c = {5,6,7,8}
a.update(b, c)
print(a)
# {1, 2, 3, 4, 5, 6, 7, 8}

# 다음과 같이 표현할 수도 있다.
a = {1,2,3,4}
b = {3,4,5,6}
c = {5,6,7,8}
a |= b
a |= c
print(a)
# {1, 2, 3, 4, 5, 6, 7, 8}