#ask the user to enter his/her name

full_name = input("Enter your name: ")
print("Name: " + full_name)

#ask the user to enter his/her age

age = int(input("Enter your age: "))
print("Age: " + str(age))

#ask the user's gender

gender = input("Enter your gender: ")
print("Gender: " + gender)

#ask the user for 2 of his hobbies

hobby1 = input("Enter your 1st hobby: ")
print("Hobby 1: " + hobby1)

hobby2 = input("Enter your 2nd hobby: ")
print("Hobby 2: " + hobby2)

#display the information

print("My Information")
print("\tFull Name: {0}".format(full_name))
print("\tAge: {0}".format(age))
print("\tGender: {0}".format(gender))
print("\tHobby 1: {0}".format(hobby1))
print("\tHobby 2: {0}".format(hobby2))

print("\tThank you for reading my information :)")

input("Press enter to terminate")