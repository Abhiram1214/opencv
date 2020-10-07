import cv2
import numpy as np

'''
img = cv2.imread(r'C:\Users\cvenkatanagasatya\Pictures\Open CV\Computer-Vision-with-Python\DATA\puppy.jpg')

while True:
    cv2.imshow('puppy', img)
    #if we waited for milli second and we pressed the esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
'''


######################
#####Function#########
#####################

def draw_circle(event, x,y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        



cv2.namedWindow(winname='Images')  #this is connecting the below window to callback function
cv2.setMouseCallback('Images', draw_circle) #windows name with draw_circle





######################################
##### Showing images in OpenCV#########
#######################################


img = np.zeros((512,512,3), np.int8)

while True:
	cv2.imshow("Images", img)

	if cv2.waitKey(20) & 0xFF==27:
		break

cv2.destroyAllWindows()
