"""
1.Numeic Types
int -> integer numbers(10,-5,0)
float -> decimal numbers(3.14,-0.5)
complex -> complex numbers (2+3j)
2.String Types


2.Boolean Types
bool -> True or False

3. Text Type
str-> string(text)

4.Sequence Types

list-> ordered,changeable list
tuple -> ordered,unchangable list

5.Set Types

set -> unordered unique values {}

6.Mapping Type

dict -> key value pairs
"""

a=10
b=-20
c=0
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

print(a/b) #3.33
print(a//b) #3
# / nomal division
# // - cut off the decimal part
print(a%b)
# % gives remainder after division
#Example: 10/3 is 3 with remainder 1 -> % gives 1.

#power (Exponent)
print(a**b) #10**3=10000


#COMPARISON OPERATORS

x=10
y=20
print(x==y)
print(x!=y)
print(x >y)
print(x<y)
print(x >=10)
print( y <=20)


#TYPE CONVERSION

f1=3.9
f2=5.1

print(int(f1))
print(int(f2))
s1='10'
s2='250'
print(int(s1))
print(int(s2))

x=2.14
y=-2.5
z=0.0
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

a=5.5
b=2.0
print(a+b) #7.5
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

p=10 #int
q=3.5 #float
print(p+q)
print(p*q )
print(p/q)


#BUILT IN FUNCTIONS AND USEFUL THINGS

#type() #to check data type

val=4.75
print(type(val))

#float()

print(float(7)) # 7.0
print(float("2.25")) #2.25

#round() - to round float values
pi=3.1455345
print(round(pi)) #3
print(round(pi,2)) #3.14
print(round(pi,3)) #3.145

#example floating point precision issue
print(0.1+0.2) #0.3000000004(small percision error)
print(round(0.1+0.2,2)) #0.3



"""
# COMPLEX NUMBERS (complex) IN PYTHON

# Complex number: a + bj
# a → real part (int or float)
# b → imaginary part (int or float)
# j → imaginary unit (√-1)

# Creating complex numbers

z1 = 2 + 3j       # real = 2, imaginary = 3
z2 = -1 - 4j
z3 = 5.0 + 0j     # real part float
z4 = 0 + 2j       # only imaginary

print(z1, z2, z3, z4)

# Check data type
print(type(z1))   # <class 'complex'>

# Accessing real and imaginary parts
print(z1.real)    # 2.0
print(z1.imag)    # 3.0

print(z2.real)    # -1.0
print(z2.imag)    # -4.0


# ----- BASIC OPERATIONS WITH COMPLEX NUMBERS ----- #

a = 2 + 3j
b = 1 - 4j

# Addition
print(a + b)    # (3-1j)

# Subtraction
print(a - b)    # (1+7j)

# Multiplication
print(a * b)    # (14-5j)

# Division
print(a / b)    # ( -0.5882352941176471 + 0.6470588235294118j ) approx


# Conjugate of a complex number
# For z = a + bj, conjugate is a - bj
z = 3 + 4j
print(z.conjugate())    # (3-4j)


# Magnitude (absolute value / modulus)
# |z| = √(a² + b²)
# In Python: use abs()
print(abs(z))   # 5.0  (because √(3² + 4²) = 5)


# Creating complex numbers using complex() function

# complex(real, imag) - Typecast/Type Conversion to complex number
c1 = complex(2, 3)      # 2 + 3j
c2 = complex(5, -1)     # 5 - 1j
c3 = complex(7)         # 7 + 0j
c4 = complex("2+3j")    # from string

print(c1, c2, c3, c4)
print(type(c4))         # <class 'complex'>


# Mixing with int and float

x = 5          # int
y = 2.5        # float
z = 3 + 4j     # complex

print(x + z)   # (8+4j)
print(y + z)   # (5.5+4j)

# Note: if you mix int/float with complex, result becomes complex


# Using complex numbers in simple examples

# Example 1: Electrical engineering (impedance)
r = 4          # resistance (real part)
x_react = 3    # reactance (imaginary part)
impedance = complex(r, x_react)   # 4 + 3j
print("Impedance:", impedance)

# Example 2: Distance from origin in complex plane
point = 3 + 4j
distance = abs(point)   # same as sqrt(3^2 + 4^2)
print("Distance from origin:", distance)  # 5.0
"""



name="John Doe"
city="Mumbai"
message='Hello World'
quote='Python is awesome'

#Both work the same
print(name)
print(message)



#END is used to what come after ending a word if two words are used..
#print("hello",end=" ")
#print("world") will give you hello world




#When to use which quotes ?
#Use single quptes inside double quotes
sentence1="Python's syntax is easy"
print(sentence1)
sentence2='He sad "Python is great"'
print(sentence2)

#index bucket
len(sentence2) #used to find the length
sample_str="Hello"
first_char=sample_str[0]
second_char=sample_str[1]
thid_char=sample_str[2]
fourth_char=sample_str[3]
last_char=sample_str[4]
print("First Character :",first_char)
print("Second Character :",second_char)
print("Third Character :",third_char)
print("Fourth Character :",fourth_char)
print("Last Character :",last_char)

first_char=sample_str[-1]
second_char=sample_str[-2]
thid_char=sample_str[-3]
fourth_char=sample_str[-4]
last_char=sample_str[-5]
print("First Character :",first_char)
print("Second Character :",second_char)
print("Third Character :",third_char)
print("Fourth Character :",fourth_char)
print("Last Character :",last_char)

#CASE BUCKET
sample_str="hello WORLD"

upper_str=sample_str.upper()
print("Upper Case: ",upper_str)

lower_str=sample_str.lower()
print("Lower Case: ",lower_str)

title_str=sample_str.title() #Title is used to conver into title
print("Ttile Case: ",title_str) #Hello World like how a title would be displayed a string like hello World would be displayed as Hello and

capitalized_str=sample_str.capitalize()

#Fully capitalize it .. only capitalize the first word is capital


#REMOVING WHITESPACE BUCKET
whitespace_str="        Hello       world "
stripped_str=whitespace_str.strip()
print("REMOING BOTH LSTRIUP AND RSTRIP FROM THE STRING .. ",stripped_str)
#Most commonly used

leading_str=whitespace_str.lstrip()
print("eadeing whitespace_str is removed: ",leading_str)
trailing_str=whitespace_str.rstrip()
print("Preceding whitespaces are removed: ",trailing_str)










#FINDING SUBSTRNG

main_str="Hello welcome to my coding journey."
"""
It is case sensitive
"""

first_index=main_str.find("hello")
#first occurence of hello..and if not find then it wil give -1


replaced_str-main_str.replace("hello","hi")
print("Replaced String:",replaced_str)


"""
BUCKETS
1. INDEX
2. CASE
3. WHITESPACE REMOVE
4. SUBSTRNG
5. CHECK IF STRING IS TRUE OR FALSE
  3 methods
  2 methods
6.Splitting and joining strings
7.startswith() and endswith() methods
8.Count
"""
word="python123"

print("Is alphabetic",word2.is_alpha())
#checks if it is only alphabets or not.
is_numeric=word.isdigit()
print("Is numeric:")
#checks if it is a digit or not
is_alnum=word.isalnum()
#check if it is alphanumeric ..like letters+ digits,no special characters,

#second bucket
.islower() #checks if it is lower
 .isupper() #checks if it is upper

#third bucket
#if any whitespace are there in the string then it will return true..
#
#\t \n also whitespaces
.isspace()

#COMMON INTUITIVE THOUGHT WOULD BE THAT IT WILL RETURN TRUE IF THE WORD MEANING ALIGNS WITH THE
#STRING THAT WE ARE PROVIDING
"""
special exanmples ->
.isupper()
  "HELLO123"  true all alphabets uppercase
  "Hello123"  false lowercase exists
  "12345"     false no alphabets
  "HELLO!!"   True  Symbols ignored

  ** same woks for .islower()

"""



#SPLITTING CASE
.split(" ") #which will split the word into a list ..
#it has a default value " "
#it has a parameter tat is used ..using cmma as a sperator.

"""
" ".join([]) -> takes a list and then join it


containing
"""




#STARTS WITH ENDS WITH CASE
test_str="Hello welcome to python programming"
#startswith if it startswith that specific word
test_str.startswith()
test_str.endswith()


#Count CASE BUCKET

count_str="Python is great.Python is dyanmaic .Python is easy to learn."

#count occurence of that substring "Python"
#here there is 3 Python so it will return 3



#SLICING
#SLICING IS WHERE THE WORD IS SLICED BASED ON THE INDEX AND IT IS USED TO ACTUALLLY
#LAST INDEX IS NOT INCLUDED
#DEFAULT STARTS WITH 0 AND ENDS WITH LENGTH OF STRING
#VAR[0:5]
slicing_str="pythonprogramming"
slicing_str[0:5] #pytho

slice_str[:6] #python
slice_str[6:]#programming
slice_str[:] #it will just generate the entire word
#Extracting substring using negative indexing
substring2=slice_str[-4:-1] #min


#CONCATENATION
#used to join two or more string into a single string

str1="Hello"
str2="World"
print(str1+str2) #uses '+' as a identifier to combine two words
#this will work only for strings but not for numbers ..for numbers it will add.

#we can use '*' to multiply the strings .
print(str1*2) # will give you hellohello



#sting with numbers
age=25
#we can use 3 solutions to combine strings and numbers

#- concatenation by type casting str(age)

# - using comma in print it will just give you print("Age is", age)

#using f-strings is used to combine strings and numbers together.for concatenation
#f"hello{age}"
MESSAGE="we can make sure everything is perfect"
print(MESSAGE)
name="Abhai"
email_bdy=f"""
    Hi,{name} nice to meet you{MESSAGE}
"""
print(email_bdy)
