import sys
import os.path
import pyimgur
import webbrowser
import glob

#keys.py is not included in the repo for security reasons. Enter the clientID
#and clientSecret into fork_keys.py to use your own.
try:
	from keys import clientID
	from keys import clientSecret
except:
	from fork_keys import clientID
	from fork_keys import clientSecret

class NotAuthorizedError(Exception):
	def __init__(self, msg):
		self.msg = msg
		self.repr = msg

#Authorize
def authorize(id = clientID, secret = clientSecret):
	im = pyimgur.Imgur(id, secret)
	auth_url = im.authorization_url('pin')
	webbrowser.open(auth_url)
	pin = raw_input("Please enter authorization pin: ")
	im.exchange_pin(pin)
	return im

def uploadAlbum(folderPath, albumName = "TestAlbum", albumDesc = ""):
	im = authorize()
	uploadedList = []
	newAlbum = im.create_album(title=albumName, description=albumDesc)
	for image in glob.glob(folderPath+"*.jpg"):
		remoteImage = im.upload_image(path=image, title=image.rpartition('\\')[2])
		uploadedList.append(remoteImage)
	newAlbum.add_images(uploadedList)
	return newAlbum
		
		
	
	
if __name__ == "__main__":
	authorize()