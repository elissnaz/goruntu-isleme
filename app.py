import cv2
import numpy as np

image= cv2.imread(r"C:\Users\USER\Downloads\Image.png")
kernel=np.ones((5,5),np.uint8)

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#griye çevirme

_,thresh=cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)#eşikleme

erosion=cv2.erode(thresh,kernel,iterations=1) #opening(morfolojik)
opening=cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("result",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()

