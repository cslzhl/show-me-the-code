import mysql.connector
import uuid

def create_code(num=200):
    result = []
    no = 0
    while no < num:
        temp = str(uuid.uuid1()).replace('-','')
        if not temp in result:
            result.append(temp)
            no +=1
    return result

def store_mysql(filepath):
    conn = mysql.connector.connect(user='root',password = 'password',database = 'showmethecode')
    cursor = conn.cursor()
    cursor.execute('show tables in showmethecode;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
            create table code(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,code CHAR(32) NOT NULL);
        ''')
    f = open(filepath,'rb')
    for line in f.readlines():
        code = line.strip()
        cursor.execute("insert into code(code) values('%s');" % (code))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    result = create_code()
    with open('active_code.txt','wb') as f:
        for code in result:
            temp = code + '\n'
            f.write(temp)
        f.close()
    store_mysql('active_code.txt')
