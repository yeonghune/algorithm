import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
jewel_lst = [tuple(map(int, input().split())) for _ in range(N)]
bag_lst = [int(input()) for _ in range(K)]

jewel_lst.sort(key=lambda x: x[0])
bag_lst.sort()

two_pointer = 0
pq = []
result = 0

for weight in bag_lst:
    while two_pointer < len(jewel_lst) and jewel_lst[two_pointer][0] <= weight:
        heapq.heappush(pq, -jewel_lst[two_pointer][1])
        two_pointer += 1

    if pq:
        result -= heapq.heappop(pq)

print(result)
