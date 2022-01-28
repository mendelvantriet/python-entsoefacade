from django.db import connection


def persist(df):
    with connection.cursor() as cursor:
        df.to_sql('records_updated', con=cursor.connection, index=False, if_exists='replace', dtype={
            'country_code_from': 'String', 'country_code_to': 'String', 'timestamp': 'DateTime', 'capacity': 'Float'})

        cursor.execute("INSERT INTO transmission_transmission(timestamp, country_code_from, country_code_to, capacity) "
                       "SELECT timestamp, country_code_from, country_code_to, capacity FROM records_updated WHERE true "
                       "ON CONFLICT DO UPDATE SET capacity = excluded.capacity ;")
