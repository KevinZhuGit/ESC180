import numpy as np

# P1


def print_matrix(M_lol):
    # .array() creates ndarray object in numpy
    M = np.array(M_lol)
    print(M)


# P2

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i

    return len(row)


# P3

def get_row_swap(M, start_i):
    left_most_index = get_lead_ind(M[start_i])
    index = start_i

    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < left_most_index:
            left_most_index = get_lead_ind(M[i])
            index = i

    return index

# P4


def add_rows_coefs(r1, r2, c1, c2):
    sum = [0]*len(r1)

    for i in range(len(r1)):
        sum[i] = r1[i]*c1 + r2[i]*c2

    return sum


# P5

def elminate(M, row_to_sub, best_lead_ind):

    for i in range(row_to_sub + 1, len(M)):
        lcm = np.lcm(M[row_to_sub][best_lead_ind], M[i][best_lead_ind])

        if lcm != 0:
            if M[row_to_sub][best_lead_ind] * M[i][best_lead_ind] > 0:
                M[i] = add_rows_coefs(
                    M[row_to_sub], M[i], -lcm//M[row_to_sub][best_lead_ind], lcm//M[i][best_lead_ind])
            else:
                M[i] = add_rows_coefs(
                    M[row_to_sub], M[i], lcm//M[row_to_sub][best_lead_ind], -lcm//M[i][best_lead_ind])


# P6


def forward_step(M):
    for i in range(len(M)-1):
        swap = get_row_swap(M, i)
        M.insert(i, M[swap])
        M.pop(swap + 1)

        elminate(M, i, get_lead_ind(M[i]))


# P7

def backward_step(M):
    for i in range(len(M)-1, 0, -1):
        backwards_elminate(M, i, get_lead_ind(M[i]))


def backwards_elminate(M, row_to_sub, lead_index):
    for i in range(0, row_to_sub):
        lcm = np.lcm(M[row_to_sub][lead_index], M[i][lead_index])

        if lcm != 0:
            if M[row_to_sub][lead_index] * M[i][lead_index] > 0:
                M[i] = add_rows_coefs(
                    M[row_to_sub], M[i], -lcm//M[row_to_sub][lead_index], lcm//M[i][lead_index])
            else:
                M[i] = add_rows_coefs(
                    M[row_to_sub], M[i], lcm//M[row_to_sub][lead_index], -lcm//M[i][lead_index])


# P8

def gaussian_elimination(M, b):

    for i in range(len(b)):
        M[i].append(b[i])

    forward_step(M)
    backward_step(M)

    for i in range(len(M)):
        mult = M[i][get_lead_ind(M[i])]

        for j in range(len(M[i])):
            M[i][j] = M[i][j] / mult

    return M


A = [[1, -2, 3],
     [3, 10, 1],
     [1, 5, 3]]

b = [22, 314, 92]

print(np.dot(A, np.array([75, 10, -11])))
print_matrix(gaussian_elimination(A, b))
