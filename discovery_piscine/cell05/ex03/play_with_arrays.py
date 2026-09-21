#include stdio.h
yo = [2, 8, 9, 48, 9, 22, -12, 2]
whatup = []

for i in yo:
    if i > 5 and (i+2) not in whatup:
        whatup.append(i+2)

print(whatup)
