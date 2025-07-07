def matrix_addition():
    print("Enter elements for Matrix 1:")
    matrix1 = [[int(input(f"Matrix1[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

    print("Enter elements for Matrix 2:")
    matrix2 = [[int(input(f"Matrix2[{i}][{j}]: ")) for j in range(2)] for i in range(2)]

    result = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]

    print("Resultant Matrix after Addition:")
    for row in result:
        print(row)

# Call the function
matrix_addition()