num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0

for i in range(0,10):
    result = sum + i
    print("previous_number ", str(sum)  + " Current_number ", str(i) + " sum : ", str(result))

    sum = i
    Current_number = i + 1
