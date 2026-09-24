import sys
def downcase_it(string):
    return string.lower()
if __name__ == "__main__":
    dalist = sys.argv
    dalist.pop(0)
    for i in dalist:
        print(downcase_it(i))
