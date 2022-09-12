from math import sqrt
from msvcrt import kbhit

def multiples_sum(a, b, limit):
    tot= 0
    for i in range(limit):
        if i % a == 0 or i % b == 0 :
            tot = tot + i 
    return (tot)
  

def fibonacci_sequence_even_valued_terms_sum(limit) :
    fibs = [0, 1, 1]
    i = 3
    nxt = 0
    tot = 0
    while nxt <= limit:
        curr = fibs[i-1]+fibs[i-2]
        fibs.append(curr)
        if curr % 2 == 0 :
            tot += curr
        nxt = curr + fibs[i-1]
        i += 1
    return tot


def prime_number(n) :
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def gen_factors(n) :
    fact = set([])
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            fact.add(i)
            fact.add(n//i)
        i += 1
    return sorted(fact)

def largest_prime_factor(n):
    prime = []
    for i in gen_factors(n):
        if prime_number(i):
            prime.append(i)
    return max(prime)

def is_palindromic(n):
    n = str(n)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            return False
    return True

def largest_palindromic_number(a,b):
    palindromic_numbers = []
    for i in range(a, b+1):
        for j in range(a, b+1):
            k = j * i
            if is_palindromic(k):
                palindromic_numbers.append(k)
            
    return max(palindromic_numbers)

print(largest_palindromic_number(100, 999))




        

