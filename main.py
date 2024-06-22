import requests
from datetime import datetime

TOKEN = "dsfdsafsD"
USERNAME = "arpan8925dey"
PIXELA_END = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
GRAPH_NAME = "Meditation Graph"
UNIT = "Days"

pixela_parameters = {
    "token": "dsfdsafsD",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=PIXELA_END, json=pixela_parameters)


GRAPH_END = f"{PIXELA_END}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": UNIT,
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_END, json=graph_parameters, headers=headers)

POST_END = f"{GRAPH_END}/{GRAPH_ID}"

today = datetime(year=2024 ,month=6 ,day=12)

date = today.strftime("%Y%m%d")

post_parameters = {
    "date": date,
    "quantity": "5",
}

# response = requests.post(url=POST_END, json=post_parameters, headers=headers)

# print(response.text)


UPDATE_DATA_END = f"{POST_END}/{date}"

update_data_params = {
    "quantity": "15"
}

# update_data = requests.put(url=UPDATE_DATA_END, json=update_data_params, headers=headers)

# print(update_data.text)

DELETE_DAYA_END = f"{POST_END}/{date}"

delete_data = requests.delete(url=DELETE_DAYA_END, headers=headers)

print(delete_data.text)