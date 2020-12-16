def list_from_file():
    with open("./input.txt", "r") as f:
        content = f.readlines()
    return [int(x) for x in content]

def is_2020(one, two):
    return one + two == 2020

def search_numbers(list_):
    first = list_.pop(0)
    if len(list_) == 0:
        print("list is empty")
        return
    
    for x in list_:
        if is_2020(first, x):
            return first * x
    return search_numbers(list_)

def day_one():
    numbers = list_from_file()
    number = search_numbers(numbers)
    print(number)

day_one()