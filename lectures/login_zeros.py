# compute a = n!
# see how many trailing zeros

def trailing_zeros(n):
    '''
    paranm:
    can also break into to def, fact(n) and zeros()
    '''
    a = 1
    zeros = 0

    for i in range(1, n+1):  # lower range included, upper is excluded, for n=0 => range(1,1) which does not print, leaving a = 1
        a *= i

    while a % 10 == 0:
        a = a // 10
        zeros += 1

    return zeros


def login(username, password):
    global attempts

    # list of logins and matching passwords
    if username == "guy" and password == "123":
        return "OK"

    attempts += 1
    return "Refused"


if __name__ == "__main__":

    attempts = 0
    while attempts <= 3:
        username = input("Username: ")
        password = input("Password: ")
        login(username, password)
