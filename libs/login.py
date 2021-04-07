from configs.config import HOST
import requests
import json
from tools.dataHandling import *
class Login:
    def login(self,inData,getToken = False):
        url = f'{HOST}/openapi/user/login'
        payload = {"ciphertext":DataHandling().encrypt(inData)}
        res = requests.post(url,data=payload)
        decRes = DataHandling().decrypt(res.text)

        if getToken:
            return  decRes['data']['token']
        else:
            return decRes


if __name__ == '__main__':
    info = {
    "username": "13085555007",
    "code": "1234",
    "type": 1,
    "token": "",
    "os": "web",
    "client": 2,
    "app_id": "UrWIgugv1m"
    }
    resp = Login().login(info)
    print(resp)