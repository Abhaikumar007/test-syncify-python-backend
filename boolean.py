a=10
b=20
print(a==b) #false
print(a!=b) #True
print(a > b) #False
print(a < b) #True
print(b <=20) #True

# ---Boolean from logical operators ----#
#AND operators
#True only if BOTH conditions are True
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False


print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

print(not True) #False
print(not False)  #True

age=19
if age >=18:
        print("You are eligible to vote")
else:
     print("You are not eligible to vote")
#Truthy and Falsy values..

#all the numbers excluding 0 are truthy values ..
#string or space is still truthy values..
#List,Tuples,dictionary are also truthy values if something is contained in that..
print(bool(True))
print(bool(1))
print(bool(-1))
print(bool("Hello"))
print(bool([1,2]))

#Falsy values ..
#0 or 0.0 are falsy values
#empty set is als a falsy value and empty liust,tuples,dictionary etc are all falsy.
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(None))


"""
THE VARIOUS METHODS USED IN PYTHON

"""
.islower()      # all letters are lowercase
.isupper()      # all letters are uppercase
.isalpha()      # only letters
.isalnum()      # letters + numbers (no symbols)
.isdigit()      # only digits (0–9)
.isnumeric()    # numeric characters (includes fractions, superscripts)
.isdecimal()    # decimal digits only
.isspace()      # only whitespace
.istitle()      # Title Case (First Letter Capital)
.isascii()      # only ASCII characters
.isprintable()  # printable characters only

#Homework 1 htis is how boolean condition works for if else conditions.
#3-5 CONDITIONS.. REAL EXAMPLES ..
#admin=101
#hr =102
#employee1=201
#employee2=202
#id=???

#COMPARISON OPERATORS WITH STRING..
#NOTES
#2.how  comparison operator work with string.
