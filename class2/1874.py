n = int(input())
stk = [ x for x in range(1, n + 1)]
kts = []
ans = []
for i in range(n):
    num = int(input())
    for j in range(n):
        ele = stk.pop(j)
        kts.append(ele)
        if len(kts) >= 1:
            if kts[-1] != num:
                print('+')
            else:
                ans.append(kts.pop())
                print('-')
    print(stk)
    print(kts)
    print(ans)
    
             
        
