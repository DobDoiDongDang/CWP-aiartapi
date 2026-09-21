#include stdio.h

def isnegative(number):
    try:
        number = float(number)
    except ValueError:
        print("Oi!! Please enter number")
        return
    if float(number) == 0:
        print("This number is both positive and negative.")
    elif float(number) > 0:
        print("this number is positive.")
    else:
        print("This number is negative.")

def multiply_cal(first_number, last_number):
    try:
        first_number = int(first_number)
        last_number = int(last_number)
    except ValueError:
        print("Oi!! Please enter integer")
        return
    return first_number * last_number

if __name__ == "__main__":
    first_number = input("Enter the first number:\n")
    last_number = input("Enter the second number:\n")
    result = multiply_cal(first_number, last_number)
    print(f"{first_number} x {last_number} = {result}")
    isnegative(result)
