import requests
import json

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan döviz türü: ")
api_key = "e424786031-a37b3a2d2c-r8h5td"
api_url = f"https://api.fastforex.io/fetch-one?from={bozulan_doviz}&to={alinan_doviz}&api_key={api_key}"
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz?: "))

result = requests.get(api_url)
result = json.loads(result.text)
print(f'1 {bozulan_doviz} = {result["result"][alinan_doviz]} {alinan_doviz}\n{miktar} {bozulan_doviz} = {miktar*result["result"][alinan_doviz]} {alinan_doviz}')