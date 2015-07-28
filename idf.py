
import os
import re
import codecs
import sqlite3
import math
import MyParser


def main():
    conn = sqlite3.connect('TF-IDF.db')
    conn.text_factory = str
    ########## conn.execute("""DROP TABLE IDFTable""")
    ########## conn.execute("""CREATE TABLE IDFTable (
    ##########                   WORD    TEXT   PRIMARY KEY,
    ##########                   IDF     INT    DEFAULT 0
    ##########                 );""")

    wa = 0
    m = 0
    print('Start idf')
    curs_word = conn.execute("""SELECT DISTINCT WORD FROM TFTable""")
    curs_doc = conn.execute("""SELECT DISTINCT DOC FROM TFTable""")
    doc_amount = len(curs_doc.fetchall())
    for row in curs_word:
        wa += 1
        if wa == 500:
            m += 1
            print(500*m)
        word = row[0]
        curs_doc = conn.execute("""SELECT DOC FROM TFTable WHERE WORD=:word""", {'word': word})
        cur_doc_amount = len(curs_doc.fetchall())
        param = (word, math.log(float(doc_amount) / cur_doc_amount, 2))
        conn.execute("""INSERT OR REPLACE INTO IDFTable VALUES (?, ?)""", param)
        conn.commit()
    print('End idf')
    # curs = conn.execute('SELECT * FROM IDFTable')
    # for row2 in curs:
    #     print(row2)
    conn.close()


if __name__ == '__main__':
    main()
