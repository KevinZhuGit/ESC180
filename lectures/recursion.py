def print_list(L):
    '''
    print list without for loop
    - keeps cutting off list
    '''
    # Recursion check to stop (when list is empty)
    if len(L) == 0:
        return

    # print first element
    print(L[0])
    # return spliced list without first element
    print_list(L[1:])


def reverse_print_list(L):
    if len(L) == 0:
        return

    print(L[len(L)])
    reverse_print_list(L[:len(L)-1])

    # OR
    # cuts list first
    reverse_print_list(L[1:])
    print(L[0])


print_list([1, 2, 3, 4, 5, 6])

# sorting algorithms and their runtime complexity
# learn merge sort: recursion: break up lists in half, sort smaller lists and then larger


def sort(l1, l2):  # Doesnt account for finishing first
    i = 0
    j = 0
    sorted = []

    while i < len(l1) and j < len(l2):
        if l1[i] > l2[j]:
            sorted.append(l1[i])
            i += 1
        else:
            sorted.append(l2[j])
            j += 1

    return sorted


sort([9, 8, 7, 7], [2, 9, 8])

# caching


def fib(n):
    # has a lot of repeating calcuations
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_cach(n, cache={}):  # cache is a dictionary, can assign in parameter??
    '''
    adds things to dicitionary and checks if there first
    since only goes through f(1), f(2)...f(n) once, complexity = O(n)
    '''
    if n == 2:
        return 1
    if n-1 in cache:
        fibn1 = cache[n-1]
    else:
        fibn1 = fib(n-1, cache)
        cache[n-1] = fibn1
    if n-2 in cache:
        fibn2 = cache[n-2]
    else:
        fibn2 = fib(n-2, cache)
        cache[n-2] = fibn2

    cache[n] = fibn1 + fibn2


def print_all(alphabet, n, start_str=''):
    '''
    prints out all combinations of alphabet with len n
    with predetermined start str

    uses start_str to do it recursively by setting new start_strs

    complexity = len(alphabet)^n -> 1 + m + m^2 + ... m^n
    gemoemtric series, use the formula and divide -> O(m^n+1)
    '''

    if n == 0:
        print(start_str)
        return

    for letter in alphabet:
        print_all(alphabet, n-1, start_str + letter)

    '''
    for returning lists

    if n == 0:
        return(start_str)
    
    res = []
    for letter in alphabet:
        res.extend(print_all(alphabet, n-1, start_str + letter)
    resturn res
    '''

    # can use nested for loops, however, needs predetermined length
    # for letter1 in alphabet:    for letter 2 in alphabet: ... for letter n in alphabet:
