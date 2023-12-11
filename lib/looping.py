#!/usr/bin/env python3

def happy_new_year():
    countdown = 10

    while countdown >= 1:
        print (countdown)
        countdown -= 1
    print("Happy New Year!")
    
def square_integers(numbers):
   
    squared_list = [num ** 2 for num in numbers]
    

    return squared_list

result = square_integers([1, 2, 3, 4, 5])
print(result)



def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


fizzbuzz()



