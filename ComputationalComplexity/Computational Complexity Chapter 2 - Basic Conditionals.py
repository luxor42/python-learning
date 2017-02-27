# Chapter 2.
#  2.2 - Basic conditionals
'''
x = 9
if x%2 == 0:
    print 'Even'
else:
    print 'Odd'
print 'Done with conditional'
'''

# Write a program that examines three variables (x,y,z) and prints the largest odd number among them.
# If none of them are odd, it should print a message to that effect.
'''
x,y,z=9,11,8
if x % 2 == 1 and (x >= y or y % 2 == 0) and (x >= z or z % 2 == 0):
        print x
elif y % 2 == 1 and (y >= z or z % 2 == 0):
        print y
elif z % 2 == 1:
    print z
else:
    print 'no odd numbers'
'''

# 2.3 - Strings and Input
# + is overloaded.  3*'a' --> aaa.  'ab'+'cd' --> abcd
# Curiously, [string] < [int] is always false.
# string functions: len, indexing with [], slicing with [first, last-1]
# input for python: raw_input

'''
name = raw_input('Enter your name:')
print name
print type(name)
print int(3.14159)
'''


#  2.4 - Iteration (looping)
#   while(var != 0):
#       code block

#  Write a program that tasks the user to input 10 integers, then prints
#  the largest odd number that was entered.
#  If no odd number was entered, say so.


n = 0
max_n = 10
old_max = 'i am a string'
while(n < max_n):
    #   print "Enter integer #",n,": "
    new_num = raw_input("Enter value #"+str(n)+": ")
    if(old_max) == 'i am a string':
        old_max = int(new_num)
        #   print 'caught the first time!'
    elif int(new_num) % 2 == 1 and int(new_num) > old_max:
        old_max = int(new_num)
    n=n+1
print old_max




