def add(m, n, A, B, Y):
    for i in range(m * n):
        Y[i] = A[i] + B[i]

def linearcomb(m, n, sa, sb, A, B, Y):
    for i in range(m * n):
        Y[i] = sa * A[i] + sb * B[i]

def transpose(m, n, A, A_t):
    for i in range(m):
        for j in range(n):
            A_t[j * m + i] = A[j + i * n]

def equal(m, n, A, B):
    for i in range(m * n):
        if A[i] != B[i]:
            return 0
    return 1

def mult(m1, n1m2, n2, A, B, Y):
    for i in range(m1):
        for j in range(n2):
            sum = 0
            for k in range(n1m2):
                sum += A[i * n1m2 + k] * B[j + k * n2]
            Y[j + i * n2] = sum
