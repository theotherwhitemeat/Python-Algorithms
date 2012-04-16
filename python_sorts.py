#!/usr/bin/python2.6

# Insertion sort
# best case runtime == O(n)
# worst case runtime == O(n2)
# average case runtime == O(n2)
# worst case space complexity == O(n)

import optparse

def setup_ops():
	""" sets up options """

	global options

	parser = optparse.OptionParser()
	optgroup = optparse.OptionGroup(parser, "Command-line options")

	optgroup.add_option("--items", "-i", dest="inputs")

	parser.add_option_group(optgroup)
	(options, args) = parser.parse_args()


class sorter:
	""" sorter superclass """

	def __init__(self, inputs):
		""" initialize class """
		self.inputs = inputs

	def sort_me(self):
		""" stub function for sorting """
		pass

	def print_inputs(self):
		""" prints inputs """
		print self.inputs


class insertion_sorter(sorter):

	def sort_me(self):
		""" pushes input into sorted list

		 Insertion sort
		 best case runtime == O(n)
		 worst case runtime == O(n2)
		 average case runtime == O(n2)
		 worst case space complexity == O(n)
		"""

		for i in range(len(self.inputs)):
			item = self.inputs[i]
			da_hole = i

			# move the hole to next smaller value until a[da_hole -1] is <=item
			while da_hole > 0 and self.inputs[da_hole - 1] > item:
				self.inputs[da_hole] = self.inputs[da_hole -1]
				da_hole = da_hole -1
				print self.inputs

			# put item in the hole
			self.inputs[da_hole] = item
			print self.inputs

		print self.inputs


class selection_sorter(sorter):

	def sort_me(self):
		""" sorts self.inputs

		Selection sort
		best case runtime == O(n2)
		worst case runtime == O(n2)
		average case runtime == O(n2)
		worst case space complexity == O(n), O(1) auxiliary """

		for ipos, item in enumerate(self.inputs):
			# find the min element in the unsorted a[iPos ... n-1]

			# assume the first element is the minimum
			imin = ipos
			# test against every other element
			for i in range(ipos+1, len(self.inputs)):
				if self.inputs[i] < self.inputs[imin]:
					imin = i

			if (imin != ipos):
				temp = self.inputs[imin]
				self.inputs[imin] = self.inputs[ipos]
				self.inputs[ipos] = temp


class quick_sorter(sorter):

	def sort_me(self):
		""" sorts self.inputs 

		Quick sort
		best case runtime == O(nlogn)
		worst case runtime == O(n2)
		average case runtime == O(nlogn)
		worst case space complexity == O(n)

		Picks pivot points, and pushes items around the
		 pivots until the left is lesser and right is
		 greater than the pivot point value """

		self.inputs = self.__quicksort__(self.inputs)

	def __quicksort__(self, inputs):
		""" quicksort recursive function """
		if len(inputs) <= 1:
			return inputs

		print "inputs:", inputs
		pivot = inputs.pop(len(inputs)/2)

		less, greater = [], []

		for item in inputs:
			if item <= pivot:
				less.append(item)
			else:
				greater.append(item)

		return(self.__quicksort__(less) + [pivot] + self.__quicksort__(greater))


def main():
	insertion_sort_me([3,2,5,2])


if __name__ == "__main__":
	""" main program loop """

	setup_ops()
	print options
	main()











