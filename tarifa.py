X = int(input())
N = int(input())
ans = 0
for i in range(N):
    p = int(input())
    ans += X - p
print(ans + X)
