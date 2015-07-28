# coding utf-8
import os
import re
import codecs
import sqlite3
import math
import MyParser


def main():
    conn = sqlite3.connect('TF-IDF.db')
    conn.text_factory = str
    # conn.execute("""DROP TABLE FILESTable""")
    # conn.execute("""CREATE TABLE FILESTable (
    #                   DOC     TEXT   PRIMARY KEY
    #                 );""")

    c = conn.execute("""SELECT * FROM FILESTable""")
    for r in c:
        print(r[0])
    q = str(raw_input('continue?'))
    if q == 'n' or q == 'qq':
        return

    path = 'C:\Users\i.skripnikov\Downloads\en\www'
    print('Start looking for *.html files')
    list_of_dirs = os.listdir(path)
    while len(list_of_dirs) > 0:
        filename = list_of_dirs[0]
        list_of_dirs.remove(filename)
        if not filename.endswith('.html'):
            print(filename)
            try:
                tmp = os.listdir('\\'.join([path, filename]))
            except Exception:
                continue
            for each in tmp:
                if each not in list_of_dirs:
                    list_of_dirs.insert(0,'\\'.join([filename, each]))
            continue
        else:
            conn.execute("""INSERT OR IGNORE INTO FILESTable VALUES (:doc)""", {"doc": '\\'.join([path, filename])})
            conn.commit()
    print('End looking  for *.html files')
    conn.close()

if __name__ == '__main__':
    main()
