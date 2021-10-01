#   https://www.acmicpc.net/problem/11723
# 집합

# 런타임에러 3t / 메모리초과 2t / 답 검색
# 답 코드

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

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

# import sys

# S = set([])
# result = []
# m = int(input())

# for _ in range(0, m):
#     order = sys.stdin.readline()
#     if order == "all":
#         S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#     elif order == "empty":
#         S = set([])
#     else:
#         order, num = order.split()
#         num = int(num)

#     if order == "add":
#         S.add(num)
#     elif order == "remove":
#         try:
#             S.remove(num)
#         except:
#             pass
#     elif order == "check":
#         if num in S:
#             result.append(1)
#         else:
#             result.append(0)
#     elif order == "toggle":
#         if num in S:
#             S.remove(num)
#         else:
#             S.add(num)

# for i in result:
#     print(i)

