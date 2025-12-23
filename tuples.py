"""
    q)Why tuple is faster than the list?

        - Tuple is an ordered collection of elements
        - Tuple is immutable ( cannot be changed after creation)
        - Tuple allows duplicate values
        - Tuple can store multiple data types
        - Tuple is written using paranthesis()
         - Tuples are faster than lists
         - TUples use less memory than lists
         - Tuples can be used as dictionary keys(lists cannot)
"""
#** #SINGLE ELEMENT TUPLE(IMPORTANT)
"""
Notes:
 - Single element tuple MUST have trailing comma
 - Without comma, its' just a value in paranthesis , not a tuple

"""

single_tuple=(5,) #single value is also a tuple ..it should contain a , after that
not_a_tuple=(5) #not a tuple but an integer
print(type(single_tuple))


#**Tuple without parameters
packed_tuple=1,2,3,4
print("\n Tuple created without paranthesis:",packed_tuple)
#==================================================================================
# TUPLE (tuple) DATA TYPE IN PYTHON
#==================================================================================
"""
NOTES:
- Tuple is an ordered collection of elements
- Tuple is IMMUTABLE (cannot be changed after creation)
- Tuple allows duplicate values
- Tuple can store multiple data types
- Tuple is written using parentheses ()
- Tuples are faster than lists
- Tuples use less memory than lists
- Tuples can be used as dictionary keys (lists cannot)
"""

# Creating tuples
numbers_tuple = (1, 2, 3, 4, 5)
names_tuple = ("Alice", "Bob", "Charlie")
mixed_tuple = (1, "Python", 3.14, True, [1, 2], {"name": "John"})

print("Numbers tuple:", numbers_tuple)
print("Names tuple:", names_tuple)
print("Mixed tuple:", mixed_tuple)

# Check data type
print("Type of numbers_tuple:", type(numbers_tuple))

# Tuple with duplicates (allowed)
duplicate_tuple = (1, 2, 2, 3, 3, 3, 4)
print("Tuple with duplicates:", duplicate_tuple)

#==================================================================================
# SINGLE ELEMENT TUPLE (IMPORTANT!)
#==================================================================================
"""
NOTES:
- Single element tuple MUST have trailing comma
- Without comma, it's just a value in parentheses, not a tuple
- This is a common mistake for beginners
"""

# Correct single element tuple
single_tuple = (5,)
print("\nSingle element tuple:", single_tuple)
print("Type:", type(single_tuple))

# Wrong - this is NOT a tuple
not_a_tuple = (5)
print("Not a tuple (just integer):", not_a_tuple)
print("Type:", type(not_a_tuple))

# Single element with trailing comma
single_string_tuple = ("hello",)
print("Single string tuple:", single_string_tuple)
print("Type:", type(single_string_tuple))

#==================================================================================
# TUPLE WITHOUT PARENTHESES (TUPLE PACKING)
#==================================================================================
"""
NOTES:
- Tuples can be created without parentheses (tuple packing)
- Comma makes it a tuple, not parentheses
- Parentheses are optional but recommended for clarity
"""

# Tuple without parentheses
packed_tuple = 1, 2, 3, 4
print("\nTuple created without parentheses:", packed_tuple)
print("Type:", type(packed_tuple))

# Single element without parentheses
single_packed = 5,
print("Single element tuple without parentheses:", single_packed)
print("Type:", type(single_packed))

#==================================================================================
# EMPTY TUPLE
#==================================================================================
"""
NOTES:
- Empty tuple is created with empty parentheses ()
- Less common than empty lists since tuples are immutable
"""

empty_tuple = ()
print("\nEmpty tuple:", empty_tuple)
print("Type:", type(empty_tuple))
print("Length of empty tuple:", len(empty_tuple))

#==================================================================================
# TUPLE INDEXING
#==================================================================================
"""
NOTES:
- Tuple is a sequence type like lists
- Indexing starts from 0
- Positive index: access from start
- Negative index: access from end
"""

sample_tuple = ("a", "b", "c", "d", "e")
print("\nSample tuple:", sample_tuple)
print("First element [0]:", sample_tuple[0])
print("Second element [1]:", sample_tuple[1])
print("Last element [4]:", sample_tuple[4])

# Negative indexing
print("Last element [-1]:", sample_tuple[-1])
print("Second last element [-2]:", sample_tuple[-2])
print("First element using negative index [-5]:", sample_tuple[-5])

# Index out of range error
# print(sample_tuple[10])  # IndexError: tuple index out of range

#==================================================================================
# LENGTH OF TUPLE
#==================================================================================
"""
NOTES:
- len() returns number of elements in the tuple
- Counts all elements including duplicates
"""

my_tuple = (10, 20, 30, 40, 50)
print("\nTuple:", my_tuple)
print("Length of tuple:", len(my_tuple))

duplicate_tuple = (1, 1, 2, 2, 3, 3)
print("Tuple with duplicates:", duplicate_tuple)
print("Length (counts duplicates):", len(duplicate_tuple))

#==================================================================================
# TUPLE SLICING
#==================================================================================
"""
NOTES:
- Slicing extracts part of the tuple
- Returns a new tuple
- Last index is NOT included
- Syntax: tuple[start:end:step]
- Original tuple remains unchanged
"""

print("\nSample tuple for slicing:", sample_tuple)
print("Elements [0:3]:", sample_tuple[0:3])
print("Elements [:3]:", sample_tuple[:3])
print("Elements [2:]:", sample_tuple[2:])
print("All elements [:]:", sample_tuple[:])
print("Elements [-3:-1]:", sample_tuple[-3:-1])
print("Every second element [::2]:", sample_tuple[::2])
print("Elements with step 2 [1:5:2]:", sample_tuple[1:5:2])

# Reverse tuple using slicing
print("Reversed tuple [::-1]:", sample_tuple[::-1])
print("Reverse with step 2 [::-2]:", sample_tuple[::-2])
"""
Notes :

- Immutability makes tuples faster and more efficeint
"""
immutable_tuple=(10,20,30)
print("\n original tuple: ",immutable_tuple)
#provides Type Error

#----------------------------
#"Tuple with mutable elements"
#-----------------------------

"""
 - Tuple allows mutable objects like list ..that can be modified.
 - Important distinciton in python.

"""
tuple_with_list=(1,2,[3,4,5])
print("\n tuple with list inside:",tuple_with_list)
tuple_with_list[2].append(6)

tuple_with_list[2][0]=999
print("After modifying list inside tuple",tuple_with_list)
#HOMEWORK
#all built in methods of that idea of tuple_with_list
#WHAT ARE THE ASSIGNMENT OPERATORS..
# @once you change the tuple address but it does not change the value at t..what will happend


"""
TUPLE CONCATENATION
 -can combine tuples using + operator
 - creates a new tuple
 - original tuples remain unchanged
 - cannot use += on tuple variable (creates new tuple)


 LIST CONCATENATION AND TUPLE CONCATENATION
  - for computer it has an address
  - list1=list1+list2
"""


#Multiple concatenation
tuple3=(7,8)

combined=tuple1+tuple2+tuple3
print("combining three tuples",combied)
tuple_x=(1,2)
print("original tuple_x",tuple_x)
tuple_x+=(3,4)
print("After tuple x+=(3,4)",tuple_x)
print("ID of new tuple_x (differmt)",id(tuple_x))
print("Note: +=creates a new tuple doesn't modify original")
