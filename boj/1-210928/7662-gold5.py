# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

# 시간초과 
import sys

t = int(sys.stdin.readline())

for i in range(0, t):
    k = int(sys.stdin.readline())

    queue = []

    for j in range(0, k):
        order, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        if order == "I":
            queue.append(num)
        else:  # order == "D"
            if num == 1:  # 최대값 삭제
                try:
                    queue.remove(queue[-1])
                except:
                    pass
            else:  # 최소값 삭제
                try:
                    queue.remove(queue[0])
                except:
                    pass
        queue.sort()
        # print(queue)
    if len(queue) == 0:
        print("EMPTY")
    else:
        print(queue[-1], queue[0])

"""
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""