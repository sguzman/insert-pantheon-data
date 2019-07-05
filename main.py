import atexit
import json
import psycopg2


def read_json() -> json:
    json_path: str = './people.json'
    json_str: str = open(json_path, 'r').read()

    json_obj: json = json.loads(json_str)
    return json_obj


def con() -> psycopg2:
    conn: psycopg2 = \
        psycopg2.connect(user='admin', password='', host='127.0.0.1', port='5432', database='misc')

    def clean_up() -> None:
        conn.close()
        print('Closing connection', conn)

    atexit.register(clean_up)
    return conn


def insert_peep(person: json) -> None:
    print(person)


def main() -> None:
    js: json = read_json()
    for peep in js:
        insert_peep(peep)


if __name__ == '__main__':
    main()
