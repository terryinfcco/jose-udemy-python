# for loops to iterate over python objects

mylist = [1,2,3,4]
for num in mylist:
    # end line with a space to get everything on one line
    print(num, end=" ")

print("\n")

for letter in 'this is a string':
    print(letter, end=" ")

print("\n")

# tuple unpacking note the parens around item1,item2 are optional.
list_of_tuples = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for (item1, item2) in list_of_tuples:
    print(item1)
    print(item2)
    print('\n')

# example for dictionary
d = {'a':1,'b':2,'c':3}
for key,value in d.items():
    print(f"key is: {key} ")
    print(f"value is: {value} ")

# example of continue statement - in this case d won't print
for letter in 'code':
    if letter == 'd':
        continue
    print(letter)
