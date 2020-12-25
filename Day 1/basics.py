#print( 'today', 'is', 'the', 'first' , sep='-')
#print("hello",end= ' ')
#print ("world")
'''
multi line
comment
'''

#taking input

# n = input ("Enter your name :")
# print(n)

# variables and data types
# a = 15  #int
# print(a)
# print(type(a)) # type function is used to print type of variable

# b = 10.2   #float
# print(b)
# print(type(b))

# c = True # boolean
# print (c)
# print (type(c))

# d = "today is a sunny day"  #str
# print(d)
# print(type(d))
'''
sum = +
substarct = -
mul = *
Div = /
integer div = //
modulo = %
power = **
'''

# a= 5
# b= 3
# print("sum is", a+b)
# print("sub is", a-b)
# print("mul is ",a*b)
# print(" div id ",a/b)
# print("remainder is ",a%b)
# print(" int div is ",a//b)

# s = "today"
# print (5*s)

'''
Logical Operators
#OR
#AND
#NOT
'''
#logical Operators

# Comparison operators


'''


if condition :
    statement (consider)
elif condition :
else:
    statement(consider)
statement(not consider)

'''
# n=18
# if n > 10 :
#     print("larger")
# else :
#     print("smaller")

# n = int(input("Enter a number :"))
# if n%3 == 0 :
#     print("zero")
# elif n%3 == 1 :
#     print("one")
# else :
#     print("two")

# n = int(input("Enter a number :"))
# if n%3 == 0 and n%5 == 0 :
#     print("FIZZ AND BUZZ")
# elif n%3 == 0 :
#     print("FIZZ")
# elif n%5 == 0 :
#     print("BUZZ")
# else :
#     print("The Number is :",n)

#CALCULATOR
# print("For sum enter 1")
# print("For sub enter 2")
# print("For mul enter 3 ")
# print("For div enter 4 ")
# print("For remainder enter 5 ")
# print("For int div enter 6 ",)

# n = int (input("Enter the choice :"))
# if n > 7 :
#     print ("WRONG CHOICE ENTERED")
    
# a = int(input("Enter 1st Number :"))
# b = int(input("Enter 2nd Number :"))
# if n == 1:
#     print(a+b)
# if n == 2:
#     print(a-b)
# if n == 3:
#     print(a*b)
# if n == 4:
#     print(a/b)
# if n == 5:
#     print(a%b)
# if n == 6:
#     print(a//b)

# leap year

# n = int(input("Enter a year"))

# if n < 0 :
#     print("Enter a valid year")
# else :
#     print("Valid year entered")
#     if n%400 == 0 :
#         print("Leap Year")
#     elif n% 100 == 0:
#         print ("Not a Leap Year")
#     elif n%4 == 0 :
#         print("Leap Year")
#     else :
#         print("Not a Leap Year")

# '''
# loops

# #for
# #while

# '''
# i=0 #counter
# while i<10 : #condition
#     print('Hello')
#     i = i+1 #step size
# print('world')

# print(list(range(5, 10, 2)))

# for i in range (2 ,10,2):
#     print(i)

#1.table
n = int(input("enter a number :"))

for i in range (1,11):
    print(n*i)