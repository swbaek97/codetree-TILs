m1, e1 = map(int, input().split())
m2, e2 = map(int, input().split())

if m1 > m2 or (m1 == m2 and e1 > e2):
    print('A')
else:
    print('B')