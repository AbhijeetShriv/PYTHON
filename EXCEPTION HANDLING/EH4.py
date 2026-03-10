try:
    f=open("demo.txt",'r')
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Execution Completed")
