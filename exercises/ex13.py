# - - coding: utf- 8 - -

from sys import argv

script, first, second, third = argv

#displayuing given arguments
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#prompting user input
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)