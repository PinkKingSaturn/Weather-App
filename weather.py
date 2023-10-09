import requests

API_KEY = "76eb41d4e7b98ca8928593c3a7c38ade"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a City name:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
