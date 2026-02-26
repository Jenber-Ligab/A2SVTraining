t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    for i in range(1,n):
        if arr[i] - arr[i-1] <= 1:
            count += 1
    if count == n-1:
        print("YES")
    else:
        print("NO")