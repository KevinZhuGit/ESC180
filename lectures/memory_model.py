# id(n) finds the address of a variable
# aliasing??


# 1,2,3,4 all have an address. list will be given an address of @n pointing to @n0 which has [@1, @2, @3, @4]
list = [1, 2, 3, 4]

hardlist = list[:]  # hardlist gets address of @n1 = [@1, @2, @3, @4]
hardlist[0] = 0     # @n1 will change the first list of @1 to @0

print(list)
print(hardlist)


shallowlist = list  # shallowlist new address of @n2 which points to @n --> @n0
# goes to first thing in @n0 and changes the first index --> changes both list and shallow list
shallowlist[0] = 0
# creates a copy that points to the same address as list, changes will change original address as well

print(list)
print(shallowlist)


m = 5
print(m)


def f(x):
    x = 6  # does not change the global variable
    # returns None


m = f(m)
print(m)


def m(list):
    list[0] = 0
    print(list)


L = [[[1, 2, 3]]]
L1 = L[:]
print(L)
print(L1)

L1[0][0] = 5
print(L)
