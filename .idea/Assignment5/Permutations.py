from itertools import permutations

def generate_permutations():
    s = input("Enter a string to find permutations: ")
    result = [''.join(p) for p in permutations(s)]
    print(f"\nTotal {len(result)} permutations:")
    print(result)

generate_permutations()