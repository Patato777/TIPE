import sqlite3

conn = sqlite3.connect(input('DB?'))
res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(res.fetchall())
curs = conn.cursor()

table = input('Table?')

col = None

print(curs.execute(f'SELECT COUNT(*) FROM {table}').fetchone())

curs.execute(f'DROP TABLE IF EXISTS new_{table}')
curs.execute(f'CREATE TABLE new_{table} AS SELECT * FROM {table} LIMIT 1')
curs.execute(f'DELETE from new_{table}')

print('New table created')

for k,row in enumerate(curs.execute(f'SELECT * FROM {table}').fetchall()):
    if col == None:
        col = [i for i, s in enumerate(row) if type(s) == str and s.startswith('[')][0]
        col_name = curs.description[col][0]
        print(col)
    other_keys1, other_keys2 = row[:col], row[col + 1:]
    val_list = eval(row[col])
    curs.executemany(f'INSERT INTO new_{table} VALUES ({",".join("?" * len(row))})',
                         [(*other_keys1, str(val), *other_keys2) for val in val_list])
    conn.commit()
    if not k%100:
        print(k)

#print(k)
print(curs.execute(f'SELECT COUNT(*) FROM new_{table}').fetchone())
#print(curs.execute(f'SELECT * FROM new_{table}').fetchall())

if input('Replace records? y/N').lower() == 'y' :
    curs.execute(f'INSERT INTO {table} SELECT * FROM new_{table}')
    curs.execute(f'DELETE from {table} WHERE {col_name} LIKE "[%]"')

curs.execute(f'DROP TABLE new_{table}')
conn.commit()
             
curs.close()
conn.close()
