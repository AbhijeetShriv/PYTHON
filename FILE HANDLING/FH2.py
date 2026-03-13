import pathlib

#Define the Directory and the file nams

dir_name="reports"
file_name="summary.txt"

#1.Create a Path Object for the new directory
reports_dir=pathlib.Path(dir_name)

#2.Check if the Directory exists and the create it if it doesn't
if not reports_dir.exists():
    reports_dir.mkdir()
    print(f"Directory : '{dir_name}' Created.")

#3. Create a path object for the file using the / operator (path joining)
file_path=reports_dir/file_name

#4. Write data using the relative path
print(f"\n---Writing to the File at Relative path: {file_path}---")
with open(file_path,'w') as file:
    file.write("Report for Q4.\n")
    file.write("Status : Completed.\n")
    print("Report Written.")

#5. Read the file to demonstrate the path works
print(f"\n---Reading from {file_path} ---")
with open(file_path,'r') as file:
    print(file.read())

