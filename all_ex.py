# Import stuff
# Used in Ex 13:
from sys import argv
# Used in Ex 17:
from os.path import exists

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
	age = raw_input("How old are you ? ")
	height = raw_input("How tall are you? ")
	weight = raw_input("How much do you weigh? ")
	print "So, you're %r old, %r tall and %r heavy." % (
		age, height, weight)

# Ex 13 - Parameters, Unpacking, Variables
def ex13():
	# requires the following
	# from sys import argv (imported at the start of this file)
	script, first, second, third = argv
	print "The script is called:", script
	print "Your fisrt variable is:", first
	print "Yout second variable is:", second
	print "Your third variable is:", third

# Ex 14 - Prompting and Passing
def ex14():
	# requires the following
	# from sys import argv (imported at the start of this file)
	script, user_name = argv
	prompt = '> '
	print " Hi %s, I'm the %s script." % (user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me %s?" % user_name
	likes = raw_input(prompt)
	print "Where so you live %s?" % user_name
	lives = raw_input(prompt)
	print "What kind of computer do you have?"
	computer = raw_input(prompt)
	print """
	Aright, so you said %r about liking me.
	You live in %r. Not sure where that is.
	And you have a %r computer. Nice.
	""" % (likes, lives, computer)

# Ex 15 - Reading Files
def ex15():
	# requires the following
	# from sys import argv (imported at the start of this file)
	script, filename = argv
	txt = open(filename)
	print "Here's you file %r:" % filename
	print txt.read()
	print "Type the filename again:"
	file_again = raw_input("> ")
	txt_again = open(file_again)
	print txt_again.read()

# Ex 16 - Reading and Writing Files
def ex16():
	# Some important stuff
	# close -- Closes the file. Like File->Save.. in your editor.
	# read -- Reads the contents of the file. You can assign the result to a variable.
	# readline -- Reads just one line of a text file.
	# truncate -- Empties the file. Watch out if you care about the file.
	# write(stuff) -- Writes stuff to the file.
	#
	# requires the following
	# from sys import argv (imported at the start of this file)
	script, filename = argv
	print "We're going to erase %r." % filename
	print "If you don't want that, hit CTRL-C (^C)."
	print "If you do want that, hit RETURN."
	raw_input("?")
	print "Opening the file..."
	target = open(filename, 'w')
	print "Truncating the file. Goodbye!"
	target.truncate()
	print "Now I'm going to ask you for three lines."
	line1 = raw_input("line 1: ")
	line2 = raw_input("line 2: ")
	line3 = raw_input("line 3: ")
	print "I'm going to write these to the file."
	target.write(line1)
	target.write("\n")
	target.write(line2)
	target.write("\n")
	target.write(line3)
	target.write("\n")
	print "And finally, we close it."
	target.close()

# Ex 17 - More Files
def ex17():
	# requires the following
	# from sys import argv (imported at the start of this file)
	# from os.path import exists (imported at the start of this file)
	script, from_file, to_file = argv
	print "Copying from %s to %s" % (from_file, to_file)
	# we could do these two on one line too, how?
	in_file = open(from_file)
	indata = in_file.read()
	print "The input file is %d bytes long" % len(indata)
	print "Does the output file exist? %r" % exists(to_file)
	print "Ready, hit RETURN to continue, CTRL-C to abort."
	raw_input()
	out_file = open(to_file, 'w')
	out_file.write(indata)
	print "Alright, all done."
	out_file.close()
	in_file.close()

# Ex 18 - Names, Variables, Code, Functions
def ex18():
	# this one is like your scripts with argv
	def print_two(*args):
	    arg1, arg2 = args
	    print "arg1: %r, arg2: %r" % (arg1, arg2)
	# ok, that *args is actually pointless, we can just do this
	def print_two_again(arg1, arg2):
	    print "arg1: %r, arg2: %r" % (arg1, arg2)
	# this just takes one argument
	def print_one(arg1):
	    print "arg1: %r" % arg1
	# this one takes no arguments
	def print_none():
	    print "I got nothin'."
	print_two("Zed","Shaw")
	print_two_again("Zed","Shaw")
	print_one("First!")
	print_none()

# Ex 19 - Functions and Variables
def ex19():
	def cheese_and_crackers(cheese_count, boxes_of_crackers):
		print "You have %d cheeses!" % cheese_count
		print "You have %d boxes of crackers!" % boxes_of_crackers
		print "Man that's enough for a party!"
		print "Get a blanket.\n"
	print "we can just give the function numbers directly:"
	cheese_and_crackers(20, 30)
	print "OR, we can use variables form out script:"
	amount_of_cheese = 10
	amount_of_crackers = 50
	cheese_and_crackers(amount_of_cheese, amount_of_crackers)
	print "we can even do math inside too:"
	cheese_and_crackers(10 + 20, 5 + 6)
	print "And we can combine the two, variables and math:"
	cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
  
# Ex 20 - Functions and Files
def ex20():
	# requires the following
	# from sys import argv (imported at the start of this file)
	script, input_file = argv
	def print_all(f):
		print f.read()
	def rewind(f):
		f.seek(0)
	def print_a_line(line_count, f):
		print line_count, f.readline()
	current_file = open(input_file)
	print "First let's print the whole file:\n"
	print_all(current_file)
	print "Now let's rewind, kind of like a tape."
	rewind(current_file)
	print "Let's print three lines:"
	current_line = 1
	print_a_line(current_line, current_file)
	current_line = current_line + 1
	print_a_line(current_line, current_file)
	current_line = current_line + 1
	print_a_line(current_line, current_file)

# Ex 21 - Functions Can Return Something
def ex21():
	def add(a, b):
		print "ADDING %d + %d" % (a, b)
		return a + b
	def subtract(a, b):
		print "SUBTRACTING %d - %d" % (a, b)
		return a - b
	def multiply(a, b):
		print "MULTIPLYING %d * %d" % (a, b)
		return a * b
	def divide(a, b):
		print "DEVIDING %d / %d" % (a, b)
		return a / b
	print "Let's do some math with just functions!"
	age = add(30,50)
	height = subtract(78, 4)
	weight = multiply(90, 2)
	iq = divide(100, 2)
	print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
		age, height, weight, iq)
	# A puzzle for the extra credit, type it in anyway.
	print "Here is the puzzle."
	what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
	print "That becomes: ", what, "Can you do it hand?"

# Ex 22 - What Do You Know So Far?
def ex22():
	pass
	# There is nothing in this exercise 

# Ex 23 - Read Some Code
def ex23():
	pass

# Ex 24 - 
def ex24():
	pass

# Ex 25 - 
def ex25():
	pass

# Ex 26 - 
def ex26():
	pass

# Ex 27 - 
def ex27():
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
	ex21()
	# test()
