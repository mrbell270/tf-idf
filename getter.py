import sqlite3

conn = sqlite3.connect('TF-IDF.db')
while True:
    word = str(raw_input('Input: '))
    if word == 'qq':
        break
    else:
        curs = conn.execute("""SELECT DOC, TF FROM TFTable WHERE WORD=:word""", {"word": word})
        print('TFs')
        for row in curs:
            print(': '.join([row[0], str(row[1])]))
        curs = conn.execute("""SELECT IDF FROM IDFTable WHERE WORD=:word""", {"word": word})
        for row in curs:
            print(': '.join(['IDF', str(row[0])]))

    print("-" * 20)

conn.close()