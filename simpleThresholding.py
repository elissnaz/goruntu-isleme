#Simple Thresholding
import cv2

#normalde renkli görsellerde RGB olmak üzere 3 kanal var
#thresholding uygularken tek kanala(0-255 arasında) indirmek daha net ve 
#hızlı nesne tespiti sağlar.

image=cv2.imread(r"C:\Users\USER\Downloads\ucak.png",0)# 0>>gri tonlama

# cv2.threshold() fonksiyonu:
# 1. Parametre: Girdi görüntüsü (gri olmalı)
# 2. Parametre: Eşik değeri (örneğin 120)
# 3. Parametre: Maksimum değer (örneğin 255>>beyaz)
# 4. Parametre: Threshold türü 

#eşik üstü beyaz(255), altı siyah(0) yapar
ret,thresh1=cv2.threshold(image,120,255,cv2.THRESH_BINARY) 
#eşik üstü siyah, altı beyaz
ret,thresh2=cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
#eşik üstü eşik değere sabitlenir, altı aynen kalır
ret,thresh3=cv2.threshold(image,120,255,cv2.THRESH_TRUNC)
#eşik altı siyah, üstü aynen kalır
ret,thresh4=cv2.threshold(image,120,255,cv2.THRESH_TOZERO)
#eşik üstü siyah, altı aynen kalır
ret,thresh5=cv2.threshold(image,120,255,cv2.THRESH_TOZERO_INV)


cv2.imshow("original",image)
cv2.imshow("thresh1",thresh1)
cv2.imshow("thresh2",thresh2)
cv2.imshow("thresh3",thresh3)
cv2.imshow("thresh4",thresh4)
cv2.imshow("thresh5",thresh5)


cv2.waitKey(0)
cv2.destroyAllWindows()