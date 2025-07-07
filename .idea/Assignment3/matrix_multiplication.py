def matrix_multiplication():
    print("Enter elements for Matrix A:")
    A = [[int(input(f"A[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

    print("Enter elements for Matrix B:")
    B = [[int(input(f"B[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

    result = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix after Multiplication:")
    for row in result:
        print(row)

# Call the function
matrix_multiplication()