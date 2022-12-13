#In this we gonna focus on loops and what they do
print("endless loop: ", end= "")
for value in range(0,5):
    print(value, end="")
print()
print("the loop continue: ", end="")
for value in range(0,5):
    if value == 2:
        print ("#", end="")
        continue 
    print(value, end="")
print()
print("Looping with pass:  ", end="")
for value in range(0,5):
    if value == 3:
        print("#", end="")
        pass
    print(value, end="")
print()
print("Looping with break:  ", end="")
for value in range(0,5):
    if value == 3:
        print("#", end="")
        break
    print(value, end="")