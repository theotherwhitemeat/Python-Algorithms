""" Math library for Euler fun and frolic.  Fuck the police. """

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

def get_lcm(num_list):
    """ 'calculates' the lcm for input list """

    # todo - make this a library call, and optimize
    #  1) get_primes()
    #  2) uniquify primes
    #  3) multiple for lcm

    def lcm_ready(numer, nums):
        """ determines if numer is divisible """

        for num in nums:
            if numer % num != 0:
                return False
        return True

    lcm = 1

    while not lcm_ready(lcm, num_list):
        lcm += 1

    return lcm

def get_sum_under_limit(num, limit):
    """ returns sum of multiples of a given number under limit """

    multiple = limit - 1

    # determine if number is equally divided
    if (multiple % num) != 0:
        # iterate until number is equally divided
        print "Iterating multiple down for %d: %d" % (num, multiple)
        while (multiple % num) != 0:
            multiple = multiple - 1 

    print "Multiple of %d less than %d: %d" % (num, limit, multiple)

    # get added sum of lowest and highest number
    aggr_sum = num + multiple
    print "Upper num for %d: %d" % (num, aggr_sum)

    aggr_sum = (aggr_sum * (multiple / num)) / 2

    return aggr_sum

def is_palindromic(num):
	""" determines if a number is palindromic """

	rev = 0
	num_copy = num

	while (num_copy) > 0:
		rev *= 10
		digit = num_copy % 10
		rev += digit
		num_copy /= 10

	return num == rev

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