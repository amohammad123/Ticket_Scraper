import requests

url = 'https://ebooking.iranair.com/ibe/IR/availability/search?captchaInput='
data = {"rand": "2023-08-26T23:43:09+03:30", "uuid": "",
        "travelPaxInfo": {"adultCount": 1, "infantCount": 0, "paxQuantities": {"ADT": "1"}},
        "availabilitySearchType": "OW", "pqPref": {}, "searchedOnDInfos": [
        {"sequence": 1, "origin": {"airportCodes": ["THR"], "code": "THR", "isAirport": True},
         "destination": {"airportCodes": ["MHD"], "code": "MHD", "isAirport": True}, "selectedDepDateStr": "14/10/2023",
         "depDayVariance": "SameDay", "cabinClassCode": None}],
        "depOrigin": {"code": "THR", "airportCodes": ["THR"], "isAirport": True},
        "searchBehaviour": {"quotePriceForAllJourneys": True, "sameFareProductPerOnd": True},
        "anonymousUserDTO": {"carrierCode": "IR", "carrierID": 15, "selectedLanguage": "fa", "salesChannel": "WEB"},
        "searchRequestContext": {"modifyBookingContext": False}}
# data = {'travelPaxInfo':{'adultCount': 1, 'infantCount': 0},'searchedOnDInfos':[{'origin':{'airportCodes':['THR'], 'code':'THR'},'destination':{"airportCodes": ["MHD"], "code": "MHD"}, 'selectedDepDateStr':'14/10/2023"'}]}
res = requests.post(url, json=data).json()
print(res)
each_flight = res['result']['journeySegDTOs'][0]['journeySegDTOs'][0]
seat_ava_bool = res['result']['journeySegDTOs'][0]['journeySegDTOs'][0]['seatAvailability']
each_class_of_flight = res['result']['journeySegDTOs'][0]['journeySegDTOs'][0]['fareProductDetails'][0]
seat_ava_count = res['result']['journeySegDTOs'][0]['journeySegDTOs'][0]['fareProductDetails'][0]['availableSeatCount']
amount_each_class = res['result']['journeySegDTOs'][0]['journeySegDTOs'][0]['fareProductDetails'][0]['amount']
