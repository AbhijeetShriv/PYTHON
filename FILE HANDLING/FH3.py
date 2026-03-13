products=[
    ("Laptop",1200.50,5),
    ("Mouse",25.99,50),
    ("Keyboard",75.00,15)
]

output_file="inventory.csv"

#1. Write the formatted data to a file
print(f"---Writing Formatted data to {output_file}---")
with open(output_file,'w') as file:
    # Write Header
    file.write(f"{'Product':<15} | {'Price':>10} | {'Stock' : >5}\n")
    file.write("-" * 35 + "\n")

    #Write Product Data using f-string formatting
    for name,price,stock in products:
        #Formatting: < 15 (Left-align in 15 Spaces), >10.2f (right-align, 2 Decimal Places)

        line=f"{name:<15} | ${price : >9.2f} | {stock:>5}\n"
        file.write(line)

        print("Inventory Saved With Formatting.")


#2. Read the formatted data back
print(f"\n---Reading Formatted data from {output_file}---")
with open(output_file,'r') as file :
    print(file.read())






















