# Waether-Monitor



Real-Time Weather Monitoring and Alert System
This project is a real-time weather monitoring system that fetches data from the OpenWeatherMap API at configurable intervals to track weather conditions across major metro cities in India. The system provides summarized daily weather insights, triggers alerts when specific conditions are met, and visualizes historical trends.

Table of Contents
Features
Technologies Used
Configuration
Getting Started
Usage
Project Structure
Future Improvements
Features
Real-Time Weather Data: Continuously fetches weather data for specified Indian cities.
Data Processing: Converts temperatures from Kelvin to Celsius and stores daily weather summaries.
Alert System: Configurable temperature and condition-based alert system with email notifications.
Historical Visualization: Graphs daily average temperature trends over time.
Extendable Design: Easily add more cities or weather parameters for monitoring.
Technologies Used
Python: Core language for data processing and API calls.
SQLite: Local storage for daily weather summaries.
OpenWeatherMap API: Source for real-time weather data.
Matplotlib: Visualization of historical trends.
SMTP: Email alerts for threshold breaches.
Configuration
OpenWeatherMap API Key: Sign up for a free API key from OpenWeatherMap.
SMTP Credentials: Required for email notifications. You may use a Gmail account with an app-specific password.
In the config.py file, replace placeholders as per your setup:

API_KEY: Your OpenWeatherMap API key.
ALERT_EMAIL: The recipient’s email for weather alerts.
TEMP_THRESHOLD: Temperature threshold to trigger alerts.
SMTP_CONFIG: SMTP server details for sending email alerts.


Getting Started
Clone the Repository:

bash

git clone https://github.com/your-username/real-time-weather-monitoring.git
cd real-time-weather-monitoring
Install Dependencies: Ensure you have Python and pip installed, then install the required libraries:

bash

pip install -r requirements.txt
Create the Database: Initialize the SQLite database by running:

bash

python -c "import database; database.create_db()"
Configure API and Email Settings: Update config.py with your OpenWeatherMap API key and SMTP settings.

Usage
Run the Main Application:

bash

python app.py
The application will start fetching weather data every 5 minutes (default interval). If the temperature in any city exceeds the threshold, an email alert will be sent.

Plot Historical Data: To visualize the collected weather data, run:

bash

python -c "import visualizations; visualizations.plot_daily_summaries()"
Project Structure
app.py: Main application for data retrieval, processing, and alerting.
config.py: Configuration file for API keys, alert settings, and SMTP credentials.
database.py: SQLite database setup and handling for weather data.
alerts.py: Alert logic to send emails if thresholds are breached.
utils.py: Helper functions, including temperature conversion and date formatting.
visualizations.py: Generates visualizations for daily summaries and trends.
Future Improvements
Additional Weather Parameters: Extend the system to monitor more parameters (e.g., humidity, wind speed).
User Interface: Create a web-based dashboard for real-time monitoring and historical data visualization.
SMS Alerts: Integrate SMS alerts using a service like Twilio.
Forecast Data: Incorporate forecast data to trigger alerts based on predicted conditions.
