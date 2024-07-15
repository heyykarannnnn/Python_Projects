def generate_fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

n = int(input("enter the number : "))
fibonacci_sequence = list(generate_fibonacci(n))
print(fibonacci_sequence)