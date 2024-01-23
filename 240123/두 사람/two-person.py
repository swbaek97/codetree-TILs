age_1, s_1 = input().split()
age_2, s_2 = input().split()
age_1, age_2 = int(age_1), int(age_2)

if (s_1 == 'M' and age_1 >= 19) or (s_2 =='M' and age_2 >=19):
    print(1)
else:
    print(0)