import glob
import os
import os.path
import unittest
import wand.image
from iwiwuploader import resizer
 
class TestResizer(unittest.TestCase):
	def test_FolderResize(self):
		testPath = os.path.join(os.environ['USERPROFILE'], "Pictures\\IWIWtest\\")
		resizer.folderResize(folderPath = testPath, width=853, height=480)
		for image in glob.glob(os.path.join(testPath,"*.jpg")):
			imageObj = wand.image.Image(filename=image)
			self.assertEquals(imageObj.width, 853)
			self.assertEquals(imageObj.height, 480)
			
			
if __name__ == '__main__':
	unittest.main()
				