folder ="C:\Users\minve\Pictures\Project1Images"

#Opens up each picture and creates a list of all of them.
pictures = []
myPicture1=makePicture(folder + "1.jpg")
pictures.append(myPicture1)
myPicture2=makePicture(folder + "2.jpg")
pictures.append(myPicture2)
myPicture3=makePicture(folder + "3.jpg")
pictures.append(myPicture3)
myPicture4=makePicture(folder + "4.jpg")
pictures.append(myPicture4)
myPicture5=makePicture(folder + "5.jpg")
pictures.append(myPicture5)
myPicture6=makePicture(folder + "6.jpg")
pictures.append(myPicture6)
myPicture7=makePicture(folder + "7.jpg")
pictures.append(myPicture7)
myPicture8=makePicture(folder + "8.jpg")
pictures.append(myPicture8)
myPicture9=makePicture(folder + "9.jpg")
pictures.append(myPicture9)

def medianOdd(myList):
  # Store list length in the variable listLength
  listLength = len(myList)
  # Sort the list
  sortedValues = sorted(myList)
  # Location of middle value. Add one because index starts at 0.
  middleIndex = (listLength + 1)/2
  # Return the object located at tha
  return sortedValues[middleIndex]
 
#The dimensions of each picture.  
width = 800
height = 530

#Creates a list for each color.
redPixelList = []
greenPixelList = []
bluePixelList = []

#Creates a new picture called canvas with the new width and height.
canvas=makeEmptyPicture(width,height)
#Goes through each picutre on the x axis
for x in range(0,width):
  #Goes through each picture on the y axis
  for y in range(0, height):
    #Goes through the list of pictures.
    for index in range(0,9):
      #JES getPixel function takes as input a picture object and coordinate pair 
      pixel = getPixel(pictures[index], x, y)
      red = getRed(pixel)      
      green = getGreen(pixel)
      blue = getBlue(pixel)
      redPixelList.append(red)
      greenPixelList.append(green)
      bluePixelList.append(blue)
    cpixel = getPixel(canvas, x, y)
    setColor(cpixel, makeColor(medianOdd(redPixelList), medianOdd(greenPixelList), medianOdd(bluePixelList)))
    #Including the pixel list for the color allows it so that it gets the values of the median values and remove the 
    #other values.
    redPixelList=[]
    greenPixelList=[]
    bluePixelList=[] 
 #Displays the new pixels to a new picture.   
show(canvas)
#Creates the picture to a new file.
writePictureTo(canvas,folder + "temp.png")
