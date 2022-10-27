def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)
n, k = map(int, input().split())
# n! / (n - k)! * k!

print(fac(n) // (fac(n-k) * fac(k)))
