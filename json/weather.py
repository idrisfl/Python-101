import requests

api_key = "273a4fbe7b5155b5b70434d6b290540b"
city = "Paris"
url = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=" + api_key

request = requests.get(url)
json = request.json()
print(json)
