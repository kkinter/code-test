
L = int(input())
word = input()
res = 0
for s in range(L):
    res += (ord(word[s]) - 96) * (31 ** s)
print(res % 1234567891 )
