
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
