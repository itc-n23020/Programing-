def fibonacci_sequence(n):
    a, b = 0, 1
    fib_sequence = [a, b]

    while b <= n:
        a, b = b, a + b
        fib_sequence.append(b)

    return fib_sequence
