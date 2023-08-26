import requests


class FlightBot:
    def __init__(self):
        self.url = 'https://apps.qeshm-air.com/api/Res/FlightAvailability?OfficeUser=Arbaeen32&OfficePass=QXJiYWVlbjMyXzIwMjMtMDgtMjYgMTI6NDY6Mjg='
        self.params = {'OfficeUser': 'Arbaeen32', 'OfficePass': 'QXJiYWVlbjMyXzIwMjMtMDgtMjYgMTI6NDY6Mjg='}

    def ticket_detail(self):
        result = []
        index = 0
        data = get_detail()
        response = requests.post(self.url, json=data).json()['AvailableFlights']

        for res in response:
            item = {}
            index += 1
            item['index'] = index
            item['air_type'] = res['AircarftTypeNameFA']
            item['flight_no'] = res['FlightNo']
            item['departure_date_time'] = res['DepartureDateTime']
            item['arrival_date_time'] = res['ArrivalDateTime']
            item['meal'] = res['Meal']

            classes_options = []
            for detail in res['ClassStatus']:
                classes = {}
                classes['cobin_class'] = detail['CabinClass']
                classes['price'] = detail['TotalPrice']
                classes['sort_index'] = detail['SortIndex']
                classes_options.append(classes)
            item['classes'] = classes_options

            result.append(item)

        return result


def get_detail():
    data = {}
    origin_airports_name = '1-امام خمینی - 2-مشهد - 3-نجف - 4-کرمانشاه - 5-بندرعباس - 6-قشم'
    print(f'فرودگاه های مبدا: {origin_airports_name}')
    origin = input('مبدا ').strip()
    get_airports = origin_airports(airport_number=origin)
    data['Origin'] = get_airports['origin_name']
    print(f"فرودگاه های مقصد: {get_airports['destination_airports']}")
    destination = input('مقصد ').strip()
    get_des_airports = destination_airports(destination_status=destination, origin_status=origin)
    data['Destination'] = get_des_airports
    date = input('تاریخ حرکت  <<نمونه: 08-05-1402>> ').strip()
    data['Date'] = date
    adult_no = input('تعداد بزرگسال <<+12 سال>> ').strip()
    data['AdultNo'] = int(adult_no)
    child_no = input('تعداد کودک <<12-2 سال>> ').strip()
    data['ChildNo'] = int(child_no)
    infantNo = input('تعداد نوزاد <<تا دو سال>>').strip()
    data['InfantNo'] = int(infantNo)
    return data


def origin_airports(airport_number):
    origin_name = ''
    destination_airports = ''

    if airport_number == '3':
        origin_name = 'NJF'
        destination_airports = '1-امام خمینی - 2-مشهد - 3-کرمانشاه - 4-بندرعباس - 5-قشم'
    else:
        if airport_number == '1':
            origin_name = 'IKA'
        elif airport_number == '2':
            origin_name = 'MHD'
        elif airport_number == '4':
            origin_name = 'KSH'
        elif airport_number == '5':
            origin_name = 'BND'
        elif airport_number == '6':
            origin_name = 'GSM'
        destination_airports = '1-نجف'
    return {'origin_name': origin_name, 'destination_airports': destination_airports}


def destination_airports(destination_status, origin_status):
    destination_name = ''
    if origin_status != '3':
        destination_name = 'NJF'

    else:
        if destination_status == '1':
            destination_name = 'IKA'
        elif destination_status == '2':
            destination_name = 'MHD'
        elif destination_status == '3':
            destination_name = 'KSH'
        elif destination_status == '4':
            destination_name = 'BND'
        elif destination_status == '5':
            destination_name = 'GSM'
    return destination_name


if __name__ == '__main__':
    print(FlightBot().ticket_detail())
