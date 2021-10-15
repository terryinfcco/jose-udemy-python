# Indentation critical to Python
# blocks of code defined by indentation levels

if 1 < 2:
    print('Condition met')

if 1==1:
    print("Condition met 1==1")
else:
    print("Last Block happened to run")

if 2 == 0:
    print('first condition true')
elif 2 == 1:
    print('second condition true')
else:
    print('nothing above was true')

agent_code = 231912
access = False

if agent_code == 12345:
    print("Code Reset")
    print("Call a supervisor")
elif agent_code == 231912:
    print("Welcome agent 231912")
    access = True
else:
    print("Sorry no matching agent_code")

# if you know your variable is a boolean you can just do simpler/cleaner code
# if access:
if access == True:
    print("Access Granted")
else:
    print("Access Denied")