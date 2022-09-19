import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user = 'root',
            passwd= '1234',
            db= 'edu_flask',
            charset = 'utf8'
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        #self.db.cursor()그냥 사용하면 결과가 튜플형태로 반환되고,
        #self.db.cursor(pymysql.cursors.DictCursor)이렇게 사용하면 딕셔너리 형태로 반환된다고 함.

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
    