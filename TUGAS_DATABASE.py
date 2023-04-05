#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
    user  = 'root',
    host = 'localhost'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[2]:


import mysql.connector

conn = mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023')

print(conn)
conn.close()


# In[3]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MAHASISWA (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30) NOT NULL,
                    Alamat VARCHAR(255) NOT NULL,
                    Mata_kuliah_yang_diikuti VARCHAR(10),
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[4]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE DOSEN (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50) NOT NULL,
                    Mata_kuliah_yang_diajar VARCHAR(50),
                    Umur INT,
                    Jenis_kelamin VARCHAR(10)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[5]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

studentRecord = """CREATE TABLE MATA_KULIAH (
                    Kode_MK VARCHAR(10) NOT NULL,
                    Nama_MK VARCHAR(50) NOT NULL,
                    Waktu DATE,
                    Ruangan VARCHAR(10),
                    Gedung VARCHAR(20)
                    )"""

cursorObject.execute(studentRecord)
dataBase.close()


# In[6]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MAHASISWA (NIM, Nama, Alamat, Mata_kuliah_yang_diikuti, Umur, Jenis_kelamin)VALUES (%s, %s, %s, %s, %s, %s)"
val = [("H004451", "Siti", "Jawa Selatan", "APSI", "19", "P"),
       ("H004452", "Joko", "Jawa Utara", "PBO", "17", "L"),
       ("H004453", "Saimin", "Jawa Tenggara", "MIKRO", "18", "L"),
       ("H004454", "Bambang", "Jawa Barat Daya", "PYTHON", "19", "L"),
       ("H004455", "Karno", "Jawa Timur Laut", "WIRELESS", "18", "L"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[7]:



import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO DOSEN (NIP, Nama_Dosen, Mata_kuliah_yang_diajar, Umur, Jenis_kelamin)VALUES (%s, %s, %s, %s, %s)"
val = [("DSN001", "Darmawan", "APSI", "19", "L"),
       ("DSN002", "Masbahah", "PBO", "17", "P"),
       ("DSN003", "Fendi", "MIKRO", "16", "L"),
       ("DSN004", "Yusuf", "PYTHON", "19", "L"),
       ("DSN005", "Rachman", "WIRELESS", "18", "L"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[9]:



import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

sql = "INSERT INTO MATA_KULIAH (Kode_MK, Nama_MK, Waktu, Ruangan, Gedung)VALUES (%s, %s, %s, %s, %s)"
val = [("MK001", "APSI", "2023-03-1", "R1L1", "G.Biru"),
       ("MK002", "PBO", "2023-03-2", "R1L2", "G.Hijau"),
       ("MK003", "MIKRO", "2023-03-3", "R1L3", "G.Hijau"),
       ("MK004", "PYTHON", "2023-03-4", "R2L1", "G.Biru"),
       ("MK005", "WIRELESS", "2023-03-5", "R1L2", "G.Biru"), ]

cursorObject.executemany(sql, val)
dataBase.commit()

dataBase.close()


# In[47]:


import mysql.connector

dataBase= mysql.connector.connect(
    user  = 'root',
    host = 'localhost',
    database = 'd3_ti_2023'
)

cursorObject = dataBase.cursor()

#print Mata kuliah yang diikuti kemudian Mahasiswa yang mengikuti matkulnya, dan yang terakhir Dosen yang mengajar matkulnya
sql = "SELECT   matkul.Nama_MK, mahasiswa.Nama, dosen.Nama_Dosen FROM MATA_KULIAH matkul         INNER JOIN MAHASISWA mahasiswa ON mahasiswa.Mata_kuliah_yang_diikuti = matkul.Nama_MK         INNER JOIN DOSEN dosen ON dosen.Mata_kuliah_yang_diajar = matkul.Nama_MK"

cursorObject.execute(sql)

result = cursorObject.fetchall()

for row in result:
    print(row)

dataBase.close()


# In[ ]:




