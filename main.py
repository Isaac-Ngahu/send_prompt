import requests
import time
import psycopg2
from flask import json

connection = psycopg2.connect("postgresql://postgres:lAtarUsDfykfJQyTPxMfKaZvBzRNbJrd@junction.proxy.rlwy.net:26909/railway")

def insert_token():
    i=0
    while i<1:
        try:
            api = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
            time.sleep(2)
            session = requests.session()
            session.headers.update({'Content-Type': 'application/json','Authorization':'Basic REVBYjhjb3FBejZxYUV5N3FDS1Z6U2ZOWUViRkozQXRtYTE3TThmeW10VUM2T0dHOmNXR0pES0JHdnRnWVZER3RDd0R6a2JxOVhWQTR5YU16Qk9mMmVBMDhSV3N0Vm5OTjJHejFpb0FrSTlrTUdvcUE='})
            response = session.get(api)
            if len(response.json().get('access_token'))>1:
                cursor = connection.cursor()
                sql = 'INSERT INTO access_tokens(access_token) VALUES(%s)'
                value = (response.json().get('access_token'),)
                cursor.execute(sql,value)
                connection.commit()
                i = i+1
                print("inserted")
            else:
                print("no access token")
        except Exception as e:
            print(str(e))


