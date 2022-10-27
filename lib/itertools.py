import itertools

char = ['A', 'B', 'C']

print(list(itertools.permutations(char, 2))) # 두 번째 인자가 없으면, len(char)이 default
print(list(itertools.combinations(char, 2))) # 두 번째 인자가 없으면, 에러