import json
import requests
import pymysql
import datetime

def jsonDemo():
    data = {'name':'tome','age':13}
    jsonStr = json.dumps(data)
    print(jsonStr)
    jsonData = json.loads(jsonStr)
    print(jsonData)
    filew = open('data.json',"w+")
    json.dump(data,filew)
    filew.flush()
    filer = open('data.json','r+')
    jsonfiler = json.load(filer)
    print(jsonfiler)

def requestsDemo():
    response = requests.get('https://www.baidu.com/')
    print(response.status_code)
    print(response.content)
    print(response.headers)
    print(response.url)
    requestBody = {"operationType": "GET_SYSTEM_STATUS"}
    responseLeyan =requests.post('https://dev-api.leyanbot.com/xbizapi/233/system_config',json=requestBody)
    print(responseLeyan.status_code)
    print(responseLeyan.content)
    print(responseLeyan.headers)
    print(responseLeyan.url)
    print(responseLeyan.json())

def pymysqlDemo():
    db = pymysql.connect('10.24.1.169','education_rw','WuWyBrpkVwGPmJfx','x_education')
    cursor = db.cursor()
    cursor.execute("select * from login_name where login_name = 'oxm1s5ZT4Z8P7eZ0ffxdjVy-qqS4';")
    # data = cursor.fetchone()
    data = cursor.fetchall()
    print(data)

def datetimeDemo():
    print(datetime.datetime.now())
    print(datetime.datetime.utcnow())




# jsonDemo()
# requestsDemo()
# pymysqlDemo()
datetimeDemo()







