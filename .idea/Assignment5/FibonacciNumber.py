def fibonacci_dp():
    n = int(input("Enter the position (n) for Fibonacci: "))
    if n <= 1:
        print(f"{n}th Fibonacci number is {n}")
        return
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    print(f"{n}th Fibonacci number is {fib[n]}")

fibonacci_dp()