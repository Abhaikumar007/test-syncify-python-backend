
"""
print("Myself Pratik")
print("i AM FORM MUMBAI")
print("I like to play football")
print("I like to travel")
"""
'''
print("Myself Pratik")
print("i AM FORM MUMBAI")
print("I like to play football")
print("I like to travel")
'''
name="Pratik"
print(name)
num=25
print(num)
name="John"
Name="Jane"
NAME="Jack"
print(name)
print(Name)
print(NAME)
"""""
1.RULES (Must Follow - Otherwise Error):

   ✓ Can contain: letters (a-z, A-Z), digits (0-9), underscore (_)
   ✓ Must start with: letter or underscore
   ✓ Cannot start with: digit/number
   ✓ Cannot contain: spaces or special characters (@, #, $, %, etc.)
   ✓ Cannot use: Python keywords (reserved words)

2. Valid Examples:
   name, age, first_name, _value, student1, total_marks

3. Invalid Examples:
   2name          → Starts with number ✗
   first-name     → Contains hyphen ✗
   first name     → Contains space ✗
   @username      → Contains special character ✗
   for            → Python keyword ✗

4. Case Sensitivity:
   - Python treats these as DIFFERENT variables:
     name, Name, NAME, nAme
   - Be consistent with capitalization

5. Python Keywords (Cannot use as variable names):
   and, as, assert, break, class, continue, def, del, elif, else,
   except, False, finally, for, from, global, if, import, in, is,
   lambda, None, nonlocal, not, or, pass, raise, return, True, try,
   while, with, yield

6. BEST PRACTICES (Conventions):

   ✓ Use descriptive names: age (good), a (bad)
   ✓ Use lowercase: name (good), NAME (avoid for variables)
   ✓ Use underscore for multiple words: first_name (good), firstname (okay)
   ✓ Don't use single letters except for: i, j, k (in loops)

   Naming Convention: snake_case
   Examples: student_name, total_marks, user_age

7. Examples of Good vs Bad names:

   Good Names          Bad Names
   ---------           ---------
   student_age         sa
   total_price         tp
   first_name          x
   is_valid            v
   user_count          count1

name = "Pratik"
# VALID variable names
name = "John"
age = 25
first_name = "John"
last_name = "Doe"
age2 = 30
_private = "secret"
student_roll_number = 101

# INVALID variable names (These will give errors - show but don't run)
# 2age = 25              # Cannot start with number
# first-name = "John"    # Cannot use hyphen
# first name = "John"    # Cannot have space
# for = 5                # Cannot use Python keywords
# @name = "John"         # Cannot use special characters

"""


a=2
b=3
c=2
a=b-c-2
print(a)
print(b)
#assign different data type values to multiple variables
name,age,email="Pratik",23,"abc@gmail.com"
print(age)
print(name)
print(email)
#swapping
a="Pratik"
b="Aasim"
print(a)
