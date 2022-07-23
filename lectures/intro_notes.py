# can specify separator
print(1, 2, 3, sep="!")

# // = / for printing

# // division with neg? Has floor bottom, i.e. rounds down so -1.4 -> -2, also floor bottom for all //


def format():
    ''' 
    DOC STRING will show in help()

    '''
    return True


# protects from running if imported to a different file
if __name__ == '__main__':
    print(format())

# multiple assignment
a = 3
b = 4
a, b = b, a  # allows values to be swapped whereas doing linearly would not work

# or use temp variable temp = a, a = b, b = temp

# without temp var
b = a + b
a = b - a
b = b - a

# bool() True for everything but '' and 0 -----> if 'abc' = True
#   and, or, not operators      priorities not > and > or
#   for one conditions true and another false: if (a or b) and not (a and b)
#       or if a != b assuming a and b are written as ture/false statements

# find prime numbers


def prime(n):
    for i in range(2, n):  # can increase steps by two if you first check n % == 2
        if n % i == 0:
            return False
    return True

# (continue, break) - loops, (pass) - if else
