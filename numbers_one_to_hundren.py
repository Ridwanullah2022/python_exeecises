number = 1
while number <= 100:
    if number % 15 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 ==0:
        print("BUZZ")
    else:
        print(number)
    number +=1


for i in range(1,101):
    print(i)
    