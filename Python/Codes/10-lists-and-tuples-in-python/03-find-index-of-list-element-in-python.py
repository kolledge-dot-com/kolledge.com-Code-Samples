# Index of a list element
def find_index(item):
    if item in my_list:
        index = my_list.index(item)
        print(f"Item {item} is at index {index}")
    else:
        print(f"Item {item} is not in my_list")


my_list = [1, 2, 3, 4]
find_index(3)
find_index(5)
