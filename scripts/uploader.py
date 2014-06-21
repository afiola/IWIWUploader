import sys
import os.path
import pyimgur
import webbrowser

#keys.py is not included in the repo for security reasons.
from keys import clientID
from keys import clientSecret


	
#Authorize
im = pyimgur.Imgur(clientID, clientSecret)
auth_url = im.authorization_url('pin')
webbrowser.open(auth_url)
pin = raw_input("Please enter authorization pin: ")
im.exchange_pin(pin)
im.create_album("This is a test album.", "For testing purposes.")

#Modify images

#Upload

#Get URLs

#Modify doc
