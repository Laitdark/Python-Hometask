import cProfile
import timeit

def sieve(n,k):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b[k-1]

def prime1(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def prime2(n,k):
    primes=[]
    for num in range(2, n):
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            primes.append(num)
    return primes[k-1]




n=2000
usernumber=(int(input('Введите номер: ')))
answersieve=sieve(n,usernumber)
answerprime=prime1(n)
print('Position:',usernumber,'Sieve:', answersieve, 'Prime:',answerprime[usernumber-1])

cProfile.run('sieve(n,usernumber)')
cProfile.run('prime1(n)')
cProfile.run('prime2(n,usernumber)')

print('Sieve 100:',timeit.timeit('sieve(n,usernumber)',globals=globals(),number=10))
print('Sieve 1000:',timeit.timeit('sieve(n,usernumber)',globals=globals(),number=100))
print('Prime1 100:',timeit.timeit('prime1(n)',globals=globals(),number=10))
print('Prime1 1000:',timeit.timeit('prime1(n)',globals=globals(),number=100))
print('Prime2 100:',timeit.timeit('prime2(n,usernumber)',globals=globals(),number=10))
print('Prime2 1000:',timeit.timeit('prime2(n,usernumber)',globals=globals(),number=100))
# Sieve 100: 0.010088499999999723
# Sieve 1000: 0.0664273999999998
# Prime1 100: 0.0006183000000001826
# Prime1 1000: 0.010763700000000043
# Prime2 100: 1.0678305999999997
# Prime2 1000: 10.8282635

# Приведены три решения. Сложности: Sieve - O(n/2), Prime - O(n/2), Prime2:O(2n).
# Решение три совершенно неоптимально из-за вложенных циклов, занимает слишком много времени и объективно сложнее
# Решето эффективно, но не идеально, так как все еще есть определенная задержка.
# Идеальным решением является половинчатое  решето в Prime2, работает в 2 раза быстрее, чем Sieve