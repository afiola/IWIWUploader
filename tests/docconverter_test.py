import os
import os.path
import unittest
import pyimgur
from iwiwuploader.keys import clientID
from iwiwuploader.keys import clientSecret
from iwiwuploader import docconverter

class TestConverter(unittest.TestCase):
    def test_docConvert(self):
        im = pyimgur.Imgur(clientID, clientSecret)
        testPath = os.path.join(os.environ['USERPROFILE'], "Pictures\\IWIWtest\\testdoc.txt")
        testAlbum = im.get_album("Jpc1N")
        docconverter.docConvert(docPath = testPath, album = testAlbum)
        with open(testPath, 'r') as docFile:
            lines = docFile.readlines()
            for image in testAlbum.images:
                found = False
                for line in lines:
                    if image.link in line and not found:
                        found = True
                        break
                if not found:
                    print image.link + " not found."
                self.assertTrue(found)
                
if __name__ == '__main__':
	unittest.main()