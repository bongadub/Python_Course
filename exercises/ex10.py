# - - coding: utf- 8 - -

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# For loop that shows escape chararctor
while True:
	for i in ["/","_","|","||","|"]:
		print "%s\r" % i,