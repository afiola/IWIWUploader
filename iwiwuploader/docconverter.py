import pyimgur
import os

def docConvert(docPath, album):
    with open(docPath+'~', 'a') as newFile:
        with open(docPath, 'r') as docFile:
            for line in docFile:
                newLine = line
                for remoteImage in album.images:
                    if ("[" + remoteImage.title + "]") in line:
                        newLine = line.replace(remoteImage.title, "IMG]"+remoteImage.link+"[/IMG")
                        print "Replacing " + remoteImage.title + " with " + remoteImage.link
                newFile.write(newLine)
    os.remove(docPath)
    os.renames(docPath + '~', docPath)