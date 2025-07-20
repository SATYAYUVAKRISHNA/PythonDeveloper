def rotate_matrix_90():
    n = int(input("Enter the size of the square matrix (n x n): "))
    matrix = [list(map(int, input(f"Enter row {i+1}: ").split())) for i in range(n)]

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for row in matrix:
        row.reverse()

    print("Rotated Matrix:")
    for row in matrix:
        print(row)

rotate_matrix_90()
