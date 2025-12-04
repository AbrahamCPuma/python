import requests
'''
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude,latitude)

print(iss_position)

'''
MY_LAT = 51.507351
MY_LNG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
my_dict = {}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
for key in data["results"]:
    if key == "sunrise" or key == "sunset":

        print(f"{key} : {data["results"][key]}")
        my_dict[key] = data["results"][key].split("T")[1].split(":")

print(my_dict)