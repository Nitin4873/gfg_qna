#Problem statement : Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward.
#For example, 121 is a palindrome while 123 is not.
#
#Example 1:input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#
#Example 2:Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
#Example 3:Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
#Constraints:-231 <= x <= 231 - 1
#
#Follow up: Could you solve it without converting the integer to a string?

import math 

print("Hello World")

def take_input() : 
  read_val = input("enter a number : ") 
  #print(" \n the value entered is : {}".format(read_val)) 
  return int(read_val) 

def count_digits(in_var) :
    count_digit = 0 
    while True : 
       if in_var > 0 :
         #print("[fxn count_digits] the in_var var : {} at the digit_count : {}".format(in_var,count_digit)) 
         in_var = int(in_var / 10) 
         count_digit = count_digit + 1 
       elif in_var == 0 : 
          break 
    #print("[fxn count_digits] length of digit : {}".format(count_digit))
    return count_digit

import math
def fetch_digit(in_var , pos , length ) :
    if pos <= 0 or length <= 0 or length < pos : 
       ret_digit=None
    elif pos < length :
       ret_digit=int( ( in_var % math.pow(10,length - (pos - 1)) ) / math.pow(10,(length-pos)) )
    elif pos==length : 
       ret_digit=int(in_var % math.pow(10,length - (length - 1)))
    #print("[fxn fetch_digit] the in var : {} with the length : {} and the pos : {} has value {}".format(in_var , length ,pos ,ret_digit ))
    return ret_digit

#fetch_digit(12345 , 1 , 5) 
#fetch_digit(12345 , 2 , 5) 
#fetch_digit(12345 , 4 , 5) 
#fetch_digit(12345 , 5 , 5) 
#fetch_digit(12345 , -5 , 5) 
#fetch_digit(12345 , 6 , 5) 

def ispallindrome_num(in_arg) :
    ispallindrome=False
    pos=1 
    length=count_digits(in_arg)
    while True :
       #print("[fxn ispallindrome] the pos : {} and the length : {}".format(pos,length))
       lhs = fetch_digit(in_arg , pos , length)
       rhs = fetch_digit(in_arg , length - pos + 1 , length)
       if lhs == rhs and pos <= length : 
          print("lhs==rhs match -> for input : {}, digit at the postition : {} is = {} and at the reverse position : {} the value is = {}".format(in_arg,pos,lhs,length - pos + 1,rhs))
          ispallindrome=True 
       elif lhs != rhs and pos <= length : 
          print("lhs==rhs NOT match -> for input : {}, digit at the postition : {} is = {} and at the reverse position : {} the value is = {}".format(in_arg,pos,lhs,length - pos + 1,rhs))
          ispallindrome=False
       elif pos > length :
          print("limit reached")
          break

       pos=pos + 1
    return ispallindrome 

print ("result of the pallindrome check is : {}".format(str(ispallindrome_num(take_input()))) )
print("finish code")