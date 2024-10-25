API_KEY = "14bbeec3ddde70cb0413f5f673556127"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# List of cities with latitude and longitude
CITIES = [
    {"name": "Delhi", "lat": 28.6139, "lon": 77.2090},
    {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777},
    {"name": "Chennai", "lat": 13.0827, "lon": 80.2707},
    {"name": "Bangalore", "lat": 12.9716, "lon": 77.5946},
    {"name": "Kolkata", "lat": 22.5726, "lon": 88.3639},
    {"name": "Hyderabad", "lat": 17.3850, "lon": 78.4867}
]

UPDATE_INTERVAL = 300  # 5 minutes in seconds
TEMP_THRESHOLD = 35  # Degrees Celsius
ALERT_EMAIL = "recipient@example.com"

# SMTP server configuration for sending alerts (adjust as per your SMTP provider)
SMTP_CONFIG = {
    "smtp_server": "smtp.gmail.com",  # or your preferred SMTP server
    "smtp_port": 587,
    "sender_email": "singhshashank3084@gmail.com",
    "sender_password": "11223344"  
}
