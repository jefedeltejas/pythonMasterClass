name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
color = input("What's your favorite color, {0}?".format(name))
print(color)

if age >= 189:
    print("You're very old homie")
elif age >= 16:
    print("Time to get a job")
else:
    print("Sorry you are not eligible for our services. Please come back in {0} years.".format(18 -age))
