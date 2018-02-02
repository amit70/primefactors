from math import sqrt
from collections import Counter

def checkPrime(n):
    if n == 2:
        return True

    i = 2
    while(i <= sqrt(n)):
        if n % i == 0:
            return False
        i+=1
    return True


def userInput():
    while True:
        ip = raw_input("Whose prime factors do you want to see? ")

        try:
            n = int(ip)
            if n > 10000:
                print "Enter number less than 10000"
            elif n > 0:
                return n
            else:
                print "Please enter valid input"
        except ValueError:
            print "Enter a number"

def getPrimeFactors(n):
    op = []
    while n != 1:
        k = 2
        while True:
            if n % k == 0:
                n = n / k
                op.append(k)
                break
            k+=1
    return op

def getExponent(op):
    c = Counter(op)
    factors = []

    for i in range(min(op), max(op) + 1):
        if i in op:
            if c[i] != 1:
                factors.append(str(i) + '^' + str(c[i]))
            else:
                factors.append(str(i))

    return factors

def main():

    while True:
        no = userInput()
        if checkPrime(no):
            print "Entered number already prime. Please Enter another number"
        else:
            break

    print getExponent(getPrimeFactors(no))

if __name__ == "__main__":
    main()