n = int(input())  # n개의 동전. 

coin = list(map(int, input().split()))

money = coin  # 만들 수 있는 금액 리스트, 동전 하나로 만들 수 있는 금액을 먼저 복사해놓고.

for i in range(n):  
    sum = coin[i]  # 
    for j in range(n):
        if i == j:  # 가지고있는 동전으로 만들 수 있는 금액을 찾고있으므로 자기자신과 더할 수 없다.
            pass
        else:
            sum += coin[j]
            money.append(sum)

money = set(money)  # set으로 중복값 제거.

print("만들 수 있는 금액: ",money)

min_money = 1  # 0원은 없으니까. 1원부터시작.

for i in range(1, max(money)):  # 1부터 시작. 만들수있는금액 중 최대 금액 까지.
    if i not in money:  # money 안에 없는 i 값이 걸리면 그것이 만들수없는 금액.
        min_money = i  # 1부터 시작했으니 걸리면 그것이 최소값.
        break
    
print(min_money)

# end

