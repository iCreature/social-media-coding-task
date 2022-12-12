from flask import Flask, render_template
import requests
import json
import threading
import os 
import time


app = Flask(__name__)


theRebel ="https://takehome.io/twitter"
theChild = "https://takehome.io/instagram"
theParent = "https://takehome.io/facebook"

jsonResponse = {}

@app.route("/",methods=['GET'])
def social_network_activity():
    rebelResponse = threading.Thread(target=activity("Twitter",theRebel))
    childResponse = threading.Thread(target=activity("Instagram",theChild))
    parentResponse = threading.Thread(target=activity("Facebook",theParent))

    rebelResponse.start()
    childResponse.start()
    parentResponse.start()

    rebelResponse.join()
    childResponse.join()
    parentResponse.join()
    
    return render_template('index.html', data = jsonResponse)

    
def activity(pName,pUrl):
    try:
        data = requests.get(pUrl)
        jsonR = json.loads(data.content)
        time.sleep(2)
        jsonResponse[pName] = jsonR
    except:
        pass

if __name__ == "__main__":
    app.run(threaded=True,debug = True)