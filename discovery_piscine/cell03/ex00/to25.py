#include stdio.h
'''Damn i accidently remove my cell03 folder and now im doing it again ;-;'''
def from_this_to_that(thisnumber, thatnumber):
    while thisnumber != thatnumber:
        print(f"Inside the loop, my variable is {thisnumber}")
        if thisnumber < thatnumber:
            thisnumber += 1
        else:
            thisnumber -= 1

if __name__ == "__main__":
    number = int(input("Enter a number less than 25\n"))
    if number >= 25:
        print("Error")
    else:
        from_this_to_that(number, 26)
