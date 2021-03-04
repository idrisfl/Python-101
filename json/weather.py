import requests

api_key = "your_api_key"
city = "Paris"
url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=" + api_key

request = requests.get(url)
json = request.json()
print(json)
