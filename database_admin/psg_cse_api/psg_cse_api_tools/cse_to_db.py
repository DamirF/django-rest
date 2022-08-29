import json
from datetime import datetime

from . import calc_func
from .db_queries_source import *
from .connection_to_database import create_connection


conn = ''


def insert_to_db(sending_user, sending_city, arrival_city, volume, weight, declared_value_rate, is_test):
    request_time = datetime.now()
    calc_func.create_request_cse(sending_city=sending_city,
                                 arrival_city=arrival_city,
                                 volume=volume,
                                 weight=weight,
                                 is_test=is_test,
                                 declared_value_rate=declared_value_rate
                                 )
    response_waiting_time = str((datetime.now() - request_time).total_seconds())
    connection = create_connection()
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(select_id)
        id_api = cursor.fetchall()

    if id_api == []:
        id_bd = 1
    else:
        id_bd = id_api[-1][-1]+1

    with connection.cursor() as cursor:
        if id_bd > 1:
            cursor.execute(select_request, (id_bd - 1, ))
            select_last_data = cursor.fetchone()
            print("Data select successfully")

    with connection.cursor() as cursor:
        if id_bd == 1:
            cursor.execute(insert_request,
                           (1,
                            json.dumps(calc_func.xml_data, ensure_ascii=False, indent=2),
                            calc_func.ready_response_calc,
                            request_time,
                            response_waiting_time,
                            int(sending_user)))
            print("Insert is successfully")
        elif id_bd > 1:
            cursor.execute(insert_request,
                           (id_bd,
                            json.dumps(calc_func.xml_data, ensure_ascii=False, indent=2),
                            calc_func.ready_response_calc,
                            request_time,
                            response_waiting_time,
                            int(sending_user)))
            print("Insert is successfully")

            cursor.execute(select_response, (id_bd,))
            select_next_data = cursor.fetchone()
            if select_next_data == select_last_data:
                print('No changes')


def send_calc_request(sending_user, sending_city, arrival_city, volume, weight, declared_value_rate, is_test):
    try:
        insert_to_db(sending_user=sending_user,
                     sending_city=sending_city,
                     arrival_city=arrival_city,
                     volume=volume,
                     weight=weight,
                     is_test=is_test,
                     declared_value_rate=declared_value_rate
                     )
    except Exception as _ex:
        print("[INFO]Error", _ex)
    finally:
        if conn:
            conn.close()
            print("[INFO]PostgreSQL connection close.")
