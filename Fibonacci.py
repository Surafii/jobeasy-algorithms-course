#TODO: HW: Rewrite code, which will return only needed element of Fib sequence



def fibonacci(n):
    if n < 0:
        return 'Invalid number'
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    fibonacci_1, fibonacci_2 = 1, 1
    i = 0
    while i < n-2:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
        i += 1
    else:
        return fibonacci_2

print(fibonacci(10))



