import csv
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)