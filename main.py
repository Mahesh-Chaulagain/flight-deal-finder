from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

# if IATA column is empty pass each city name in sheet_data to flight search to get correspondinng IATA code
# for that city using the flight search API
# International Air Transport Association (IATA) code helps to identify airports and metropolitan areas

if sheet_data[0]["iataCode"] == "":     # check for "iatacode" is empty
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
