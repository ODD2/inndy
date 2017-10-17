from z3 import *

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True

Fibonacci_primes=[
2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497, 1066340417491710595814572169, 19134702400093278081449423917, 475420437734698220747368027166749382927701417016557193662268716376935476241]

#print(is_prime(Fibonacci_primes[6]))
#print Fibonacci_primes


VAL1=BitVec('x',32)
VAL2=BitVec('y',32)

first=[(VAL1 * VAL2) == 3720560946]

second=[(VAL1^126)*(VAL2+16)==1931514558]


third=[(VAL1-VAL2) & 4095==3295]

num1=1
num2=1
for i in range(0,1000):
	temp = num1+num2
        num2=num1
 	num1=temp
	int32only = num1&0xffffffff
#	print "%d"%(iny32only)
	if is_prime(int32only)==True:
#		print "%d!!!!!!!!!!!IS PRIME"%(int32only)
		fourth=[VAL1==num1]
#		print  first+second+third+fourth
		solve(first+second+third+fourth)

