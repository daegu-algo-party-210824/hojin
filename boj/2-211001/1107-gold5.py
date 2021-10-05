# https://www.acmicpc.net/problem/1107

# 19:43
# 23:07
# 23:40

# 런타임에러 왜 나는지 모르겠음

n = input()  # 가고싶은 채널 string
m = int(input())  # 고장난 버튼 갯수

# btns = [ i for i in range(10)]
# btn_alive = [True for i in range(10)]
btn_alive = [True,True,True,True,True,True,True,True,True,True]
now_channel = 100

btn = input().split(' ')  # 고장난 버튼 입력

for i in btn:  # 버튼 죽이기
    # print(i)
    if i == '':
        break
    btn_alive[int(i)] = False

def has_broken_num(n):  # 고장난 숫자를 포함하면 true 반환. 아니면 false
    if n < 0:
        return True

    n = str(n)
    for i in n:
        if btn_alive[int(i)] is False:  
            return True
    return False

def find_up_down(n):  # 버튼으로 누를 수 있는 n과 가장 가까운 수를 찾아 반환.
    n = int(n)
    if has_broken_num(n) is True:
        for i in range(500000):
            if has_broken_num(n - i) is False:
                if n - i < 0:
                    pass
                else:
                    return n - i
            elif has_broken_num(n + i) is False:
                    return n + i
    else:
        return n  # int

x = find_up_down(n)  # int 가장 가까운 수
click = abs(int(n) - x)
result = abs(int(n) - 100)  # int 방향키로만 누룰 때
result = min(result, len(str(x)) + click)

print(result)

"""
5457
3
6 7 8

->6
----------------------
100
5
0 1 2 3 4

->0
----------------------
500000
8
0 2 3 4 6 7 8 9

->11117
"""