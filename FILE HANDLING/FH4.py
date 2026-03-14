import pathlib

# --- Setup: Define Path and Data ---

data_dir=pathlib.Path("Student_data")
if not data_dir.exists():
    data_dir.mkdir()

data_file_path=data_dir/"records.txt"
print(f"Working with File : {data_file_path}")

students_to_add=[
    ("Ramesh",88,"A"),
    ("Suresh",75,"B")
]

new_enrollment=("Mahesh",92,"A+")

# --- PHASE 1: Create and Initial write (Formatted)---
print("\n---Phase 1 : Creating / Overwriting file and writing initial records---")
#Use 'w' to create or overwrite the file

with open(data_file_path,'w') as f:
    #Write a header using f-strings for all alignment
    f.write(f"{'Name': <10}{'Score': >6}{'Grade': >8}\n")
    f.write("-" * 24 + "\n")

    #Write initial Data
    for name,score,grade in students_to_add:
        #Format the Line
        formatted_line=f"{name:<10}{score:>6}{grade:>8}\n"
        f.write(formatted_line)

    print("Initial Records Written.")


# --- PHASE 2 : READ AND DISCPLAY ---
print(f"\n---Phase 2 : Reading the current file content (read())---")
with open(data_file_path,'r') as f:
    content=f.read()
    print(content)

# --- PHASE 3 : APPEND a new Record (Formatted) ---
print("\n---Phase 3:Appending one new student record --- ")
#use 'a' to append to the end of the file
with open(data_file_path,'a') as f :
    #Format the single new enrollment data
    name,score,grade=new_enrollment
    formatted_line=f"{name:<10}{score:>6}{grade:>8}\n"
    f.write(formatted_line)
    print(f"Record for {name} Appended.")


# ---PHASE 4 : Final Read (Readlines())---
print("\n---Phase 4 : Final Verification (readlines())---")
with open(data_file_path,'r') as f :
    #Read all lines into a list
    all_lines=f.readlines()

    #Process and print each line except the header
    print("Final Records (Excluding header and separator) : ")
    for line in all_lines[2:]:
        print(line.strip())

print("\nFile Handling sequence Complete.")




















