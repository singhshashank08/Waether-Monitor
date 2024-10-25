import requests
import schedule
import time
from config import API_KEY, BASE_URL, CITIES, UPDATE_INTERVAL
from database import insert_daily_summary
from utils import kelvin_to_celsius, unix_to_date, dominant_condition
from alerts import check_alerts

# Fetch real-time weather data
def fetch_weather_data(city):
    lat, lon = city['lat'], city['lon']
    response = requests.get(f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}")
    return response.json()

# Process and aggregate weather data
def process_weather_data():
    for city in CITIES:
        city_name = city['name']
        weather_data = fetch_weather_data(city)
        
        temp = kelvin_to_celsius(weather_data['main']['temp'])
        condition = weather_data['weather'][0]['main']
        timestamp = weather_data['dt']
        date = unix_to_date(timestamp)

        check_alerts(city_name, temp, condition)

        insert_daily_summary(city_name, date, temp, temp, temp, condition)
schedule.every(UPDATE_INTERVAL).seconds.do(process_weather_data)

while True:
    schedule.run_pending()
    time.sleep(1)
