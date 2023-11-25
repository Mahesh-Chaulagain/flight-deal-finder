import requests

SHEETY_ENDPOINT = "https://api.sheety.co/4d1e06c59a61424694f91d70d8e6c213/flightDeals/prices"

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # use sheety API to GET all the data in google sheet and print it out
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    # to update the google sheet with the IATA codes
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

