from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

sheet_data = data_manager.get_destination_data()

# if IATA column is empty pass each city name in sheet_data to flight search to get correspondinng IATA code
# for that city using the flight search API
# International Air Transport Association (IATA) code helps to identify airports and metropolitan areas

if sheet_data[0]["iataCode"] == "":     # check for "iatacode" is empty
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = datetime.now()
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )
    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                    f"to {flight.destination_city}-{flight.destination_airport},"
                    f"from {flight.out_date} to {flight.return_date}."
        )

