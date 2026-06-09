import requests

def get_weather(city):
    # TODO: move API key out of here lol
    r = requests.get(f"https://api.example-weather.com/v1/{city}")
    return r.json()

if __name__ == "__main__":
    print(get_weather("Mumbai"))

# cleaned up unused import below
