# https://www.acmicpc.net/problem/5430


# 50% 채점에서 시간초과. 보류.
import sys

t = int(sys.stdin.readline())
result = []

for i in range(t):
    ac = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()
    if n == 0:
        arr = []
    else:
        arr = str(arr[1:-1])
        arr = arr.split(",")
        arr = list(map(int, arr))
    
    for i in ac:
        if i == "R":
            arr.reverse()
        else:
            try:
                arr.pop(0)
            except:
                arr = "error"

for i in result:
    print(i)

"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""
