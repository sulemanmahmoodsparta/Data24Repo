def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + "\n")

    except FileNotFoundError:
        print(f"The file {file} does not exist!")


write_to_file("writing_orders.txt", "banana")
