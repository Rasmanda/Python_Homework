# Assign the name of 2 items to 2 variables. if the values of the 2 variable are equal print the items are the same. if not print the items
# are different

a = 10
b = 20
if (a == b): print("The items are the same")
else: print("The items are not the same")

# 2 task. ask for name and age. check if the person can enter the club. if yes, welcome them. if not- refuse

Legalage = 18
print("Hello, what is you name?")
name = input()

print("How old are you?")
age = int(input())
if age >= Legalage:
    print(f"welcome to the club, {name}.Have fun!")
else:
    yearsleft = Legalage - age
    print(f"{name},sorry, unfortunatelly you are too young. Come back after {yearsleft} years.")
