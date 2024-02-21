n = int(input())

cnt=1

for i in range(n):
    for j in range(n):
        if i <= j:
            if cnt < 9:
                print(cnt, end=' ')
                cnt += 1
            else:
                print(cnt, end=' ')
                cnt = 1
        else:
            print(' ', end=' ')
    print()