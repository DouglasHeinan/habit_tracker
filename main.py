import requests
from datetime import datetime
import os

USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
COLOR = "shibafu"
GRAPH_NAME = "reading_graph"
GRAPH_UNIT = "pages"
# TYPE should equal "int" or "float"
TYPE = "int"


def main():

    # This can be commented out because if only needs to run once to create the user.
    # parameters = {
    #     "token": TOKEN,
    #     "username": USERNAME,
    #     "agreeTermsOfService": "yes",
    #     "notMinor": "yes"
    # }
    #
    # pixela_endpoint = "https://pixe.la/v1/users"
    #
    # response = requests.post(url=pixela_endpoint, json=parameters)
    # print(response.text)

    # This can be commented out because if only needs to run once to create the graph.
    # graph_parameters = {
    #     "id": "graph1",
    #     "name": GRAPH_NAME,
    #     "unit": GRAPH_UNIT,
    #     "type": TYPE,
    #     "color": COLOR,
    # }
    #
    # headers = {
    #     "X-USER-TOKEN": TOKEN
    # }
    #
    # graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    #
    # response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
    # print(response.text)

    # ----------------PIXEL CREATOR---------------
    # today = datetime.now()
    #
    # pixel_parameters = {
    #     "date": today.strftime("%Y%m%d"),
    #     "quantity": "6",
    # }
    #
    # pixel_headers = {
    #     "X-USER-TOKEN": TOKEN
    # }
    #
    # pixel_endpoint = "https://pixe.la/v1/users/gruvis41/graphs/graph1"
    # response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=pixel_headers)
    # print(response.text)

    # ---------------PIXEL UPDATE---------------
    # Changes to make:
    # A few of these repeat variables (graph and username) should be saved to constants.
    # The yesterday variable needs to change based on the day.

    today = datetime.now()
    yesterday = datetime(year=2022, month=3, day=15)

    update_parameters = {
        "quantity": "4"
    }

    update_headers = {
        "X-USER-TOKEN": TOKEN
    }

    update_endpoint = f"https://pixe.la/v1/users/gruvis41/graphs/graph1/{yesterday.strftime('%Y%m%d')}"
    response = requests.put(url=update_endpoint, json=update_parameters, headers=update_headers)
    print(response.text)

    # yesterday = datetime(year=2022, month=3, day=14)
    #
    # update_headers = {
    #     "X-USER-TOKEN": TOKEN
    # }

    # update_endpoint = f"https://pixe.la/v1/users/gruvis41/graphs/graph1/{yesterday.strftime('%Y%m%d')}"
    # response = requests.delete(url=update_endpoint, headers=update_headers)
    # print(response.text)


if __name__ == '__main__':
    main()
