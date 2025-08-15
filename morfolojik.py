import cv2
import numpy as np

image=cv2.imread(r"C:\Users\USER\Downloads\orijinal.png")

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)  #daraltma, gürültü temizleme
dilation=cv2.dilate(image,kernel,iterations=1) #aşındırma, nesneleri kalınlaştırmak 

erosion1=cv2.erode(image,kernel,iterations=1) 
opening=cv2.dilate(erosion1,kernel,iterations=1) #(e>d) daha güzel sonuç verir(opening)

dilation1=cv2.dilate(image,kernel,iterations=1)
closing=cv2.erode(dilation1,kernel,iterations=1)#closing(d>e)

cv2.imshow("original",image)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
