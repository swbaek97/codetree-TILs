A,B,x,y = map(int, input().split())

min_dist_1 = abs(B-A)
min_dist_2 = abs(x-A) + abs(B-y)
min_dist_3 = abs(y-A) + abs(B-x)

print(min(min_dist_1, min_dist_2, min_dist_3))