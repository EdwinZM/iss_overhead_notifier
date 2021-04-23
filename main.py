import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
IS_OVERHEAD = False

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead():
    if (iss_latitude >= MY_LAT - 5 and iss_latitude <= MY_LAT + 5) and (iss_longitude >= MY_LONG - 5 and iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

def is_night():
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if hour >= sunset or hour <= sunrise:
        return True
    else:
        return False

time_now = datetime.now()
hour = time_now.hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_overhead():
        if is_night():
            message = "Look up\n\nThe ISS is in the sky."
            user = "example@gmail.com"
            password = "*******"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=user, password=password)
                connection.sendmail(from_addr=user, to_addrs="example@hotmail.com", msg=message)






