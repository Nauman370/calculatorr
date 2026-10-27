import sys
print("Calculator")
print("==================")
x=int(input("Enter your first number "))
y=int(input("Enter your second number "))
print("1st number is",x)
print("second number is",y)
if y==0:
    print("invalid number")
else:
    addition=x+y
    subtraction=x-y
    multiplication=x*y
    division=x/y
    operation_1=addition
    operation_2=subtraction
    operation_3=multiplication
    operation_4=division
    print("1=addition,2=subtraction,3=multiplication,4=division")
    operation_user=int(input("Select your operation"))
    if operation_user==1:
        print(operation_1)
    elif operation_user==2:
        print(operation_2)
    elif operation_user==3:
        print(operation_3)
    elif operation_user==4:
        print(operation_4)
    else:
        print("invalid operation")
exiting_code=int(input("Press 99 to exit the code"))
if exiting_code==99:
    sys.exit()
else:
    print("Calculator")
print("==================")
x=int(input("Enter your first number "))
y=int(input("Enter your second number "))
print("1st number is",x)
print("second number is",y)
if y==0:
    print("invalid number")
else:
    addition=x+y
    subtraction=x-y
    multiplication=x*y
    division=x/y
    operation_1=addition
    operation_2=subtraction
    operation_3=multiplication
    operation_4=division
    print("1=addition,2=subtraction,3=multiplication,4=division")
    operation_user=int(input("Select your operation"))
    if operation_user==1:
        print(operation_1)
    elif operation_user==2:
        print(operation_2)
    elif operation_user==3:
        print(operation_3)
    elif operation_user==4:
        print(operation_4)
    else:
        print("invalid operation")
exiting_code=int(input("Press 99 to exit the code"))
if exiting_code==99:
    sys.exit()