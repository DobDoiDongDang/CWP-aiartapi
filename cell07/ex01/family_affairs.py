def find_the_redheads(dic):
    redhairs = []
    for i in dic.keys():
        if dic[i] == "red":
            redhairs.append(i)
    return redhairs

if __name__ == "__main__":
    dupont_family = {
            "florian": "red", 
            "marie": "blond",
            "virginie": "brunette", 
            "david": "red", 
            "franck": "red"}
    print(find_the_redheads(dupont_family))
