n = int(input().strip())
for i in range(n):
    a, b, c = map(int, input().strip().split())
    if a + b == c:
        print("YES")
    elif a + c == b:
        print("YES")
    elif b + c == a:
        print("YES")
    else:
        print("NO")