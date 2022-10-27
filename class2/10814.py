# 나이는 1 <= age <= 200
# 길이 length <= 100
# 입력 가입순

N = int(input())
users = []
for idx in range(N):
    age, name = input().split()
    users.append((int(age), idx, name))

arr = sorted(users, key = lambda x : (x[0] , x[1]))
for i in arr:
    print(i[0], i[2])