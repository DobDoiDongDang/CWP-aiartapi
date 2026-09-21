#include stdio.h
def iszero(number):
    try:
        number = int(number)
    except ValueError:
        print("Oi!! Please enter integer")
        return
    if number == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
if __name__ == "__main__":
    iszero(input())
