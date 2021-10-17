
n = int(input())

# def fibo(i):

#     if i == 1:
#         return 1

#     result = i * fibo(i - 1)

#     return result

# result = str(fibo(n))

counter = 0

# for i in range(len(result)):
#     if result[-1 * (i + 1)] == "0":
#         counter += 1
#     else:
#         break

while n >= 5:
    counter += n//5

    n //= 5

print(counter)