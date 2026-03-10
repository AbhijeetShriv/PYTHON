try:
    x=int(input("Enter Number : "))
    y=int(input("Enter another number : "))
    result=x/y
except ZeroDivisionError:
    print("Division by Zero Error")
else:
    print("Result : ", result)