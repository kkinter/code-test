import sys
import heapq
heap = []
sys.stdin = open('./1927.txt')
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    x = int(input())
    if x >= 1:
        heapq.heappush(heap, x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))

