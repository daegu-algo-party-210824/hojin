# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

a, b = map(int, input().split())

zip = []

for i in range(0, a):
    monster = input()
    zip.append(monster)

question = []
for i in range(0, b):
    q = input()
    question.append(q)

for i in range(0, b):
    try:  # 값이 숫자일 때 
        if int(question[i]) + 0 >= 0:
            print(zip[int(question[i])-1])
    except:  # 문자열이면
        print(zip.index(question[i])+1)