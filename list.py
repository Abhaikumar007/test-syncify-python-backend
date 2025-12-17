"""
NOTES
 -  List is an ordered collection of elements
 -  List is mutable (changeable elementst)
 -  List allows duplicate values
 -  List can stoer multiple data types
 -  List is writtend using square bracketts []

"""

#Creating lists
numbers=[1,2,3,4,5]
names=["Alice","Bob","Charlie"]
mixed_list=[1,"Python",3.14,True]
print(numbers)
print(names)
print(mixed_list)

#chck data type
print(type(numbers)) #lists

#List indexing

"""
- List is a sequence type
- Indexing starts from 0
- Use positive index from start
- Use negative index from end
"""
sample_list=["a","b","c","d","e"]



print(sample_list[0]) #a

pint(sample_list[-1]) #e
print(sample_list[-2]) #d

#Step in slicing
print(sample_list[0:5:2]) #['a','c','e']
print(sample_list[::2]) #['a','c','e']
print(sample_list[:5:3]) #['a','d']

#Negative step ==>V V IMPORTANT
#REVERSE THE LIST
print(sample_list[::-1])
print(sample_list[::-2]) #['e','c','a']

#List SLICING

#it works same like indexing strings
#it can take list of negative indexing too..
#so 0:3 will give you upto 2nd index.


"""
- Mutable means elements can be modified
- Unlike strings, lists allow item assignemnt
"""

nums=[10,20,30]
nums[0]=100
nums[1]=200
print(nums) #[100,200,30]

#REVERSING OF LIST FOR THE STRING..JUST SIMILAR.
#THIRD PRACTICE EVERYTHING..
#IMMUTABILITY OF THE STRING..IF YOU FIND THE ERROR..THEN MENTION THAT ERROR IN COMMENTS..
