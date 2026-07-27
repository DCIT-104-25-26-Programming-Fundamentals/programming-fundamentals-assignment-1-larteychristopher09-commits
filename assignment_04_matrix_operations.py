# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
def read_matrix(rows, cols, label=""):
    """Read a matrix of given size from user input, one row per line."""
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}{label}: ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Print a matrix in a neat, aligned grid."""
    for row in matrix:
        print("  ".join(f"{val:>4}" for val in row))


def transpose(matrix):
    """Return the transpose of a matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b):
    """Return the element-wise sum of two same-size matrices."""
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b):
    """Return the matrix product of A (MxN) and B (NxP)."""
    m = len(a)
    n = len(b)
    p = len(b[0])
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


if __name__ == "__main__":
    # --- Part A: Transpose ---
    print("--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix))

    # --- Part B: Addition ---
    print("\n--- Part B: Add Two Matrices ---")
    add_rows = int(input("Enter number of rows: "))
    add_cols = int(input("Enter number of columns: "))
    print("Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols)
    print("Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols)

    print("\nSum Matrix:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    # --- Part C: Multiplication ---
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("Matrix A:")
    mat_a = read_matrix(m, n)
    print("Matrix B:")
    mat_b = read_matrix(n, p)

    print("\nProduct Matrix (A x B):")
    print_matrix(multiply_matrices(mat_a, mat_b))