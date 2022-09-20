# Metodo para demostrar la suceción o Ley de fibonaccio f(n) = f(n-1)+f(n-2)
def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)

for x in range(20):
    print(fib(x))
