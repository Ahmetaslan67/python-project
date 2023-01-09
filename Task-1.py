# TASK - 1 (Write a Python program to display the first and last colors from the following list.)

color_list = ["Red","Green","White" ,"Black"]
print(f"{color_list[0]}, {color_list[3]}")

# TASK - 2 (Write a Python program to accept a filename from the user and print the extension of that.)
# Sample filename : abc.java , Output : java)

filename = input("Enter a filename: ")
i = filename.index(".")
print(i)
print(filename[i+1:])


# TASK - 3  (Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23, Output : 
# #List : ['3', ' 5', ' 7', ' 23'] Tuple : ('3', ' 5', ' 7', ' 23')

num1 = input("Enter number one with comma: ")
num2 = input("Enter number two with comma: ")
num3 = input("Enter number three (last number): ")

list = []
list.append(num1)
list.append(num2)
list.append(num3)
print(list)
tuple = tuple(list)
print(tuple)
