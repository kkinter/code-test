import sys
# sys.stdin = open('./1181.txt')
N = int(input())
word_dict = {}
for i in range(N):
    word = input()
    word_dict[word] = len(word)

ans = sorted(word_dict, key = lambda x: (word_dict[x], x))
for v in ans:
    print(v)
