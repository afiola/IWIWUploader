import os
import os.path
import glob
import wand.image
 
def folderResize(folderPath, width, height):
    for img in glob.glob(os.path.join(folderPath,"*.jpg")):
        #print "Resizing " + img.rpartition('\\')[2]
        imgObj = wand.image.Image(filename=img)
        aspectRatio = float(width)/height
        #print "aspectRatio = " + str(aspectRatio)
        croppedHeight = int(round(imgObj.width/aspectRatio))
        #print "croppedHeight = " + str(croppedHeight)
        cropHeightStart = int((imgObj.height - croppedHeight)/2)
        cropString = str(imgObj.width) + 'x' + str(croppedHeight) + '+0+' + str(cropHeightStart)
        resizeString = str(width) + 'x' + str(height)
        imgObj.transform(crop=cropString, resize=resizeString)
        imgObj.save(filename = img)
        