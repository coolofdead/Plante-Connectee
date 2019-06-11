# csv: name / temperature / air humidity / ground humidity / luminosity #

import requests
import json

from Login_Window import OpenWindow as OpenLoginWindow

"------------------------- FUNCTIONS -------------------------------"
def Connection(username, password):
    global api_json
    
    mydata["username"] = username
    mydata["password"] = password

    try:
        api_json = requests.post(url+para, data=mydata).json()
    except:
        return "Time out"

    if("error" in api_json):
        return "wrong username / password"
    else:
        return "succes"

def GetDevices():
    global api_json
    global mydata
    global url

    device_para = "v1/users/" + mydata["username"] + "/devices?authorization=" + api_json["access_token"]

    main_url = url + device_para
    return requests.get(main_url, params=mydata).json()

def SetDevice(device):
    global device_name
    device_name = device

def GetPlantData():
    global api_json
    global mydata
    global url
    global device_name
    global ressources

    datas = []
    for ressource in ressources:
        try:
            final_url = url + "v2/users/" + mydata["username"] + "/devices/" + device_name + ressource + "?authorization=" + api_json["access_token"]
            datas.append(requests.get(final_url).json())
        except:
            datas.append("error")
    return datas

"------------------------- VALUES -------------------------------"
mydata = {
        "Content-Type" : "application/x-www-form-urlencoded",
        "grant_type" : "password",
        "username" : "",
        "password" : ""
     }

url = "https://api.thinger.io/"
para = "oauth/token"

device_name = ""
ressources = ["TemperatureValue", "AirMoistureValue", "MoistureValue", "LuxValue"]

"------------------------- MAIN -------------------------------"
if(__name__ == "__main__"):
    OpenLoginWindow()
