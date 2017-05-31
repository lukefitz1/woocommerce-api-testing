import pymysql

class db():

    def __init__(self):
        pass

    def __connect(self, db):
        host = '127.0.01'
        conn = pymysql.connect(host=host, port=3306, user='root', passwd='root', db=db)
        return conn

    def select(self, db, query):
        # make connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute query
        cur.execute(query)
        result = cur.fetchall()

        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col))

            all_rows.append(row)

        # close connection
        conn.close()
        cur.close()

        return all_rows

    def update(self, db, query):
        # make connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute query
        result = cur.execute(query)
        conn.commit()

        # close connection
        conn.close()
        cur.close()

        return result