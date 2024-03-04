import math
import random

def upr_4():
    a = [5]
    b = [5]
    cnt_a = 0
    cnt_b = 0
    positive_num = []
    for i in range(1, 6):
        num = random.randrange(-10, 10)
        a.append(num)
        if num>0:
            cnt_a+=1
            positive_num.append(num)
    for j in range(1, 6):
        num = random.randrange(-10, 10)
        b.append(num)
        if num>0:
            cnt_b+=1
            positive_num.append(num)

    if cnt_a>cnt_b:
        print("Больше в списке А")
    else:
        print("Больше в списке B")

    print(positive_num)
print("Упражнение 4")
upr_4()

def upr_14():
    array = [13, 4, -2, 6, 7, -1, -5, 2, -3, 4]
    negative = []
    positive = []
    for i in range(len(array)+1):
        if array[i]<0:
            negative.append(array[i])
        else:
            positive.append(array[i])
    positive.reverse()
    k = 1
    for i in range(7):
        k += negative[1]*positive[1]
    print(k)

print("Упражнение 14")
upr_14()