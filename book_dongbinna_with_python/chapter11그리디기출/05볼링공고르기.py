n, m = map(int, input().split())  # n 공의 갯수, m 공의 최대무게.

list_ball = list(map(int, input().split()))

cases = []

for i in range(n):
    for j in range(i, n):
        if i == j:  # 서로 같은 번호의 공 고르면 패스.
            pass
        else:
            if list_ball[i] == list_ball[j]:  # 서로 같은 무게의 공 고르면 패스.  
                pass
            else:
                cases.append([list_ball[i],list_ball[j]])

count = len(cases)
print("cases: ", cases)
print(count)