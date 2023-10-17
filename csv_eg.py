import csv
from cs50 import get_string

# file = open("phonebook.csv", "a")  # a - append

# name = input("Name   : ")
# number = input("Number : ")

# writer = csv.writer(file)
# writer.writerow([name, number])

# file.close()


# below is a better way of doing it, then we do not need to file.close()
# with open("phonebook.csv", "a") as file:

#     name = input("Name   : ")
#     number = input("Number : ")

#     writer = csv.writer(file)
#     writer.writerow([name, number])


with open("phonebook.csv", "r") as fe:
    # reader = csv.reader(fe)
    # # next(reader) - this is used to ingore the first line, sometimes first line only have field names
    # for row in reader:
    #     num = row[1]

    reader = csv.DictReader(fe)
    for row in reader:
        num = row["Number"]
        print(num)
