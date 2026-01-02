"""
DICTIONARY
    - must be unique
    - whenever we access elements ..the key should be unique
    - very fast lookup o(1) using a key (keys are unique)
    - keys must be immutable



    - dict() constructor can take keyword arguments


"""
student={"name":"Alice","age":20,(1,2,3):"Tuplevalue"}
#Two ways to create a dictionary

empty_dict={} #empty curly braces
empty_dict2=dict()

person=dict(name="Bob",age=30,city="New York")

"""
Valid keys:
    stirng,number,tuple(with immutable elements )
    Invalid Keys: List,dict, set(mutale type)
"""
#tuple should be hashable ..
"""
ACCESSING DICTIONARY VALUES
    - keys in square brackets
        print("Name",student["name"])
        - key error if it doesn't exist
    -get() method
        #searches the key 'phone' and if it didn't find then it will substitute with
        #the new value
            -actually default value is None if there wasn't provided
        student.get("phone", "Not available")
        difference between keysin square brackets:
ADD SINGLE VALUE
    -KEYS IN SQUARE BRACKET AND THEN ASSINGMENT OPERATOR AND THEN THE VALUE
    -update() -to add multiple key:value pairs

- len() - used to find the number of keys in the dictionary

"""
"""
removing

    -pop(key) removes and returns values and raises Key error ..if not found
    -pop(key,default) -> removes and returns a value and if it didn't find then it gives default..okay?
    

"""
