try:
    lst=[1,2,3]
    print(lst[5])
except IndexError:
    print("Index out of range")
except TypeError:
    print("Type Mismatch")

