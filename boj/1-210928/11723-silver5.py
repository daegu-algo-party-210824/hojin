# 집합  https://www.acmicpc.net/problem/11723

import sys

S = set([])
result = []
m = int(input())

for _ in range(0, m):
    order = input()
    if order == "all":
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif order == "empty":
        S = set([])
    else:
        order, num = order.split()
        num = int(num)

    if order == "add":
        S.add(num)
    elif order == "remove":
        S.remove(num)
    elif order == "check":
        if num in S:
            result.append(1)
        else:
            result.append(0)
    elif order == "toggle":
        if num in S:
            S.remove(num)
        else:
            S.add(num)

for i in result:
    print(i)

"""
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
"""