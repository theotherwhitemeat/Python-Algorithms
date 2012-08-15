#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600,851,475,143
"""

import math_lib.math as mathy


def main():
	""" does the main thaing """

	prime_chunk = 100
	my_num = 600851475143
	factors = []

	test = mathy.prime_factor(600851475143)
	print test

if __name__ == "__main__":
	main()