import matplotlib.pyplot as plt
from database import fetch_all_summaries

def plot_daily_summaries():
    data = fetch_all_summaries()

    cities = set(row[0] for row in data)
    
    for city in cities:
        city_data = [row for row in data if row[0] == city]
        dates = [row[1] for row in city_data]
        avg_temps = [row[2] for row in city_data]

        plt.plot(dates, avg_temps, label=city)

    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.title('Daily Average Temperatures')
    plt.legend()
    plt.show()
