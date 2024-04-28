# calling pandas for data manipulation
import pandas as pd
# calling pprint and Request for API Calls
from pprint import pprint
import requests
import mysql.connector

URL = 'https://discosweb.esoc.esa.int'
token = 'ImUwYzQ2YTk1LWIzODQtNDVlYi1hNjUzLTAzZjAxYzEwYjI5NSI.A2EkjCeiipEzbpiP1hybmPOAP3o'

page = 1
doc = {}
first_run = 1

if (first_run == 0):
    while (page < 1):  # 262 total pages
        response = requests.get(
            f'{URL}/api/objects?page%5Bsize%5D=100&page%5Bnumber%5D={page}',
            headers={
                'Authorization': f'Bearer {token}',
                'DiscosWeb-Api-Version': '2',
            },
            params={
                'filter': "and(cosparId=ne=null,mass=ne=null)"
            }
        )
        if response.status_code == 200:
            data = response.json()
            doc[page] = data
        # else:
            # print(f"Error: {response.status_code}")
            # break

        page += 1

    data_list = [item['attributes'] for page_data in doc.values()
                 for item in page_data['data']]

    df = pd.DataFrame(data_list)

    df
    first_run = 1
else:
    response = requests.get(
        f'{URL}/api/objects?page%5Bsize%5D=100&page%5Bnumber%5D=1',
        headers={
            'Authorization': f'Bearer {token}',
            'DiscosWeb-Api-Version': '2',
        },
        params={
            'filter': "and(cosparId=ne=null,mass=ne=null)"
        }
    )
    if response.status_code == 200:
        data = response.json()
        doc = data

    data_list = [item['attributes'] for page_data in doc.values()
                 for item in page_data['data']]

    df = pd.DataFrame(data_list)


connection = mysql.connector.connect(
    host='localhost',
    user='babb',
    password='C^3M8fsvXbaW',
    database='DISCOS'
)

cursor = connection.cursor()

sql = "SELECT * FROM Objects"
cursor.execute(sql)

results = cursor.fetchall()

columns = [column[0] for column in cursor.description]
sql_df = pd.DataFrame(results, columns=columns)

differences = df.merge(sql_df, indicator=True, how='left')
differences = differences[differences['_merge'] == 'left_only']

if not differences.empty:
    insert_cursor = connection.cursor()

    for _, row in differences.iterrows():
        values = tuple(row.values)

        insert_sql = "INSERT INTO Objects (xSectMax, vimpelId, xSectAvg, name, diameter, depth, mass, span, cosparId, satno, height, width, xSectMin, shape, objectClass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        insert_cursor.execute(insert_sql, values)

    connection.commit()
    insert_cursor.close()

connection.close()
