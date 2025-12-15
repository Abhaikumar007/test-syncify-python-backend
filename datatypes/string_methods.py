


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
#checks if it is only  a digit or not
is_alnum=word.isalnum()
#check if it is only  alphanumeric ..like letters+ digits,no special characters,

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
