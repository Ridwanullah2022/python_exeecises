number = int(input("Enter a number:"))
factor = 1
sum_of_factor = 0
while factor <= number // 2:
    if number % factor == 0:
         print(factor)
         sum_of_factor = sum_of_factor + factor


    factor += 1


if sum_of_factor < number:
     print(number, "is deficient")
elif sum_of_factor > number:
     print(number, "is abundant")
else:
     print(number, "is a perfect number")








