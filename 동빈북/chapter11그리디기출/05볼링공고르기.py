n, m = map(int, input().split()) 

list_ball = list(map(int, input().split()))

cases = []

for i in range(n):
    for j in range(i, n):
        if i == j:
            pass
        else:
            if list_ball[i] == list_ball[j]:
                pass
            else:
                cases.append([list_ball[i],list_ball[j]])

count = len(cases)
print("cases: ", cases)
print(count)