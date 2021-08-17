import requests
import json

# this should be passed as env of course
LOGGINGURL = "http://127.0.0.1:5000"
APP_PASSWORD = "testitest"
APP_NAME = "testapp"

# just copy this part into your function
def log(errormessage):
    payload = json.dumps({
        "password": APP_PASSWORD,
        "appname": APP_NAME,
        "errorjson": errormessage
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", LOGGINGURL, headers=headers, data=payload)
    print(response.text)
    
# your function here
def boundToFail():
    array = [10, 50, 10, "ohnoooo"]
    for elem in array:
        try:
            elem = elem / 2
        except Exception as e:
            errormsg = {
                "error": str(repr(e)),
                "elemntWhereItHappened" : elem
            }
            log(errormsg)
            print("logged error: ",errormsg)
            # raise
            
boundToFail()