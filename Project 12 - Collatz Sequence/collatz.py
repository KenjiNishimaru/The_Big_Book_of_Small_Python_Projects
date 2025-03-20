def Collatz(n):
    if n == 1:
        print(n)
        return
    print(f'{n}',end=', ')
    if n % 2 == 0:
        n = int(n/2)
        Collatz(n)
    else:
        n = (n*3) + 1
        Collatz(n)

print('The Collatz conjecture is a sequence of numbers produced from a starting number positive integer n.')
n = int(input('> '))
Collatz(n)

