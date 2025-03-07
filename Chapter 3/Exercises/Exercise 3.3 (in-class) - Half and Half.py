"""
Exercise 3.3 - Half and Half

Write a program that asks the user for an integer number 1 or greater.

Once the use enters a valid number, the program should continuously divide the number by 2 until the answer is less than 0.5.

The output should display the value of the result after each division

and the total number of division needed for the number to be less than 0.5.

    :Author: <NAME>
    :Date: <TODAY'S DATE>
"""
integer = abs(int(input("Pretty Please Enter a number bigger then 1: ")))
count = 0

while integer > 0.5:
    integer /=2
    print(f'-{integer}')
    count +=1

print(f'It took {count} tries for your number to be less then 0.5')
