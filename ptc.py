from itertools import product
K, M = map(int, input().split())
arr = []
for i in range(K):
    Arr = map(int, input().split()[1:])
    arr.append(map(lambda x:x**2%M, Arr))
print(max(map(lambda x: sum(x)%M, product(*arr))))