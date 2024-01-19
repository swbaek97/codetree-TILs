t, w = map(int, input().split())

bmi = (100*100*w) // (t*t)

print(bmi)
if bmi >= 25:
    print('Obesity')