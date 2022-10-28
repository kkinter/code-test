
import sys
sys.stdin = open('./1620.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
poke_dic = {}
rev_dic = {}
for i in range(n):
    pokemon = input().strip()
    poke_dic[pokemon] = i + 1
    rev_dic[i + 1] = pokemon

for j in range(m):
    question = input().strip()
    try:
        print(rev_dic[int(question)])
    except:
        print(poke_dic[question])
