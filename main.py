import atexit
import json
import psycopg2


def con() -> psycopg2:
    conn: psycopg2 = \
        psycopg2.connect(user='salvadorguzman', password='', host='127.0.0.1', port='5432', database='personal')

    def clean_up() -> None:
        conn.close()
        print('Closing connection', conn)

    atexit.register(clean_up)
    return conn


def main() -> None:
    print('hello')


if __name__ == '__main__':
    main()
