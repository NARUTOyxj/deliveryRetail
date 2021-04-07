from configs.config import HOST
import requests
class DataHandling:
    # 加密
    def encrypt(self,inData):
        url = f'{HOST}/openapi/test/e'
        payload = inData
        resp = requests.post(url,data=payload)
        return resp.text

        # 解密
    def decrypt(self,inData):
        url = f'{HOST}/openapi/test/d'
        payload = {"ciphertext":inData}
        resp = requests.post(url,data=payload)
        return resp.json()


if __name__ == '__main__':
    info = {"username": "13085555007","code": "1234","type": 1,"token": "", "os": "web","client": 2,"app_id": "UrWIgugv1m"}
    res = DataHandling().encrypt(info)
    print(type(res))
    res2 = DataHandling().decrypt(res)
    print(res2)