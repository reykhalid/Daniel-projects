import requests
from datetime import datetime
USERNAME = "reydaniel1997"
TOKEN = "abcdefghiklmnop"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPGH_ID = "graph1"
user_params = {

    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPGH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",

}
headers ={
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}"
today = datetime(year=2023, month=5, day=24)
pixel_data = {
    "date": today.strftime("20230524"),
    "quantity": "20",
}
#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)\
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}/{today.strftime('20230524')}"
put_pixel = {
    "quantity": "10"
}
#response = requests.put(url=update_endpoint, json=put_pixel, headers=headers)
#print(response.text)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPGH_ID}/{today.strftime('20230524')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)