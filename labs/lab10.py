# Problem 1

def power(x, n):
    # case if called with zero
    if n == 1:
        return x

    return x*power(x, n-1)


print(power(2, 8))

# Problem 2


def interweave(l1, l2):
    # use zeros!
    if len(l1) == 1:
        return [l1[0], l2[0]]

    template = [l1[0], l2[0]]

    # template + ...
    template.extend(interweave(l1[1:], l2[1:]))
    return template


a = [1, 3, 5]
b = [2, 4, 6]
print(interweave(a, b))

# Problem 3


def reverse_rec(L, i=-1):
    # do it backwards by passing list?

    if len(L) == 1:
        return [L[0]]

    template = [L[i]]

    return template + reverse_rec(L, i-1)


print(reverse_rec([1, 2, 3, 4, 5]))


# Problem 4
def outwards(L):
    if len(L) % 2 != 0:
        print(L[len(L)//2], '', end='')
        L.pop(len(L)//2)  # editing list, be careful
        outwards(L)
    elif len(L) == 0:
        print('')
    else:
        n = len(L)
        print(L[n//2 - 1], L[n//2], '', end='')
        outwards(L[:n//2 - 1] + L[n//2 + 1:])


outwards([1, 2, 3, 4, 5])


def zigzag1(L):
    if len(L) == 0:
        print('')  # does not stop until end met
    elif len(L) == 1:
        print(L[0], end="")
    else:
        print(L[0], L[-1], end="")  # swap 73 and 74
        zigzag1(L[1:-1])


# Problem 5


def is_balanced(s):
    first_open = s.find('(')
    last_open = s.rfind('(')
    first_closed = s.find(')')
    last_closed = s.rfind(')')

    if first_open == -1 and first_closed == -1:
        return True
    elif first_closed < last_open and first_open < first_closed and last_open < last_closed:
        return is_balanced(s[first_closed + 1: last_open])
    elif first_closed < first_open and last_closed < last_open:
        return False

    return is_balanced(s[first_open + 1: last_closed])


test = '(well (I think), recursion works like that (as far as I know))'
print(is_balanced(test))
