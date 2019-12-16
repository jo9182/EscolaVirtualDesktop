import sqlite3


def getStudentData():
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    return c.execute('SELECT * FROM StudentData')

def getRoomData():
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    return c.execute('SELECT * FROM ClassroomData')

def getStudentsFromRoom(room):
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    return c.execute('SELECT * FROM StudentData WHERE room = '+ room)

def getSpecificRoom(room):
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    return c.execute('SELECT * FROM ClassroomData WHERE name = '+ room)

def getSpecificStudent(nameIn):
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    return c.execute("SELECT * FROM StudentData WHERE name = '"+ nameIn +"'")

def updateStudent(Data):
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    sql = "UPDATE StudentData SET name = '%s', age = '%s', room = '%s', job = '%s', keys = '%s', notes = '%s' WHERE name = '%s'"%Data
    c.execute(sql)
    conn.commit()
    conn.close()

def insertNewStudent(Data):
    conn = sqlite3.connect('EscolaVirtualDB')
    c = conn.cursor()
    sql = "INSERT INTO StudentData(name,age,room,job,keys,notes) values(?,?,?,?,?,?)"
    c.execute(sql,Data)
    conn.commit()
    conn.close()

"""for row in c.execute('SELECT * FROM StudentData'):
    ID = row[0]
    name = row[1]
    age = row[2]
    room = row[3]
    job = row[4]
    keys = row[5]
    notes = row[6]
    print(name)"""
