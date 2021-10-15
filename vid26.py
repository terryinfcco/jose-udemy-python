# Miscellaneous operators

# range function - generate a list of integers
# for num in range(0,11)  # will print 0 to 10 not including 11
# 3rd argument is step - for num in range(0,101,5) - will print 0,5,10,15,,,, 100

print(list(range(0,10)))

# enumerate function - create an index while iterating over an object
# creates a list of tuples where the first item in each tuple is the index you're at
for index,letter in enumerate('abcdefg'):
    print(f"At index {index} the letter is {letter}")

# zip function creates a list of tuples from 2 lists.
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
for item in zip(list1, list2):
    print (item)

# in - check for something in an object
# x in 'abcdefg' ==> False
# x in 'wxyz' ==> True

# max and min find max and mins in lists
from random import shuffle
# shuffle shuffles a list
mylist = [10,20,30,40,50]
shuffle(mylist)
print(mylist)

from random import randint
print(randint(0,10000))

# covered and or and not to combine conditionals 




