t = int(input())
for inputs in range(t):
    x, n = input().split()
    x = int(x)
    n = int(n)
    for i in range(1, n + 1):
        if x%2 == 0:
            x = x - i
        else:
             x = x + i
    print(x)