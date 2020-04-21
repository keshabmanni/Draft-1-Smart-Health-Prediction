import requests
import json


def current_location():
    try:
        send_url = "http://api.ipstack.com/check?access_key=b652053a823bacc0fda4b403ffd99e03"
        geo_req = requests.get(send_url)
        if geo_req:
            geo_json = json.loads(geo_req.text)
            city = geo_json['city']
            if 'ā' in city:
                city = city.replace('ā', 'a')
            return city
        else:
            return 'Connection Problem!!'
    except:
        return 'Connection Problem!!'
