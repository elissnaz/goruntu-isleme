import cv2
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\USER\Downloads\ucak.png",0)

#Histogram, piksel parlaklıklarının dağılımı

#plt.hist(image.ravel(), 256, [0,256])
#plt.title("Histogram")
#plt.show() 

#120-150 arası göze çarpıyor

ret,thresh1=cv2.threshold(image,120,255,cv2.THRESH_BINARY)#ideal
ret,thresh2=cv2.threshold(image,120,100,cv2.THRESH_BINARY)
ret,thresh3=cv2.threshold(image,80,255,cv2.THRESH_BINARY)
ret,thresh4=cv2.threshold(image,200,200,cv2.THRESH_BINARY)
ret,thresh5=cv2.threshold(image,120,250,cv2.THRESH_BINARY)#ideal

cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()