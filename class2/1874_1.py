import sys
sys.stdin = open('./1874.txt')

n = int(input())
stk = []
ans = []
flag = False
cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:
        stk.append(cur)
        ans.append('+')
        cur += 1
    if stk[-1] == num:
        stk.pop()
        ans.append('-')
    else:
        print('NO')
        flag = True
        break
if not flag:
    for i in ans:
        print(i)
    