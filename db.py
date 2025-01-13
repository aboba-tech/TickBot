import psycopg2

def connection():
    conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    database='abobadb',
    password='aboba')
    conn.autocommit = True

    return conn


def add_user(id):
    try:
        conn = connection()
        with conn.cursor() as cur:
            print(id)
            cur.execute(f"INSERT INTO attack_num (user_id) VALUES ({id})")
            print('New user added...')

    finally:
        if conn:
            conn.close()
            print("Connection closed...")

def check_user(id):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT user_id FROM attack_num
                        WHERE user_id = {id}
                         """)
            result = cur.fetchall()[0][0]

            if result == id:
                return True
            
    except IndexError:
        add_user(id)
            
    finally:
        if conn:
            conn.close()
            print("Connection closed..")

def add_bz(id: int, input: int, severity: str):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT bz_{severity} FROM attack_num
                WHERE user_id = {id}
                """)
            
            result = cur.fetchall()[0][0]
            new_value = result + input

            cur.execute(                
                f"""
                UPDATE attack_num
                SET bz_{severity} = {new_value}
                WHERE user_id = {id}
                """)

            print('Bzik added succesfully..')
            return view_all_data(id, cur)

    finally:
        if conn:
            conn.close()
            print('Connection closed..')


def remove_bz(id: int, input: int, severity: str):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT bz_{severity} FROM attack_num
                WHERE user_id = {id}
                """)
            
            result = cur.fetchall()[0][0]
            # r = print(result)  проверка работоспособности запроса

            # return r
            
            if result > 0:
                new_value = result - input

            cur.execute(                
                f"""
                UPDATE attack_num
                SET bz_{severity} = {new_value}
                WHERE user_id = {id}
                """)
            
            print('Bzik removed succesfully..')
            return view_all_data(id, cur)

    finally:
        if conn:
            conn.close()
            print('Connection closed..')


def add_pr(id: int, input: int, severity: str):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT pr_{severity} FROM attack_num
                WHERE user_id = {id}
                """)
            
            result = cur.fetchall()[0][0]

            new_value = result + input

            cur.execute(                
                f"""
                UPDATE attack_num
                SET pr_{severity} = {new_value}
                WHERE user_id = {id}
                """)
            
            print('Pristup added succesfully..')
            return view_all_data(id, cur)

    finally:
        if conn:
            conn.close()
            print('Connection closed..')


def remove_pr(id: int, input: int, severity: str):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(
                f"""
                SELECT pr_{severity} FROM attack_num
                WHERE user_id = {id}
                """)
            
            result = cur.fetchall()[0][0]
            
            if result > 0:
                new_value = result - input

            cur.execute(                
                f"""
                UPDATE attack_num
                SET pr_{severity} = {new_value}
                WHERE user_id = {id}
                """)
            
            print('Pristup removed succesfully..')
            return view_all_data(id, cur)
            



    finally:
        if conn:
            conn.close()
            print('Connection closed..')


def view_all_data(id, cur):
    cur.execute(f"""
                SELECT * FROM attack_num
                WHERE user_id = {id}   
                """)
    
    res = cur.fetchall()
    res_list = []
    for x in range(len(res[0])):
        res_list.append(res[0][x])
        x += 1

    return res_list


def view_all_data_full(id):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT * FROM attack_num
                        WHERE user_id = {id}   
                        """)
            
            res = cur.fetchall()
            res_list = []
            for x in range(len(res[0])):
                res_list.append(res[0][x])
                x += 1

        return res_list

    finally:
        if conn:
            conn.close()
            print('Connection closed..')

def clear_data(id):
    try:
        conn = connection()
        with conn.cursor() as cur:
            cur.execute(f"""
                        SELECT * FROM attack_num
                        WHERE user_id = {id}   
                        """)
            
            res = cur.fetchall()
            res_list = []
            for x in range(len(res[0])):
                res_list.append(res[0][x])
                x += 1

        return res_list

    finally:
        if conn:
            conn.close()
            print('Connection closed..')

# 6830309199
# 1089193715
# 2147483647
