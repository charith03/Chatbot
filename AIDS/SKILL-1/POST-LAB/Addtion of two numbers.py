name = input("Hello, what is your name? ")
print("Hello " + name)
print("Welcome , I will do the calculations for you...")
# Inputs:
input1 = input('Enter first number: ')
input2 = input('Enter second number: ')

# Addition
sum = float(input1) + float(input2)

# Subtration
sub = float(input1) - float(input2)

# Multiplication
mul = float(input1) * float(input2)

# Division
div = float(input1) / float(input2)

# addded result
print('the sum of {0} and {1}is {2}'.format(input1, input2, sum))

# subtracted result
print('the subtraction of {0} and {1} is {2}'.format(input1, input2, sub))

# multiplied result
print('the multiplication of {0} and {1}is {2}'.format(input1, input2, mul))

# divided result
print('the division of {0} and {1}is {2}'.format(input1, input2, div))