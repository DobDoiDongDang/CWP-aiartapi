import sys
da_list = sys.argv
da_list.pop(0)
new_list = []
for i in da_list:
    if i[-4:-1] != "ism":
        new_list.append(i+"ism")
print("\n".join(new_list))
