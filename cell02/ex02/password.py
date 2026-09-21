#include stdio.h

def password_check(word):
    password = "Python is awesome"
    if word == password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")

if __name__ == "__main__":
    password_check(input())
