# write a program that takes a string and checks if it contains consecutive vowels or not. 
# It should give Positive as an output if it contains consecutive vowels and Negative otherwise. 
# For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels. So it should give Positive as an output. On the other hand, if you take the string of statoqag, the output should be Negative.

# First_Method:


vw=["a", "e", "i", "o", "u"]
nst=[]
first=input("Enter a string: ").lower()
for i in first:
    if i in vw:
        nst.append(i)
print(nst)
for i in range(0,(len(nst)-1)):
  if nst[i] in vw and nst[i+1] in vw and len(nst) > 1 :
    print("Positive")
    break   
else:
  print("Negative")

#  Second_Method:

# word = input("Please enter a string: ")
# word = word.lower()

# vowels = ["a", "e", "i", "o", "u"]
# exist = False

# for i in range(len(word)-1):
#   if word[i] in vowels:
#     if word[i+1] in vowels:
#       exist = True
#       break
      
# if exist:
#   print("Positive")
# else:
#   print("Negative")