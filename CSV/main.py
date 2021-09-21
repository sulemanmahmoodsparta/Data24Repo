# Comma Seperated Values
import csv

with open("user_details.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # for row in csvreader:
    #     print(row[-1])

    csvreader = list(csvreader)[1:]
    print(csvreader)

