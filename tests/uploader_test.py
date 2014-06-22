import unittest
import pyimgur
import glob
import os
import os.path
from iwiwuploader import uploader

class TestUploader(unittest.TestCase):
	def testAlbumUpload(self):
		testPath = os.path.join(os.environ['USERPROFILE'], "Pictures\\IWIWtest\\")
		album = uploader.uploadAlbum(testPath)
		self.assertIsNotNone(album)
		self.assertNotEqual(album.images, False)
		for image in glob.glob(os.path.join(testPath,"*.jpg")):
			fileName = image.rpartition('\\')[2]
			self.assertIn(fileName, [remoteImage.title for remoteImage in album.images])
		
if __name__ == '__main__':
	unittest.main()
	