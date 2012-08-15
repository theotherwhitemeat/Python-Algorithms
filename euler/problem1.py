#!/usr/bin/env python2.6

import os
import sys
import math_lib.math as mathy

if __name__ == "__main__":

    # create number list
    num_list = [3, 5]
    sums = {}

    # set upper bound
    upper = 1000

    lcm = mathy.get_lcm(num_list)
    print "lcm: %d" % (lcm)

    # add up sums
    for num in num_list:
        sums[num] = mathy.get_sum_under_limit(num, upper)
    total_sum = sum(x for x in sums.values())

    # subtract lcm sum
    nuke_me = mathy.get_sum_under_limit(lcm, upper)

    total_sum -= nuke_me

    print total_sum
    print sums










