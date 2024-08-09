#!/usr/bin/python3 

number1 = int(input("Enter a number less than 25 \n"))

if number1 <= 25:
    while number1 <= 25:
        print(f"Inside the loop, my variable is {number1}")
        number1 = number1 + 1

else:
    print("Error")
