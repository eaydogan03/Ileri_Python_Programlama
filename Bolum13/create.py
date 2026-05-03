import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS urunler (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               urun_adi TEXT NOT NULL,
               fiyat REAL,
               stok_adedi INTEGER)"""

)

db.commit()
print("Tablo oluşturuldu.")

db.close()