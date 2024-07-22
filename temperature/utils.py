import requests
from dotenv import load_dotenv
import os
load_dotenv()

WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")


def get_current_temperature(city_name: str) -> float:
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city_name}"
    print(url)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_temperature = data["current"]["temp_c"]
        return current_temperature
    else:
        print("Failed to retrieve temperature data")
        return 666
    

if __name__ == "__main__":
    print(get_current_temperature("Kyiv"))