# 1 ~ N 원을 이루며 앉아 있음
# K 순서대로 K번째 사람을 제거
# i - 1 2 4 5 6 7 > 3 pop(arr[2]) 2 > (K - 1) +
# ii - 1 2 4 5 7  > 6 pop(arr[4])
# iii - 1 4 5 7   > 2 pop(arr[1])
# iiii - 1 4 5    > 7 pop(arr[3]) 

from collections import deque

N, K = map(int, input().split())
dq = deque([x for x in range(1, N + 1)])
res = []
print('<', end='')
while dq:
    for i in range(K - 1):
        dq.append(dq[0])
        dq.popleft()
    print(dq.popleft(), end='')
    if dq:
        print(', ', end='')
print('>')


