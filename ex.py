# Ex 1 - A Good First Program
def ex1():
	print "hello world"
	print "Hello Again"
	print "I like typing this."
	print "This is fun"
	print "Yay! Printing"
	print "I'd much rather you 'not'."
	print 'I "said" do not touch this.'

# Ex 2 - Comments And Pound Characters
def ex2():
	# A comment, this is so you can read your program later.
	# Anything after the # is ignored by python.
	print "I could have code like this." # and the comment after is ignored
	# You can also use a comment to "disable" or comment out a piece of code:
	# print "This won't run."
	print "This will run."

# Ex 3 - Numbers And Math
def ex3():
	print "I will now count my chickens:"
	print "Hens", 25 + 30 / 6
	print "Roosters", 100 - 25 * 3 % 4
	print "Now I will count the eggs:"
	print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
	print "Is it true that 3 + 2 < 5 - 7?"
	print 3 + 2 < 5 - 7
	print "What is 3 + 2?", 3 + 2
	print "What is 5 - 7?", 5 - 7
	print "Oh, that's why it's False."
	print "How about some more."
	print "Is it greater?", 5 > -2
	print "Is it greater or equal?", 5 >= -2
	print "Is it less or equal?", 5 <= -2
	# PEMDAS Python maths operation -  Parentheses Exponents Multiplication Division Addition Subtraction

# Ex 4 - Variables And Names
def ex4():
	cars = 100
	space_in_a_car = 4.0
	drivers = 30
	passengers = 90
	cars_not_driven = cars - drivers
	cars_driven = drivers
	carpool_capacity = cars_driven * space_in_a_car
	average_passengers_per_car = passengers / cars_driven
	print "There are", cars, "cars available."
	print "There are only", drivers, "drivers available."
	print "There will be", cars_not_driven, "empty cars today."
	print "We can transport", carpool_capacity, "people today."
	print "We have", passengers, "to carpool today."
	print "We need to put about", average_passengers_per_car, "in each car."
	# print without space
	print "Hey %s there." % "you" 
	# %s = String (converts any Python object using str()), prints = you
	# %d = Signed integer decimal, 
	# %f = Floating point decimal format,
	# %F = Floating point decimal format,
	# %c = Single character (accepts integer or single character string), 
	# %r = String (converts any Python object using repr()), prints = 'you' #Best used for debugging#
	# more reading = https://docs.python.org/2/library/stdtypes.html

# Ex 5 - More Variables and Printing
def ex5():
	my_name = 'Zed A. Shaw'
	my_age = 35 # really ?
	my_height = 74 # inches
	my_weight = 180 #lbs
	my_eyes = 'Blue'
	my_teeth = 'White'
	my_hair = 'Brown'
	print "Let's talk about %s." % my_name
	print "He's %d inches tall." % my_height
	print "He's %d pounds heavy." % my_weight
	print "Actually that's not too heavy."
	print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
	print "His teeth are usually %s depending on the coffee." % my_teeth
	#this line is trickery, try to get it exactly right
	print "If I add %d, %d, and %d I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight)

# Ex 6 - Strings and Text
def ex6():
	x = "There are %d types of people." % 10
	binary = "binary"
	do_not = "don't"
	y = "Those who know %s and those who %s." % (binary, do_not)
	print x
	print y
	print "I said: %r." % x
	print "I also said: '%s'." % y
	hilarious = False
	joke_evaluation = "Isn't that joke so funny?! %r"
	print joke_evaluation % hilarious
	w = "This is the left side of..."
	e = "a string with a right side."
	print w + e

# Ex 7 - More Printing
def ex7():
	print "Mary had a little lamb."
	print "Its fleece was white as %s." % 'snow'
	print "And everywhere that Mary went."
	print "." * 10 # what'd that do ? Ans : multiplies . for 10 times = ..........
	end1 = "C"
	end2 = "h"
	end3 = "e"
	end4 = "e"
	end5 = "s"
	end6 = "e"
	end7 = "B"
	end8 = "u"
	end9 = "r"
	end10 = "g"
	end11 = "e"
	end12 = "r"
	# watch that comma at the end. try removinf it to see what happens
	print end1 + end2 + end3 + end4 + end5 + end6,
	print end7 + end8 + end9 + end10 + end11 + end12

# Ex 8 - Printing, Printing
def ex8():
	formatter = "%r %r %r %r"
	print formatter % (1,2,3,4)
	print formatter % ("one", "two", "three", "four")
	print formatter % (True, False, False, True)
	print formatter % (formatter, formatter, formatter, formatter)
	print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
	)

# Ex 9 - Printing, Printing, Printing
def ex9():
	# Here's some new strange stuff, rmember type it excatly.
	days = "Mon Tue Wed Thu Fri Sat Sun"
	months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
	print "Here are the days: ", days
	print "Here are the months: ", months
	print """ 
	There's something going on here.
	With the three double-quotes.
	We'll be able to type as much as wel like.
	Even 4 lines if we want, or 5, or 6.
	""" # This """ will allow you to print out to multiple lines

# Ex 10 - What Was That?
def ex10():
	tabby_cat = "\tI'm tabbed in."
	persian_cat = "I'm split\non a line."
	blackslash_cat = "I'm \\ a \\ cat."
	fat_cat = """
	I'll do a list:
	\t* Cat food
	\t* Fishies
	\t* Catnip\n\t\t* Grass
	"""
	print tabby_cat
	print persian_cat
	print blackslash_cat
	print fat_cat

# Ex 11 - Asking Questions
def ex11():
	print "How old are you?",
	age = raw_input()
	print "How tall are you?",
	height = raw_input()
	print "How much do you weigh?",
	weight = raw_input()
	print "So, you're %r old, %r tall and %r heavy." % (
		age, height, weight)

# Ex 12 - Prompting People
def ex12():
	pass

# Ex 13 - 
def ex12():
	pass

# Ex 14 - 
def ex13():
	pass

# Ex 15 - 
def ex14():
	pass

# Ex 16 - 
def ex15():
	pass

# Ex 17 - 
def ex16():
	pass

# Testing function - used of testing some part of my code
def test():
	# while True:
		# for i in ["/","-","|","\\","|"]:
			# print "%s\r" % i,
	pass # to declare an empty function
	# print "Hey %s there." % "you" 
	# print " This is to print %r" % "print this no matter what."
	# print "a " + "b" # we can also write the program like this but this is not the ethical way 
# main function
if __name__ == "__main__":
	ex12()
	# test()
