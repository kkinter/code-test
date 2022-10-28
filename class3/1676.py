n = int(input())
def fac(n):
    if n < 1:
        return 1
    else:
        return fac(n - 1) * n
res = str(fac(n))
cnt = 0
for i in res[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)
