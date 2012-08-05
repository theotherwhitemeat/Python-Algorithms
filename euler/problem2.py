#!/usr/bin/env python

""" Each new term in the Fibonacci sequence is generated
 by adding the previous two terms. By starting with 1 and 2,
  the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the 
even-valued terms. """


def get_fibos(count=None, fibo_max=None):
	""" gets the fibos """

	fibos = [1, 2]

	if (count is not None):
		while (len(fibos) < count):
			i = len(fibos) - 1
			fibos.append(fibos[i] + fibos[i - 1])
	elif (fibo_max is not None):
		while (fibos[len(fibos)-1] < fibo_max):
			i = len (fibos) - 1
			fibos.append(fibos[i] + fibos[i - 1])
		fibos = fibos[:-1]

	return fibos


if __name__ == "__main__":
	derp_max = 4000000
	nums = get_fibos(fibo_max=derp_max)
	num_sum = 0

	for derp in nums:
		if (derp % 2) == 0:
			num_sum = num_sum + derp

	print "Sums below %d: %d" % (derp_max, num_sum)