import pymysql

host, port, user, passwd, db = 'remotemysql.com', 3306, '9hkyb0ebUg', 'Q9XsNQ9fQw', '9hkyb0ebUg'
# host, port, user, passwd, db = '0.0.0.0', 33306, 'user', 'user', 'myapp-db'

def insert(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        print("insert - ",cursor)
        cursor.execute(f"INSERT into myapp-db.users (user_id, user_name, creation_date) VALUES ({user_id},'{user_name}', CURRENT_TIMESTAMP);")

        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(e)
        raise Exception


def select(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        print("select - ",cursor)
        cursor.execute(f"SELECT * FROM myapp-db.users WHERE user_id = '{user_id}';")
        data = cursor.fetchall()
        user_name = data[0]['user_name']

        cursor.close()
        conn.close()
        return user_name
    except Exception as e:
        print(e)
        raise Exception


def update(user_id, user_name):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        print("update - ",cursor)
        cursor.execute(f"UPDATE myapp-db.users SET user_name = {user_name} WHERE user_id = '{user_id}';")

        cursor.close()
        conn.close()
        return user_name
    except Exception as e:
        print(e)
        raise Exception


def delete(user_id):
    try:
        # Establishing a connection to DB
        conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                               cursorclass=pymysql.cursors.DictCursor)
        conn.autocommit(True)
        # Getting a cursor from Database
        cursor = conn.cursor()
        print("delete - ",cursor)
        cursor.execute(f"DELETE FROM myapp-db.users WHERE user_id = {user_id};")

        cursor.close()
        conn.close()
        return user_id
    except Exception as e:
        print(e)
        raise Exception