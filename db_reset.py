import sqlite3
conn = sqlite3.connect('TF-IDF.db')

conn.execute("""DROP TABLE FILESTable""")
conn.execute("""CREATE TABLE FILESTable (
                  DOC     TEXT   PRIMARY KEY
                );""")

conn.execute("""DROP TABLE TFTable""")
conn.execute("""CREATE TABLE TFTable (
                  DOC     TEXT   NOT NULL,
                  WORD    TEXT   NOT NULL,
                  TF      INT    DEFAULT 0,
                  PRIMARY KEY(WORD, DOC)
                );""")

conn.execute("""DROP TABLE IDFTable""")
conn.execute("""CREATE TABLE IDFTable (
                  WORD    TEXT   PRIMARY KEY,
                  IDF     INT    DEFAULT 0
                );""")