# - - coding: utf- 8 - -

print "\nExercise 8"

#Prinitnig on Exercise 8
formatter = "%r %r %r %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)


#Prinitng on Exercise 9
print "\nExercise 9"

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\njan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

print "Here are the days: ", days
print "Here are the months: ", months


print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""