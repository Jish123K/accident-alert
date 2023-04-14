import time

import requests

from twilio.rest import Client

from io import BytesIO

from PIL import Image

import pytesseract

import re

def get_screenshot(url):

    response = requests.get(url)

    img = Image.open(BytesIO(response.content))

    return img

def extract_coordinates(text):

    pattern = r'\d+\.\d+'

    coordinates = re.findall(pattern, text)

    if len(coordinates) == 2:

        return coordinates[0], coordinates[1]

    return None

def generate_maps_url(coordinates):

    if coordinates:

        return f"https://www.google.com/maps/search/?api=1&query={coordinates[0]},{coordinates[1]}"

    return None

def send_location(url):

    account_sid = '#' # your twilio account id1

    auth_token = '#' # your twilio account token1

    client = Client(account_sid, auth_token) 

    message = client.messages.create( 

                                  from_='whatsapp:+1#', #twilio number1

                                  body=f"{url}",      

                                  to='whatsapp:+91#' #user phone number

                              )

    account_sid = '#' # your twilio account id2

    auth_token = '#'# your twilio account token2

    client = Client(account_sid, auth_token)

    message = client.messages \

          .create(

                     body=f"{url}",

                     from_='+1#',#twilio number1

                     to='+91#'#user phone number

                 )

def main():

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    url = 'http://192.168.43.1:8080/sensors.html'

    img = get_screenshot(url)

    img.save('web_screenshot1.png')

    text = pytesseract.image_to_string(img)

    coordinates = extract_coordinates(text)

    maps_url = generate_maps_url(coordinates)

    if maps_url:

        send_location(maps_url)

if __name__ == "__main__":

    main()

