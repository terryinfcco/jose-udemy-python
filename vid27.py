# list comprehensions
# quickly create a list in Python

mylist = []

s = 'somestring'

for letter in s:
    mylist.append(letter)
print(mylist)

mynewlist = [letter for letter in s]
print(mynewlist)

squares = [x**2 for x in range(0,11)]
print (squares)

evens = [x for x in range(0,10) if x % 2 == 0]
print (evens)
