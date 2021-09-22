# Comma Seperated Values
import csv


def transform_user_details(csv_file_name):
    new_user_data = []
    with open("user_details.csv") as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data


def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name="new_user_data.csv"):
    new_user_data = transform_user_details(old_user_data_file)

    with open(new_file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_user_data_csv()


# with open("user_details.csv") as file:
#     csvreader = csv.reader(file)
#
#     for row in csvreader:
#         print(row)


# with open("user_details.csv") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#
#     # for row in csvreader:
#     #     print(row[-1])
#
#     csvreader = list(csvreader)[1:]
#     print(csvreader)
