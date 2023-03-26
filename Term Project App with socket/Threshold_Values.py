# importing requests and json
import requests, json
import random


# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# API key
API_KEY = "857a04bf402d432f6d13307cee57d8e7"
# upadting the URL
URL = BASE_URL + "q=" + "&appid=" + API_KEY +"&lat=35.245919&lon=33.033941"


def get_random_numbers(temperature,humidity):
  num1 = random.randint(int(temperature*0.8), int(temperature*1.3))  # generates a random integer between 0 and 100
  num2 = random.randint(int(humidity*0.7), int(humidity*1.2))  # generates a random integer between 0 and 100
  return num1, num2

list_of_values = []

def thresholdForFire():
    list_of_values.clear()
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']

       #print(f"Temperature: {temperature}")
       #print(f"Humidity: {humidity}")
       #print(f"Pressure: {pressure}")
       #print(f"Weather Report: {report[0]['description']}")
       temperature_in_celsius = temperature - 273.15
       print(temperature_in_celsius,humidity)
       sensorTemperature,sensorHumidity= get_random_numbers(temperature_in_celsius,humidity)
       list_of_values.append(sensorTemperature)
       list_of_values.append(sensorHumidity) 
       if (sensorTemperature>temperature_in_celsius*1.1) or (sensorHumidity>humidity*0.9):
             #print("fire threshold exceeded")
             list_of_values.append(1)
             #print("list is {}".format(list_of_values))
             return list_of_values
       else:
        list_of_values.append(0)
    else:
      # showing the error message
      print("Error in the HTTP request")
    return list_of_values




if __name__ == "__main__":

    list2 = thresholdForFire()
    #print("list 2 is {}".format(list2))