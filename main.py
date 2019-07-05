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


def insert_peep(conn: psycopg2, p: json) -> None:
    sql_peep_insert: str = 'INSERT INTO misc.public.people (name, domain, countryCode, longitude, latitude, pageViewsEnglish, birthYear, birthState, occupation, en_curid, numLangs, birthCity, averageViews, totalPageViews, countryName, stdDevPageViews, countryCode3, pageViewsNonEnglish, dataset, l_star, gender, industry, hpi, continentName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    data = [p['name'], p['domain'], p['countryCode'], float(p['LON']) if len(p['LON']) != 0 else None, float(p['LAT']) if len(p['LAT']) != 0 else None, p['PageViewsEnglish'], p['birthyear'], p['birthstate'], p['occupation'], p['en_curid'], p['numlangs'], p['birthcity'], p['AverageViews'], p['TotalPageViews'], p['countryName'], p['StdDevPageViews'], p['countryCode3'], p['PageViewsNonEnglish'], p['dataset'], p['L_star'], p['gender'], p['industry'], p['HPI'], p['continentName']]
    print('Inserting', data)

    cursor = conn.cursor()
    cursor.execute(sql_peep_insert, data)

    conn.commit()
    cursor.close()


def main() -> None:
    conn: psycopg2 = con()
    js: json = read_json()
    for peep in js:
        insert_peep(conn, peep)


if __name__ == '__main__':
    main()
