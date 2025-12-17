#IMMUTABILITY PROBLEM
string="AbhaiKumar"
print(string[0]) #output is A
#lets change the string
# strings[0] ="a"
"""
NameError: name 'strings' is not defined. Did you mean: 'string'?
"""

#REVERSING OF LIST
string_list=["m","a","l","a","y","a","l","a","m"]
print(string_list[::-1])#malayalam
print(string_list[::-2])#mlylm

#PRACTICE
name="John Doe"
checklist="thirty one"
id='1230'
check=False
if(name.strip().lower()[1]=='j'):
    print("his name starts with j")
    check=True
elif name.lower().startswith('j'):
    print("his name does definetly start with j")
    check=True
else:
    print("his name does not start with j")
if(check and id.isdigit()):
    print(f"{name} has an id {id}","he is permitted", sep="-->")
checklist=checklist.split(" ")
print(31)
