# .insert(index, elem)
#       inserts elem into index position

# .index(elem)
#       finds index of first elem in list, or returns error if none
#       can check by using elem in L, returns True if elem is in list L, or False if not
#           also elem not in L

# L[x:y:z], starts at index x, moves by increments of z up to y  ==> basically range(x,y,z)
#       L[::2], goes by increments of 2

# can delete index with del L[i]
#       if looping through, can have indexing error since size of list changes
#       for i in range(5) but now only up to 4
#       can use while loop, but check for skipping and fix index count
#       ****splicing is better*****
