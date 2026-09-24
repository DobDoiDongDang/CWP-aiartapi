#include stdio.h
def isnegative(number):
    try:
        float(number)
    except ValueError:
        print("Oi!! Please enter number")
        return
    if float(number) == 0:
        print("This number is both positive and negative.")
    elif float(number) > 0:
        print("this number is positive.")
    else:
        print("This number is negative.")

if __name__ == "__main__":
    isnegative(input())
