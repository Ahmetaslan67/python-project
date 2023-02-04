# Problem Statement
# Write a program that takes a string and checks if it contains consecutive vowels or not and these consecutive vowels are at the same ordered with the list [a,e,i,o,u] like ae, io etc.
# It should give Positive as an output if it contains consecutive vowels and Negative otherwise. 
# For example saetqi string contains a adjacent to e, which means that it contains consecutive vowels. So it should give Positive as an output. On the other hand, if you take the string of statoqag, the output should be Negative.

# Expected Output:
# Please enter a string: gasdph
# Negative

# Please enter a string: ae or soul or keil 
# Positive

# Please enter a string: taom
# Negative

# Please enter a string: a
# Negative

print("This program checks the consecutive vowels in a str ing that you enter")
print("Please write 'exit' to terminate the program")
vw=["a", "e", "i", "o", "u"]

while True:
    nst,frk,a,b=[],[],0,0
    first=input("Enter a string: ").lower()
    if first=="exit":
        break
    else:
        for i in first:
            if i in vw:
                nst.append(i)
        while (b-a)!=1:
            print(f"nst={nst}")
            if len(nst) > 1:
                for i in range(0,(len(nst)-1)):
                    a= int(vw.index(nst[i]))
                    b= int(vw.index(nst[i+1]))
                    frk.append(b-a)
                if 1 in frk:
                    print("Positive")
                    break
                else:
                    print("Negative")
                    break
            else:
                print("Negative")
                break
