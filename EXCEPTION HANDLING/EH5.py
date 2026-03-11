try:
    num=int(input("Enter a Number : "))
    print(100/num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Calculation SuccessFul")
finally:
    print("Program Ended")