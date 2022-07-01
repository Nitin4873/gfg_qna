#However, if you write a program like this: prints the output
#What a lambda returns #2
result=(lambda x: x + x)(5)
print("the result return : " , result )

x="some kind of a useless lambda"
(lambda x : print(x))(x)

#lambda function pass #3 
#what is this trying to show ?

#A REGULAR FUNCTION
def wrap( funct, *args ):
    funct( *args )

#simple print function
def printer_one( arg ):
    return print (arg)
#note this fyunction has a return 

#simple print function 2
def printer_two( arg ):
    print(arg)

#CALL A REGULAR FUNCTION 
wrap( printer_one, 'printer 1 REGULAR CALL' )
wrap( printer_two, 'printer 2 REGULAR CALL \n' )

#CALL A REGULAR FUNCTION THRU A LAMBDA
wrap(lambda: printer_one('printer 1 LAMBDA CALL'))
wrap(lambda: printer_two('printer 2 LAMBDA CALL'))

#Output:
#printer 1 REGULAR CALL
#printer 2 REGULAR CALL
#printer 1 LAMBDA CALL
#printer 2 LAMBDA CALL

#Code Explanation
#A function called guru that takes another function as the first parameter and any other arguments following it.
#printer_one is a simple function which prints the parameter passed to it and returns it.
#printer_two is similar to printer_one but without the return statement.
#In this part, we are calling the guru function and passing the printer functions and a string as parameters.
#This is the syntax to achieve the fourth step (i.e., calling the guru function) but using lambdas.
