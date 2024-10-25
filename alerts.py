import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import ALERT_EMAIL, TEMP_THRESHOLD, SMTP_CONFIG

def send_email_alert(city, temperature, condition):

    msg = MIMEMultipart()
    msg['From'] = SMTP_CONFIG['sender_email']
    msg['To'] = ALERT_EMAIL
    msg['Subject'] = f"Weather Alert for {city}!"

    # Email body content
    body = f"""
    Alert! The weather in {city} has triggered an alert.

    Current temperature: {temperature:.2f}°C
    Weather condition: {condition}

    Please take necessary actions if required.

    Regards,
    Weather Monitoring System
    """
    msg.attach(MIMEText(body, 'plain'))

    # SMTP server connection and sending the email
    try:
        with smtplib.SMTP(SMTP_CONFIG['smtp_server'], SMTP_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(SMTP_CONFIG['sender_email'], SMTP_CONFIG['sender_password'])
            server.sendmail(SMTP_CONFIG['sender_email'], ALERT_EMAIL, msg.as_string())
        print(f"Alert email sent to {ALERT_EMAIL} for {city}.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

def check_alerts(city, temperature, condition):
    """
    Checks if the weather data breaches the defined thresholds.
    Triggers an alert if a threshold is breached.
    """
    if temperature > TEMP_THRESHOLD:
        print(f"Temperature alert triggered in {city}: {temperature:.2f}°C")
        send_email_alert(city, temperature, condition)
