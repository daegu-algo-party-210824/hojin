string1 = input()

new_string = string1[0]

for i in range(len(string1) - 1):

    if string1[i] != string1[i + 1]:
        new_string += string1[i + 1]

# print(new_string)

result = 0

if new_string.count("0") > new_string.count("1"):
    result = new_string.count("1")
else:
    result = new_string.count("0")

print(result)

# end 백준 체점 맞음.