# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")
# Iteration - loops

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello {name}")

# while name == "":
#     print("You did not enter your name")
# #infinite loop
# print(f"Hello {name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")


# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")


# num = int(input("Enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10"))

# print(f'Your number is {num}')



# for loops = execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.

#Count
# for x in range(1, 11):
#     print(x)

#Count backwards
# for x in reversed(range(1, 11)):
#     print(x)

#print("HAPPY NEW YEAR!")

#Skip count
# for x in range(1, 11, 2):
#     print(x)

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

#Skip a #
# for x in range(1, 21):
#     if x == 13:
#         continue  #Skips over the number
#     else:
#         print(x)

#Stop at a number
# for x in range(1, 21):
#     if x == 13:
#         break  #Stops the count
#     else:
#         print(x)



# Challenge

list_of_names = ['John', 'Paul', 'George', 'Ringo']
# if the name is 'George', print 'Gerorge was found!'
# otherwise, print 'George was not found!' and print
# out the other names using a loop

for name in list_of_names:
    if name == 'George':
        print('George was found!')
    else:
        print('George was bto found!')
        print(name)

list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
# loop through the list_of_names2 and
# if the name is 'Ironman', skip over it and
# print out the other names

for name in list_of_names2:
    if name == 'Ironman':
        continue
    print(name)

#Renaming/Updating list
for name in list_of_names2:
    if name == 'Thanos':
        name = 'Jeffy'
    print(name)
