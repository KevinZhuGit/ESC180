import lab02


def sum_cubes(n):
    total = 0

    for i in range(1, n+1):
        total += i**3

    return total


def sum_cubes2(n):
    return ((n**2)*(n+1)**2)//4


def check_sum(n):
    if sum_cubes(n) == sum_cubes2(n):
        return True
    else:
        return False
    # return sum_cubes(n) == sum_cubes2(n)


def check_sum_up_to_n(n):
    counter = 0

    while counter <= n:
        if sum_cubes(n) != sum_cubes2(n):  # call check_sum(n)
            return False

        counter += 1

    return True


def leibniz(n):
    total = 0

    for i in range(0, n+1):
        total += ((-1)**i) / (2*i+1)

    return 4*total


if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    print(check_sum_up_to_n(6))

    print(leibniz(100000))
