def fibonacci_sequence(n):
    a, b = 0, 1
    result = [a, b]

    while b <= n:
        a, b = b, a + b
        result.append(b)

    print(result)
