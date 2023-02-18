# Write a program that takes inputs of strings from the user (until the user enters "exit", case-insensitive), and then prints the most frequent letter (excluding "exit") and its occurrence count in these strings.

# Please note that you cannot make any assumptions on the capitalization of the letters of strings, thus lowercase and uppercase of the same letters should be counted in the same occurrence.

lst=[]
while True:
    str=input("Enter a string: ").lower()
    if str != "exit":
        lst.append(str)
    else:
        break
print(lst)
insec=[]
for i in range(len(lst)):
    insec.extend(lst[i])   # created  a list (insec) which covers letters of lst items.
print(insec)

a=max(set(insec), key=insec.count)
count=0

for i in insec:
    if i == a:
        count=count+1
print(f"{a} -> {count}")


# in case most frequent letter to be counted once per string,
# we need to change line 21-24 in the way shown below;

# for wrd in lst:
#     if a in wrd:
#         count+=1
# print(f"{a} -> {count}")

