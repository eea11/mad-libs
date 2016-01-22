# This is an introduction.
print """
Welcom to my Mad Libs game.
Please enter the information that is specified.
"""

# In the following lines I ask for infromation
# The information is stuff like name, place, food etc.
print "Please enter your name."
name = raw_input("> ")

print "Please enter a location."
place1 = raw_input("> ")

print "Please enter an -ing action verb."
verb1 = raw_input("> ")

print "Enter a food."
food1 = raw_input("> ")

print "Enter another person's name."
person = raw_input("> ")

# Here, I ouput all the before entered information.
# %s outputs the information if it is a string.
print "So %s is at %s %s while eating %s with %s,." % (
		name, place1, verb1, food1, person)
