'''value_1 = 45
value_2 = 90

if value_1 > value_2:
    print("Eyooo Value 2 is bigger")
else:
    #This code above would not be able to run because nothing is following the else statement and indicates 3 errors'''

def placeholder():
    return

value_1 = 45
value_2 = 90

if value_1 > value_2:
    print("I am schmol")
elif value_2 > value_1:
    print("I am thicker than 1")
else:
    print("Statement after ifs")

print("statement after if")
#Here we will get the following output
#I am thicker than 1
#statement after if
#IF WE SWITCH THE DIRECTION OF VALUE_1 TO VALUE_2 ON LINE 15 WE GET THE FOLLOWING OUTPUT
if value_1 < value_2:
    print("I am schmol")
elif value_2 > value_1:
    print("I am thicker than 1")
else:
    print("Statement after ifs")
#I am schmol
#statement after if
#IF WE ADD A PASS STATEMENT UNDER ELSE ON LINE 20 WE GET THE FOLLOWING OUTPUT
if value_1 > value_2:
    print("I am schmol")
elif value_2 > value_1:
    print("I am thicker than 1")
else:
    pass
#I am thicker than 1
#statement after if
#PASS FUNCTION WORKS AS A PLACEHOLDER AND SIMPLY SKIP THE PART OF THE CODE
