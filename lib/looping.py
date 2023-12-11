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
    
    pass
