import csv


with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",", quotechar='"')
    answer = list(reader)[1:]
    for id, name, title, clas, score in answer:
        if "Хадаров Владимир" in name:
            print("Ты получил:",score +", за проект -", title)
            break
    class_count = {}
    sum_class = {}
    for el in answer:
        class_count[el[-2]] = class_count.get(el[-2], 0) + 1
        sum_class[el[-1]] = sum_class.get(el[-1], 0) + (int(el[-1]) if el[-1] != 'None' else 0)
    for el in answer:
        if el[-1] != 'None':
            el[-1] = round(sum_class[el[-1]] / class_count[el[-2]], 3)
    file.close()


with open("students_new.csv", "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(['id','Name','titleProject_id','class','score'])
    writer.writerows(answer)
