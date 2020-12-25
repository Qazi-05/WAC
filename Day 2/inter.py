#while loop

# i = 0 # start

# while i < 5 : #condition
#     print(i)
#     i = i + 1 # increment

# for i in range (1, 20, 2) :
#     print (i)
# for i in range (19, 1, -2) :
#     print (i)

# Sum of n natural numbers

# n = int(input("Enter a number :"))

# k = 0 
# for i in range (1, n+1):
#     k += i
# print ("the sum is : ", k)

# #Factorial

# n = int(input("Enter a number :"))

# p = 1 
# for i in range(1,n+1):
#     p = p*i 
# print("The factorial is :", p)

#to swap a number 
# a, b = 5, 10
# print (a)
# print(b)
# a, b = b, a
# print(a)
# print(b)

#Nested loops
# for i in range(5):
#     for j in range (5):
#         print(i, end=' ')
#     print()


# 1. star pattern
'''
n = 5

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

#code

#n = int(input("Enter a number :"))

# for i in range(n+1):
#     for j in range(n+1):
#         print("*" , end ='   ')
#     print()

# for i in range(n):
#     print('* '*n)

'''
n = 4
*
* *
* * *
* * * *

'''

#CODE

#n = int(input("Enter a number :"))

# for i in range (n+1):
#     for j in range (i+1):
#         print("*", end=' ')
#     print()

# for i in range(n):
#     print('* ' * (i+1))

'''

BREAK AND CONTINUE STATEMENTS

'''

# for i in range (10):
#     if i == 7 :
#         break # loop existing statement
#     print(i)


# for i in range(10):
#     if i%2 == 0 :
#         continue # Loop skipping statement
#     print (i)
 
# for i in range (10):
#     if i%2 == 0 :
#         continue # Loop skipping statement
#     if i == 7 :
#         break # loop existing statement
    
#     print(i)

# 3. ENTERED NUMBER PRIME OR NOT

# n = int(input("Eneter a number :"))
# k = 0
# for i in range(1, n+1):
#     if n%i == 0 :
#         k += 1
# if k > 2 :
#         print("It is not a prime number :")
# else :
#         print ("It is a prime number")

# PRINT PRIME NUMBERS FROM 1 TO N

# n = int(input("Enter a number :"))

# print("The list of prime numbers are :")
# k = 0
# for i in range(2, n) :
#     if i > 1 :
#         for j in range (2, i):
#             if (i % j == 0):
#                 break
#         else :
#             print (i)
'''
strip()  : deletes the starting and ending spaces
split()  : it splits the string on the basis of characters provided
'''
s = '    today is a good day!!'      
print(s)
print(s.strip())
print(s.strip().split('a'))
    

