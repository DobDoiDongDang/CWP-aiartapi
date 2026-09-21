#include stdio.h
def advance_mult(thisnumber, thatnumber):
    for i in range(0, thisnumber+1):
        if i != 0:
            print()
        print(f"Table de {i}: ", end="")
        for j in range(0, thatnumber+1):
            print(f"{i*j}", end=" ")
if __name__ == "__main__":
    advance_mult(10, 10)
