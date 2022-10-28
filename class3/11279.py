import heapq
import sys
sys.stdin = open('./11279.txt')
input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
