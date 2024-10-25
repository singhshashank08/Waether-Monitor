from datetime import datetime

# Convert Kelvin to Celsius
def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

# Convert Unix timestamp to human-readable date
def unix_to_date(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d')

# Find dominant weather condition
def dominant_condition(conditions):
    return max(set(conditions), key=conditions.count)
