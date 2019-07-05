import atexit
import json
import psycopg2
from typing import Optional


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
    lon: Optional[str] = p.get('LON')
    lat: Optional[str] = p.get('LAT')

    lon_float: Optional[float] = None
    if lon is not None:
        if len(lon) != 0:
            lon_float = float(lon)

    lat_float: Optional[float] = None
    if lat is not None:
        if len(lat) != 0:
            lat_float = float(lat)

    page_views: Optional[str] = p.get('PageViewsEnglish')
    birth_state: Optional[str] = p.get('birthstate')
    birth_city: Optional[str] = p.get('birthcity')
    average_views: Optional[int] = p.get('AverageViews')

    sql_peep_insert: str = 'INSERT INTO misc.public.people (name, domain, countryCode, longitude, latitude, pageViewsEnglish, birthYear, birthState, occupation, en_curid, numLangs, birthCity, averageViews, totalPageViews, countryName, stdDevPageViews, countryCode3, pageViewsNonEnglish, dataset, l_star, gender, industry, hpi, continentName) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    data = [p['name'], p['domain'], p['countryCode'], lon_float, lat_float, page_views, p['birthyear'], birth_state, p['occupation'], p['en_curid'], p['numlangs'], birth_city, average_views, p['TotalPageViews'], p['countryName'], p['StdDevPageViews'], p['countryCode3'], p['PageViewsNonEnglish'], p['dataset'], p['L_star'], p['gender'], p['industry'], p['HPI'], p['continentName']]
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
