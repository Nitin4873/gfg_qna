#lambda p1, p2: expression
#p1 & p2 : arg passed to the function
#note - no brackets or parantheses() are used beside the function.

#eg : simple lambda function - working 
adder = lambda x, y: x + y
print (adder (1, 2))

#What a lambda returns is the expression result ? or the function itself ? .
# We declare a lambda that calls a print statement and prints the result.
string='some kind of a useless lambda'
print(lambda string : print(string))

#Expected Output: <function <lambda> at 0x00000185C3BF81E0>
# But why doesn’t the program print the string we pass? 
# This is because the lambda itself returns a function object. 

# In this example, the lambda is not being called by the print function but simply returning the function object and the memory location where it is stored. 
# That’s what gets printed at the console.

#However, if you write a program like this:
#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)

# Expected Output: some kind of a useless lambda 
# the string we pass gets printed at the console. 
# But what is that weird syntax, and why is the lambda definition covered in brackets? 
# In this part, we are defining a lambda and calling it immediately by passing the string as an argument. 
# This is something called an IIFE, IIFE stands for immediately invoked function execution