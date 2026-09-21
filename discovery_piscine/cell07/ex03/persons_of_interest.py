def sorting(key, item):
    sort = []
    while len(item) > 0:
        most = 0
        index = 0
        for i in item:
            if int(i) > most:
                most = int(i)
                index = item.index(i)
        sort.append(key.pop(index))
        item.pop(index)
    return sort

def famous_births(dic):
    key = []
    item = []
    for i in dic:
        key.append(i)
        item.append(dic[i]["date_of_birth"])
    return sorting(key, item)

if __name__ == "__main__":
    women_scientists = {
            "ada": { "name": "Ada Lovelace", "date_of_birth": "1815"}, 
            "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" }, 
            "lise": {"name": "Lise Meitner", "date_of_birth": "1878"}, 
            "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}}
    for i in famous_births(women_scientists)[::-1]:
        print(f"{women_scientists[i]["name"]} is a great scientist born in {women_scientists[i]["date_of_birth"]}.")
