import requests
from datetime import datetime
import os
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 1.2
AGE = 25
APP_ID = "b1eae3b3"
API_KEY = "10d3f60e94fee7381a13531e791df26b"
TOKEN = "reydaniel1997"

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0dce85582ab1f8e2239bd4940a8eb2bf/trackingWorkout/sheet1"
excercise_text = input("tell me which exercise you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,

}
APP_ID = os.environ["APP_ID"] = "1eae3b3"
env = os.getenv("APP_ID")
print(env, type(env))
API_KEY = os.environ["API_KEY"] = "10d3f60e94fee7381a13531e791df26b"
TOKEN = os.environ["TOKEN"] = "reydaniel1997"
response = requests.post(url=excercise_endpoint, json=parameters, headers=headers)
sheet_endpoint = os.environ["sheet_endpoint"] = "https://trackapi.nutritionix.com/v2/natural/exercise"
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%x")

for excercise in result["exercises"]:
    Authorization_Header = {
        "Authorization": "Bearer reydaniel1997"

    }
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories":excercise["nf_calories"]

        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=Authorization_Header)
    print(sheet_response.text)

