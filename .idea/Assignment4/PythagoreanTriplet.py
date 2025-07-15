def is_pythagorean_triplet():
    a, b, c = map(int, input("Enter three numbers: ").split())
    x, y, z = sorted([a, b, c])
    if x * x + y * y == z * z:
        print("Is Pythagorean Triplet: True")
    else:
        print("Is Pythagorean Triplet: False")

is_pythagorean_triplet()