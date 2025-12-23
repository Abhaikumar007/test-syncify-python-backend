"""
NOTES
 -  List is an ordered collection of elements
 -  List is mutable (changeable elementst)
 -  List allows duplicate values
 -  List can store multiple data types
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

#ADDING ELEMENTS TO LIST.

"""
- append() adds element at the end
- insert(index,value) adds element at specific position


 if we try to insert at index which we don't have in list it will add the value at the
 end

BUCKETS
    - add element in list
        (insert(index,value), append()- adds at the end) .extend() -> used to add two lists
    - removing elements from list
        (remove(value) , pop() removes and returns the last element, and also pop(index) removes the element at index and return it
        .clear() method used to remove every item.or empty the list,) del will just remove the list from the memory itself     - length of the list
        len() returns number of elements in the list
    - sorting list
            sort() in ascending order
            sort(reverse=True) #descending order
            works only if the elements are cmpareables
    - count,index
"""

nums.insert(2,200)
#if we try to insert at the index which we don't have in list then it will add value at the
#end
print("Insert ---->",nums)
nums.insert(20,200) #it will add value at the end as we have max index in the list is 3
print("Insert ---->",nums)


try:
    nums.remove(3000) #removes a specific value
except:
    print("It will throw an error ")
print(nums)


#pop - removes the last element and returns the last element
last_item=nums.pop()
print(last_item)
print(nums)
#pop(index) - removes the element from the index ..and then return that popped item
removed_item=nums.pop(0)
print(removed_item)
print(nums)

#clear
temp_list=[1,2,3]
temp_list.clear()
print(temp_list)

nums2=[4,2,7,1]
nums2.sort()
print("Sorted list:",nums2)

nums2.sort(reverse=True)
print(nums2)


#revesr the order of elements..
#does not sort the list
nums2.revese()
print(nums2)


del nums2  #remove it from the memory
del nums_del[1:3] #it can do slicing too but it will delete from the entirely
del nums_del[1] #remove the first index from the memory itself


.sort() #does not return a value it will change the original list
sorted() # does return a new list  and it works on any iterable like list tuple string set etc


#There is a different one like copying list (REFERENCE VS COPY)
#SO WHAT REFERENCING DOES IS THAT
a=[1,2,3,4]
b=a
#whenever we change anything on b then it will get affected in a too
#so like if we append a value into b
b.append(5)
#then it will just reflect that change on a too

#a.copy()
c=a.copy()
c.append(6)
#this is where it will just create the copy of that but doesn't get any reflection of change

#HOMEWORK
#shallow copy and deep copy
"""

shallow copy - creates a new outer objecrt but references the same inner objects
deepcopy - creates a new outer object and new inner objets

"""
#in and not in (member ship operator)

#LIST CONCATENATION

 """
 lists=[1,23,4]
 lists2=[1,333,3,5]
  lists+lists2
  #lists.extend() is used to add elements of another iterable to the same list..
  concatenation is used to join two lists to create new lists
 """


nums_count=[1,2,2,3,2,4]
print(nums_count.count(2))
#used to count the number of items in that list ..okay


#then there is .index()
#used to find the index  of a particular value then you can find it out
fruits=["apple","banana","cherry"]
print(fruits.index("banana")) #which index it exist

"""
NESTED LIST #basically list inside another list
 matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]
 print(matrix)

"""
#LIST COMPREHENSION

squares=[i*i fo i in range(1,6)]

#BUILT IN FUNCTIONS
nums4=[10,20,30]
print(sums(nums4))
print(max(nums4))
print(min(nums4))

#ANY() AND all()
nums5=[2,4,6,8]
print(all(i %2 ==0 for i in nums5)) #
print(any(i > 5 for i in nums5))

nums5=[2,4,6,8]
print(all(i%2==0  for i in nums5))
print(any(i >5 for i in nums5))


marks=[5,90,78,92]
total=sum(marks)
average=total/len(marks)
print(total,average)

cart=["Milk","Bread","Eggs"]
cart.append("Butter")
cart.remove("Bread")
print(cart)

tasks=[]
tasks.append("Learn Python")
tasks.append("Practice Coding")
tasks.append("Build Project")
print(tasks)


#TUPLE
