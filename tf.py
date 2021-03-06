
import os
import re
import codecs
import sqlite3
import math
import MyParser


def main():
    conn = sqlite3.connect('TF-IDF.db')
    conn.text_factory = str

    parser = MyParser.MyHTMLParser()
    curs_files = conn.execute("""SELECT * FROM FILESTable""")
    for row_filename in curs_files:
        filename = row_filename[0]
        try:
            f = codecs.open(filename, encoding='utf8')
        except Exception:
            conn.execute("""DELETE FROM FILESTable WHERE DOC=:doc""", {"doc": filename})
            continue
        parser.feed(f.read())
        word_amount = dict()
        p = re.compile('\w+', re.U)
        for word in p.findall(parser.HTMLData):
            if word not in word_amount:
                word_amount[word] = 0
            word_amount[word] += 1
        total = sum(word_amount.values())
        word_freq = map(lambda x: (x[0], float(x[1]) / total), word_amount.iteritems())
        print(': '.join(['Start tf', filename]))
        param = []
        for tup in word_freq:
            param.append(filename, tup[0], tup[1])
        conn.executemany("""INSERT OR IGNORE INTO TFTable VALUES (?, ?, ?)""", param)
        conn.commit()
        parser.HTMLData = ''
    print('End tfs')
    conn.close()


if __name__ == '__main__':
    main()
