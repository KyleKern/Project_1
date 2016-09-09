import os
import io
import PIL
from PIL import Image
from statistics import median

#read files and assigns them to an array
image1 = Image.open("C:/Users/minve/Pictures/Project1Images/1.png")
image1.load()
image2 = Image.open("C:/Users/minve/Pictures/Project1Images/2.png")
image2.load()
image3 = Image.open("C:/Users/minve/Pictures/Project1Images/3.png")
image3.load()
image4 = Image.open("C:/Users/minve/Pictures/Project1Images/4.png")
image4.load()
image5 = Image.open("C:/Users/minve/Pictures/Project1Images/5.png")
image5.load()
image6 = Image.open("C:/Users/minve/Pictures/Project1Images/6.png")
image6.load()
image7 = Image.open("C:/Users/minve/Pictures/Project1Images/7.png")
image7.load()
image8 = Image.open("C:/Users/minve/Pictures/Project1Images/8.png")
image8.load()
image9 = Image.open("C:/Users/minve/Pictures/Project1Images/9.png")
image9.load()
jpgimage=[image1,image2, image3, image4, image5, image6, image7, image8, image9]
##sets picture width and height, already determinded because all 9 pictures are same size
pictureWidth=495
pictureHeight=557      
myImage=[]
##sorts each pixel color and then assigns it to the new picture for each spot in the list
new_im=Image.new("RGB",(495,557))
new_imdata=new_im.load()
#creating the new pixel
for x in range(0, pictureWidth):
    for y in range(0, pictureHeight):
        redPixelList=[]
        greenPixelList=[]
        bluePixelList=[]
        for myImage in jpgimage:
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
        sorted(redPixelList)
        sorted(greenPixelList)
        sorted(bluePixelList)
      
        new_imdata[x,y] = (int(median(redPixelList)),int(median(greenPixelList)),int(median(bluePixelList)))
            
##shows new image made from the other 9 images, and prints done upon completetion
new_im.show()
print("done")
