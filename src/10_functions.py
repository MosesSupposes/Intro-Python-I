# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
	return True if n % 2 == 0 else False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def print_even_or_odd(n):
	print("Even!" if (is_even(n)) else "Odd")

print_even_or_odd(num)
