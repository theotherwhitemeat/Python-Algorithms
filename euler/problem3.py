#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143
"""

def gen_primes(upper_limit=None, count=None):
	""" generates prime numbers up to the limit """

	# take it to the limit!
	primes = [2]
	counter = 3

	while (counter < upper_limit):
		prime_num = True
		for prime in primes:
			if (counter % prime) == 0:
				prime_num = False
				break
		if prime_num:
			primes.append(counter)
			print counter
		counter = counter + 2

	return primes

def prime_factor(num):
	""" factors a num into it's prime constituents """

	# take it to the limit!
	primes = [2]
	counter = 3
	factors = []

	while max(primes) < num:
		# see if existing primes are factors
		for prime in primes:
			if (num % prime) == 0:
				factors.append(prime)
				num = num / prime
				print "Found factor: %d" % (prime)
				print "Number to factor: %d" % (num)
				break

		# add to existing primes if we exhaust them
		prime_num = True
		for prime in primes:
			if (counter % prime) == 0:
				prime_num = False
				break
		if prime_num:
			primes.append(counter)
			print counter
		counter = counter + 2

	factors.append(num)
	return factors

def main():
	""" does the main thaing """

	prime_chunk = 100
	my_num = 600851475143
	factors = []

	test = prime_factor(600851475143)
	print test

#	my_primes = gen_primes(max_num)
#	print my_primes


if __name__ == "__main__":
	main()