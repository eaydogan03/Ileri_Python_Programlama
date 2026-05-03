import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

target_id=4

sql="DELETE FROM urunler WHERE id= ?"

cursor.execute(sql, (target_id,))

db.commit()

db.close()