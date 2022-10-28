import sys
sys.stdin = open('./11399.txt')
# 값이 작은 사람이 먼저 서야함
n = int(input())
arr = list(map(int, input().split()))
rev = sorted(arr)
sum_val = 0
for i in range(n):
    sum_val += sum(rev[:(i+1)])
print(sum_val)