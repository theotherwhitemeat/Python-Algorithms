#!/usr/bin/env python2.6

import os
import sys

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

    multiple = upper - 1

    # determine if number is equally divided
    if (multiple % num) != 0:
        # iterate until number is equally divided
        print "Iterating multiple down for %d: %d" % (num, multiple)
        while (multiple % num) != 0:
            multiple = multiple - 1 

    print "Multiple of %d less than %d: %d" % (num, upper, multiple)

    # get added sum of lowest and highest number
    aggr_sum = num + multiple
    print "Upper num for %d: %d" % (num, aggr_sum)

    aggr_sum = (aggr_sum * (multiple / num)) / 2

    return aggr_sum

if __name__ == "__main__":

    # create number list
    num_list = [3, 5]
    sums = {}

    # set upper bound
    upper = 1000

    lcm = get_lcm(num_list)
    print "lcm: %d" % (lcm)

    # add up sums
    for num in num_list:
        sums[num] = get_sum_under_limit(num, upper)
    total_sum = sum(x for x in sums.values())

    # subtract lcm sum
    nuke_me = get_sum_under_limit(lcm, upper)

    total_sum -= nuke_me

    print total_sum
    print sums










