import math


def count_evens(L):  # counts numbers
    sum = 0

    for i in range(len(L)):
        if i % 2 == 0:
            sum += 1

    return sum


def list_to_string(list):
    template = ''  # add brackets after creating for edge case with slicing

    for i in range(len(list)):
        template += f'{list[i]}, '

    list_string = f"[{template[:-2]}]"

    return list_string


def lists_are_the_same(list1, list2):
    # check lengths
    if len(list1) == len(list2):
        for a, b in zip(list1, list2):
            if a != b:
                return False
    else:
        pass

    return True


def simplify_fractions(n, m):
    for i in range(n, 0, -1):  # n, 0 --> exclusive

        if (n % i == 0) and (m % i == 0):

            print(f"{n // i}/{m // i}")

            break


def sigdigs_leibniz(n):
    terms = 0
    total = 0

    while int((4*total)*(10**n)) != int(math.pi*(10**n)):
        total += ((-1)**terms) / (2*terms + 1)

        terms += 1

    return terms - 1


def euclids(a, b):
    num1 = a
    num2 = b

    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    print(f"{a//num2}/{b//num2}")


simplify_fractions(10, 7)
simplify_fractions(2322, 654)
euclids(2322, 654)
