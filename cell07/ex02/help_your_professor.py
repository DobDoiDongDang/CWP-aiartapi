def average(dic):
    sum_score = 0
    sum_student = 0
    for i in dic.keys():
        sum_score += dic[i]
        sum_student += 1
    return sum_score/sum_student

if __name__ == "__main__":
    class_3B = {
            "marine": 18,
            "jean": 15, 
            "coline": 8,
            "luc": 9}
    class_3C = {
            "quentin": 17,
            "julie": 15, 
            "marc": 8, 
            "stephanie": 13}
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
