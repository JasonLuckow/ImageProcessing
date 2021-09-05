'''
Author: Jason Luckow
Class: Image Processing
Professor: Dr. Hamed Sari-Sarraf
File name: Jason_Luckow_Project1.py
'''
import os
import cv2

# Obtain path to folder of images
pathToFolder = input("\nEnter the path to the folder of images: ")

# Verify path exists
while not os.path.exists(pathToFolder):
    pathToFolder = input("Incorrect path, try again: ")

# Iterate through folder
for image in os.listdir(pathToFolder):

    fullImgPath = pathToFolder + '\\' + image

    cvImage = cv2.imread(fullImgPath)

    # Convert to HSV
    hsvRange = cv2.cvtColor(cvImage, cv2.COLOR_BGR2HSV)

    hsvAverage = cv2.mean(hsvRange)

    saturation = hsvAverage[0]

    # Place day/night text
    if saturation > 1: 
        cv2.putText(cvImage, "Day", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)
    else:
        cv2.putText(cvImage, "Night", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # Display image
    cv2.imshow(str(image), cvImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()