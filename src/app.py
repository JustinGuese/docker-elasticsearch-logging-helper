from quart import Quart, request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json
from os import environ
from elasticsearch import Elasticsearch

if environ.get("ES_USER") is not None and environ.get("ES_PW") is not None:
    user = str(environ.get("ES_USER"))
    pw = str(environ.get("ES_PW"))
    ES_AUTH = (user,pw)
    es = Elasticsearch("http://%s:9200" % environ["ES_HOST"], http_auth = ES_AUTH)
else:
    ES_AUTH = ()
    es = Elasticsearch("http://%s:9200" % environ["ES_HOST"])



app = Quart("Elastic Logger")

AUTH_PW = generate_password_hash(environ["AUTH_PW"])
environ["AUTH_PW"] = ""

def logged_in(msg):
    appname = msg["appname"]
    message = msg["errorjson"]
    msg = {"appname": appname, "error": message, "timestamp": datetime.now()}
    res = es.index(index="errors",  body=msg)
    return res["result"]

@app.route('/', methods=['POST'])
async def index():
    # receives json with 
    # appname
    # password
    # errorjson
    msg = await request.json
    try:
        if check_password_hash(AUTH_PW,msg["password"]):
            # correct password
            success = logged_in(msg)
            if success:
                return json.dumps({"code":200, "message": "success"})
            else:
                json.dumps({"code":500, "message": "insert into mongodb didnt work"})
        else:
            return json.dumps({"code": "401", "error":"incorrect password"})
    except Exception as e:
        msg = {
            "code": "500",
            "help" : "Endpoint expects json with: appname, password, errorjson",
            "error" : repr(e)
        }
        return json.dumps(msg)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')