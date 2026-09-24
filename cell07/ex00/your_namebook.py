def array_of_names(dic):
    namelist = []
    for i in dic:
        namelist.append(i[0].upper()+i[1:]+" "+dic[i][0].upper()+dic[i][1:])
    return namelist

if __name__ == "__main__":
    person = {
            "jean": "valjean", 
            "grace": "hopper", 
            "ivier": "niel", 
            "fifi": "brindacier"}
    print(array_of_names(person))
