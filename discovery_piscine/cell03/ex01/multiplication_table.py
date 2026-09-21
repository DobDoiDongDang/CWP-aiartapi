#include stdio.h
def multiplication_table(number):
    for i in range(0, 10):
        print(f"{i} x {number} = {i * number}")
if __name__ == "__main__":
    multiplication_table(int(input("Enter a number\n")))
