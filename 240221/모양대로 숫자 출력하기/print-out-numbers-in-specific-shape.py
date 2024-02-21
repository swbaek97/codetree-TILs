n = int(input())

for i in range(n):
    for j in range(n,0,-1):
        if j <= n-i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()