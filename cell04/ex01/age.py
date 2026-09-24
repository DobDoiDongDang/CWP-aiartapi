#include stdio.h
def whatmyage(age):
    for i in range(10, 31, 10):
        print(f"In {i} years, you'll be {age+i} years old.")

if __name__ == "__main__":
    whatmyage(int(input("Please tell me your age: ")))
