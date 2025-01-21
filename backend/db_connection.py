import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        #host='localhost',
        host='lab-edu-rds-aurora.cluster-c9g0we6ously.ap-northeast-2.rds.amazonaws.com',
        database='trip_advisor',
        user='user',
        password='qwer1234'
    )
    return conn