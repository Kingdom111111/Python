import re
import pymysql
import requests
import time
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd


# Connect Mysql

db = pymysql.connect(host="localhost",port=3306,user="root",passwd="123456",db="stockDataBase",charset="utf8")
cursor = db.cursor()

# Get Data From Table
posi = pd.read_excel("insert.xlsx")
num = 60
_nameList = np.array(posi['Name'][0:num])
_ageList = np.array(posi['Age'][0:num])
_genderList = np.array(posi['Gender'][0:num])
_addrList = np.array(posi['Address'][0:num])

# 数组转List
_nameList = list(_nameList)
_ageList = list(_ageList)
_genderList = list(_genderList)
_addrList = list(_addrList)
print(_ageList)

for i in range(len(_addrList)):
    print(_ageList[i])
    try:
        #sql = "INSERT INTO A1(NAMEE,AGE,GENDER,ADDRESS) VALUES ('"+_nameList[i] +"',"+"'"+_ageList[i]+"',"+"'"+_genderList[i]+"',"+"'"+_addrList[i]+"'"+")"
        sql = "INSERT INTO A1(AGEE) VALUES ("+"'"+_ageList[i]+"'"+")"
        #sql = "INSERT INTO A1(NAMEE,AGE,GENDER,ADDRESS) VALUES ("+"'"+_nameList[i]+"',"+"'"+_ageList[i]+"',"+"'"+_genderList[i]+"',"+"'"+_addrList[i]+"'"+")"
        #print("电话交换机："+sql)
        print(sql)
        sql = sql.encode('utf-8')
        cursor.execute(sql)
        db.commit()
    except:print("999")
db.close()
#print("9999999999999999999")