# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if not n:
        return 0
    if n < 0:
        return (-1) ** (-n + 1) * Fibonacci(-n)
    if n in (1, 2):
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

k = int(input('k = '))
fibo = []
for i in range(-k, k + 1):
    fibo.append(Fibonacci(i))
print(fibo)