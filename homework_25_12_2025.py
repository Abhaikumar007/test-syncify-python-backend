
"""
BUILT IN METHODS
"""
#count()	Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)





#index()	Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)


#once you change the tuple address but it does not change the value at t..what will happend
t = (1, 2, 3)
print(id(t))
#since t will get a new address with the values

t = (1, 2, 3, 4)
print(id(t))






"""
1️⃣ =

Simple assignment

x = 10

2️⃣ +=

Add and assign

x = 5
x += 3   # x = x + 3

3️⃣ -=

Subtract and assign

x = 10
x -= 4   # x = x - 4

4️⃣ *=

Multiply and assign

x = 4
x *= 2   # x = x * 2

5️⃣ /=

Divide and assign (float result)

x = 8
x /= 2   # x = 4.0

6️⃣ //=

Floor divide and assign

x = 9
x //= 2  # x = 4

7️⃣ %=

Modulus and assign

x = 10
x %= 3   # x = 1

8️⃣ **=

Power and assign

x = 2
x **= 3  # x = 8

9️⃣ &=

Bitwise AND and assign

x = 5     # 101
x &= 3    # 011 → x = 1

🔟 |=

Bitwise OR and assign

x = 5     # 101
x |= 3    # 111 → x = 7

1️⃣1️⃣ ^=

Bitwise XOR and assign

x = 5     # 101
x ^= 3    # 110 → x = 6

1️⃣2️⃣ <<=

Left shift and assign

x = 2     # 10
x <<= 1   # 100 → x = 4

1️⃣3️⃣ >>=

Right shift and assign

x = 4     # 100
x >>= 1   # 10 → x = 2

"""

"""
3.MEMBERSHIP OPERATORS

in =>

not in =>
"""

"""
4.Shallow COPY AND DEEP COPY
shallow copy - it just creates a new object by copying the Referencing
it  does not copy nested objects..

changes to nested objects affect both that copies


Deep COPY
it creates a new object and recursively copies all nested objects.
method: .deepcopy(original)
that the changes do not affect the original..

"""

"""
Referencing

a = [1, 2, 3]
b = a
b.append(4)
print(a) #[1,2,3,4]
a and b refer to the same list



Copy
copy creates a new object
b=[1,2,3]
b=a.copy()
b.append(4)
print(a) #[1,2,3]
print(b) #[1,2,3,4]
"""

"""
List comprehension

squares = [i * i for i in range(5)]
# you can also use if

squares=[i  for i in range(5) if i not in [1,2,3]]
#output =[0,4]
#you can use if else

print([i if i not in [0,1,2,3] else None for i in range(5) ])
#output=[None,none,none,none,4]

"""
"""
Range

range(start, stop, step)
range(5) #0,1,2,3,4
range(1,10,2) #1, 3,5,7,9

print(list(range(0,10,2))) #[0, 2, 4, 6, 8]

"""


"""
Built in methods
len([1,2,3])      # 3
sum([1,2,3])      # 6
max([1,2,3])      # 3
min([1,2,3])      # 1
zip([1,2], [3,4]) #used to zip it as (1,3) and (2,4)
and there is another function called
map function used to
 -map() applies the function to every element
 -It does not remove elements

 filter function
"""
