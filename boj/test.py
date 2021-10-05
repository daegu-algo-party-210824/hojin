# https://www.acmicpc.net/problem/1259

def validator(string):
    counter = True
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            counter = False
    return counter

result = []

while True:
    string = input()
    if string == "0":
        break

    if validator(string) is True:
        result.append("yes")
    else:
        result.append("no")

    
for i in result:
    print(i)


"""
121
1231
12421
0

결과
yes
no
yes
"""