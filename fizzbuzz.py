# print the numbers from 1 to 100
numbers = list(range(1, 101))
#If the number is dividable by 3 and 5 print FizzBuzz instead of the number.
for num in numbers: 
    if (num % 3!=0 and num % 5!=0):
        print(num)
    elif (num % 3==0 and num % 5==0):
        print("FizzBuzz")
# If the number is dividable by 3 print Fizz
    elif (num % 3==0 and num % 5!=0):
        print("Fizz")
#if the number is dividable by 5 print Buzz instead of the number
    elif (num % 5==0 and num % 3!=0):
        print("Buzz")