import sys
input = sys.stdin.readline
# def fibo(n):
#     global one, zero
#     if n == 0:
#         one += 1
#         return 0
#     elif n == 1:
#         zero += 1
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

t = int(input())
for i in range(t):
    zero = [1, 0, 1]
    one = [0, 1, 1] 
    n = int(input())
    if n >= 3:
        for j in range(3, n + 1):
            zero.append(zero[j - 1] + zero[j - 2])
            one.append(one[j - 1] + one[j - 2])

 
    print(zero[n], one[n])