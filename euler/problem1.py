#!/usr/bin/env python2.6


# create number list
num_list = [3, 5]
sums = {}

# set upper and lower bounds
upper = 1000 
lower = 0

LCM = 15

for num in num_list:
    

def get_sum_under_limit(num, limit):

    multiple = upper - 1

    # determine if number is equally divided
    if (multiple % num) == 0:
        even = True
    else:
        even = False
        # iterate until number is equally divided
        print "Iterating multiple down for %d: %d" % (num, multiple)
        while (multiple % num) != 0:
            multiple = multiple - 1 

    print "Multiple of %d less than %d: %d" % (num, upper, multiple)

    # get added sum of lowest and highest number
    aggr_sum = num + multiple
    print "Upper num for %d: %d" % (num, aggr_sum)

    # if evenly divided, the algorithm is aggr_sum * .5 divisions
    if even:
        print "%d goes into %d evenly" % (num, upper)
        aggr_sum = (aggr_sum * (multiple / num)) / 2
    # if not evenly divided, the algorithm adds .5 aggr_sum's
    else:
        print "%d goes into %d oddly" % (num, upper)
        aggr_sum = (aggr_sum * (multiple / num)) / 2 #- (aggr_sum / 2)

    sums[num] = aggr_sum


total_sum = sum(x for x in sums.values())

print total_sum
print sums

