import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

yeni_fiyat=50000
urun_id=1

sql="UPDATE urunler SET fiyat= ? WHERE id= ?"

cursor.execute(sql, (yeni_fiyat, urun_id))

db.commit()