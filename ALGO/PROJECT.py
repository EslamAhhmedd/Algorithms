def strassen_matrix_multiply(A, B):
    n = len(A)

    # Base case: If matrices are 1x1, return their product
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Divide matrices into four submatrices
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Recursive calls to calculate various products
    P1 = strassen_matrix_multiply(A11, subtract_matrices(B12, B22))
    P2 = strassen_matrix_multiply(add_matrices(A11, A12), B22)
    P3 = strassen_matrix_multiply(add_matrices(A21, A22), B11)
    P4 = strassen_matrix_multiply(A22, subtract_matrices(B21, B11))
    P5 = strassen_matrix_multiply(add_matrices(A11, A22), add_matrices(B11, B22))
    P6 = strassen_matrix_multiply(subtract_matrices(A12, A22), add_matrices(B21, B22))
    P7 = strassen_matrix_multiply(subtract_matrices(A11, A21), add_matrices(B11, B12))

    # Calculate resulting submatrices
    C11 = add_matrices(subtract_matrices(add_matrices(P5, P4), P2), P6)
    C12 = add_matrices(P1, P2)
    C21 = add_matrices(P3, P4)
    C22 = subtract_matrices(subtract_matrices(add_matrices(P5, P1), P3), P7)

    # Combine submatrices into the result matrix
    C = combine_matrices(C11, C12, C21, C22)
    
    return C

def split_matrix(matrix):
    n = len(matrix)
    mid = n // 2
    A11 = [matrix[i][:mid] for i in range(mid)]
    A12 = [matrix[i][mid:] for i in range(mid)]
    A21 = [matrix[i][:mid] for i in range(mid, n)]
    A22 = [matrix[i][mid:] for i in range(mid, n)]
    return A11, A12, A21, A22

def combine_matrices(A11, A12, A21, A22):
    return [A11[i] + A12[i] for i in range(len(A11))] + [A21[i] + A22[i] for i in range(len(A21))]

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]
