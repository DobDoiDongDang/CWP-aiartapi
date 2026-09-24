#include stdio.h
def highlow(word):
    anotherword = ""
    for i in word:
        if i.islower():
            anotherword += i.upper()
        else:
            anotherword += i.lower()
    return anotherword

if __name__ == "__main__":
    print(highlow(input()))
