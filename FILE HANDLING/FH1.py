file_name="data_record.txt"

#1. CREATING AND WRITING THE FILE WITH ('W' mode)
# 'W' Mode Opens The File and immediately truncates (clears) it.
print(f"---1.Writing to {file_name} ---")
with open(file_name,'w') as file:
    file.write("Name :Abhijeet\n")
    file.write("Age : 19n\n")
    print("Data Written Successfully.")

#2. READING ('R' mode)
print(f"\n---2.Reading {file_name} File ---")
with open(file_name,'r') as file:
    content=file.read()
    print(content)

#3. APPEND ('A' mode)
print(f"\n---3.Appending New Data to {file_name}---")
with open(file_name,'a') as file:
    file.write("City:Gandhidham\n")
    print("New Data Appended Successfully.")


#4 FINAL READ TO VERIFY
print(f"\n---4. Final Verification read ---")
with open(file_name,'r') as file:
    lines=file.readlines()
    print("Content as a list of lines:")
    print(lines)

