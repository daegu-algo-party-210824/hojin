# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

# 시간초과 6t
# 답안지. 채점 통과.
# https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj7662/


import sys;read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        elif s[1]=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))
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

# 타임아웃코드
"""
import sys

t = int(sys.stdin.readline())

for i in range(0, t):
    k = int(sys.stdin.readline())

    queue = []

    for j in range(0, k):
        order, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        if order == "I":
            if len(queue) == 0 or num >= queue[-1]:
                queue.append(num)
            elif num <= queue[0]:
                queue.insert(0, num)
            else:
                queue.append(num)
                queue.sort()
        else:  # order == "D"
            if num == 1:  # 최대값 삭제
                if len(queue) == 0:
                    pass
                else:
                    # queue.remove(queue[-1])
                    queue.pop()
            else:  # 최소값 삭제
                if len(queue) == 0:
                    pass
                else:
                    # queue.remove(queue[0])
                    queue.pop(0)
                
        # queue.sort()
        # print(queue)
    if len(queue) == 0:
        print("EMPTY")
    else:
        print(queue[-1], queue[0])
"""