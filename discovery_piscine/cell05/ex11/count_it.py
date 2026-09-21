import sys
print("parameters:", len(sys.argv))
for i in sys.argv:
    print(i+": "+str(len(i)))
