# SELECT CODES AND THAN [CTRL + /].It Helps To Comment OR Uncomment the code us
import sqlite3

connector=sqlite3.connect("ONE.db",isolation_level=None)
cursoor=connector.cursor()

cursoor.execute("CREATE TABLE Tipper(ID INT, NAME TEXT)")
uid=int(input("Enter ID: "))
nam=input("Enter Name: ")
cursoor.execute("INSERT INTO Tipper(ID,NAME) VALUES(?,?)",(uid,nam))
cursoor.execute("SELECT * FROM Tipper")
rows=cursoor.fetchall()
print("ID\t NAME")
print("-" * 99)
for row in rows:
    print(row[0],"\t",row[1])
cursoor.execute("UPDATE Tipper SET NAME = ? WHERE ID = ?",(nam,uid))
cursoor.execute("DELETE FROM Tipper where ID = ?",(uid,))
