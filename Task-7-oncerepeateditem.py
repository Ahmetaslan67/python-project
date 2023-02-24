# Problem Statement
# A book store is trying to find the books that are only left 1 in the stock.
# They have the book list and they ask you to find the books. 
# You are going to write a computer program that finds the non-repeated values in the list. 
#  Also indicate how you have used computational thinking concepts to find the solution.

products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]

# First method:

for i in products:
    if products.count(i)==1: print(i)

# Second method:
i=0
for a in products:
    products.remove(a)
    if not a in products: print(a)
    products.insert(i, a)
    i+=1

# # Third method:

dict={}
for i in range(len(products)):
    letter=products[i]
    count=products.count(products[i])
    dict.update({letter:count})

for i in range(len(dict)):
    if list(dict.values())[i]==1: print(list(dict.keys())[i])

## Fourth method:

for product_1 in products:
  count = 0
  for product_2 in products:
    if product_1 == product_2:
      count += 1
      if count > 1:
        break
  if count == 1:
    print(product_1)
