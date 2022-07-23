# sum(list) returns sum of entire list
# max(list) returns max num or max(a,b) and returns greatest of a and b
# sorted(list/string) returns sorted list
# set(list) returns set of unique elems

# list.index(elem) returns first index of element
# list.count(elem) returns count of elem, useful for anagrams
# list.pop(elem) pops elem and returns index
# list.remove(elem) removes elem

# if x in list checks if elem in list

# negative list indexing starts at -1

# break breaks through current loop, not all

# % acts as modulous, can be used to wrap around lists
5 % 4  # 1
4 % 5  # 0
4 % 2  # 0

print('a', 'b')  # will auto space between
print('a' + 'b')  # no space


def f():
    print('hi')


a = f()  # f() returns None

# lists in lists are shallow copied when using :
