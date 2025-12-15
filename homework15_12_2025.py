#based on comparison with boolean conditions
marks = 55
if marks>=50:
    print("Pass")
else:
    print("Fail")


year=2000
if(year >=2015):
    #oif the year is greater than 2015 then he will be termed as gen alpha

    print("You are gen alpha")
elif(year >= 2000):
    print("You are genz")
else:
    print("You are a millenial")
#just some random values i put it in


internet_connected = False
#if its not False hich is True then it says the internet is not connected..
if not internet_connected:
    print("No internet")
else:
    print("Connected and the ip is 128.0.0.1")



#WORKING WITH STRINGS
name = "Abhai"

if name == "Abhai":
    print("Name matched")



password = "1234"
#THIS WORKS LIKE IF THE PASSWORD IS NOT ADMIN THEN IT SAYS WRONG PASSWORD
if password != "admin":
    print("Wrong password")
