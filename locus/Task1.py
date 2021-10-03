import requests
import json
import datetime
import time
    

def replace_time(datetime_object):
    """ Replacing time with 4am for a particular date"""
    return datetime_object.replace(hour=4, minute=0, second=0)


def calculate_timestamp(datetime_object):
    """ Calculating the timestamp to put in the API as a Parameter"""
    return int(datetime.datetime.timestamp(datetime_object))


def get_timestamp(datetime_object):
    """ Method to Return the Timestamp, Required Arguments :- Datetime_object like 2020-02-01 00:10:12 0000"""
    yesterday = replace_time(datetime_object)
    return int(calculate_timestamp(yesterday))


def input_check(value):
  """ Method to check if Input Contains Degree Values in Lattitude and longitude """
  if value[-1] in ["N","E","W", "S"]:
    if value[-3] == "°":
      return value[:-3]
    elif value[-2] == "°":
        return value[:-2]
  else:
    return float(value)  


def main_execution(key):
    """ Main Execution to get latitude and longitude from the user to get the atmospheric Pressure """
    print("Welcome \n")
    print("Please Enter the Options Carefully to get the Pressure")
    print("Enter only Integer or Float values ex:- 28.7041, 77.1025 \n")
    try:
        latitude = input("Please Enter the Latitude of your location :-")
        latitude = input_check(latitude)
        print("\n")
        longitude = input("Please Enter the Longitude of your location :-")
        longitude = input_check(longitude)
        for i in range(1, 4):
            now = datetime.datetime.now()
            day = now - datetime.timedelta(days=i)
            timeStamp = get_timestamp(day)
            url = 'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'.format(
                latitude, longitude, timeStamp, key)
            response = requests.get(url)
            if response.status_code != 200:
                print("Free Quota Exhausted. Kindly Pay to Access OpenweatherAPI")
                break
            json_response = response.json()
            pressure = json_response.get("current").get("pressure")
            print("Atmospheric Pressure on ", day.date(), " at 4am", "is :- ", pressure)
            print("\n")
            time.sleep(2)
        print("Finished....")
    except Exception as e:
        print("Please Check Your input")
        print("Enter only Integer or Float values ex:- 1.122, 88 \n")
        main_execution(key)


if __name__ == '__main__':
    with open('api_key.json') as json_file:
        data = json.load(json_file)
        key = data['key'] 
        main_execution(key)