s = input()

res = 0
for i in range(len(s)):
    if i == '0' or i == '1':
        res += int(s[i])
    else:
        if res == 0:
            res += int(s[i])
        else:
            res *= int(s[i])
print(res)
        