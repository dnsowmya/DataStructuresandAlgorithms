def fibonacci(n):
    assert n>= 0 and int(n) == n , 'Fibonacci numbers needs to be a positive integer only!'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)