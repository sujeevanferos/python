num = int(input("Enter any number: "))

while True:
    if num % 2 == 0:
        num /= num

    else:
        num = num*3 + 1


    print(num)