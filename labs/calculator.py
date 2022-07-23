import math


def display_current_value():
    print(f"Currnet value: {cur_value}")


def add(to_add):
    global cur_value
    global prev_value

    prev_value = cur_value
    cur_value = cur_value + to_add


def subtract(to_subtract):
    global cur_value
    global prev_value

    prev_value = cur_value
    cur_value = cur_value - to_subtract


def multiply(to_multiply):
    global cur_value
    global prev_value

    prev_value = cur_value
    cur_value = cur_value*to_multiply


def division(to_division):
    global cur_value
    global prev_value

    if to_division != 0:
        prev_value = cur_value
        cur_value = cur_value/to_division
    else:
        print("Division by 0")


def memory():
    global store
    store = cur_value


def recall():
    global cur_value
    global store

    cur_value = store


def undo():
    global cur_value
    global prev_value

    temp = cur_value
    cur_value = prev_value
    prev_value = temp


if __name__ == "__main__":
    cur_value = 0
    prev_value = 0
    store = 0

    print(f"Welcome to the calculator program.\nCurrent value: {cur_value}")

    cur_value = 42
    division(math.pi)
    display_current_value()
    division(0)
    display_current_value()
    division(1285397314561234)
    display_current_value()
    multiply(1285397314561234)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
