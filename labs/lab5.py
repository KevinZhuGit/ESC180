def list1_starts_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False

        return True
    return False


def match_pattern(list1, list2):
    # iterates through slices

    for i in range(len(list1) - len(list2)):
        if list1[i: i+len(list2)] == list2:
            return True

    return False


def repeats(list0):  # only need 2, not left and right
    for i in range(1, len(list0) - 1):
        if list0[i-1] == list0[i] and list0[i] == list0[i+1]:
            return True

    return False


def print_matrix_dim(M):
    print(f"{len(M)}x{len(M[0])}")


def mult_M_v(M, v):
    vector = [0]*len(M)

    for m in range(len(M)):
        sum = 0

        for n in range(len(v)):
            sum += M[m][n] * v[n]

        vector[m] = sum

    return vector


def mult_M(A, B):       # mxn and nxj
    vector_m = [0]*len(A)

    for m in range(len(A)):
        vector_n = [0]*len(B[0])

        for j in range(len(B[0])):
            sum = 0

            for n in range(len(B)):
                sum += A[m][n] * B[n][j]

            vector_n[j] = sum

        vector_m[m] = vector_n

    return vector_m


i = [[1, 4], [2, 3], [4, 4], [7, 1]]  # 4x2
j = [[5, 3, 1], [2, 2, 7]]  # 2x3

print(mult_M(i, j))
