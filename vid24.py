# While loop - execute a block of code while a condition is true
# Be careful - easy to have infinite while loops

x = 0

while x < 3:
    print('X is currently:')
    print(x)
    print('Still less than 3, add 1 to x')
    x = x + 1
    print("\n")

save_input = input('Please input a number: ')

print('Welcome Agent')

passcode = 0

while passcode != 123:
    # input provides a string, so have to convert to integer for our test
    passcode = int(input('Please provide your passcode: '))

    if passcode != 123:
        print("Wrong Password")
        print("Please try again")
        print("\n")

print("Correct Password")
