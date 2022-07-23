a = sorted('cba')  # returns list of strings
b = 'replaces spaces using replace'.replace(' ', '')

# create empty list/string of lengh n
# temp = ' '*n, temp = ['']*n

#TUPLES, immutable
ex = (1, 2, [3, 4], 5)

a, b, c, d = ex
# unpacks and assigns a,b,c,d to tuple, needs to have same length
# like x, y = y, x


# DICTIONARIES
#       key and value pair to the key
#       key must be unique, value whatever, acts as indices/tags

grades = {"phy": 90, "mat": 80}

# appends to dictionary, ****** key cannot be mutable, ie a list******
grades["civ"] = 95

grades.keys()  # tuple with list of keys
grades.values()  # tuples with list of values
grades.items()  # tuple with list of key and value pairs

# iterating through dictionary
#       for x, y in dictionary.items():   x, y will be key and values
# or for x in dictionary(): - loops through keys, can check values through dictionary[x]

# checking and adding to value for a key
#       grades[key].append(value) -----> only works if value already a list

# can delete pair with   del dictionary[key]
