import cv2

image=cv2.imread(r"C:\Users\USER\Downloads\ucak.png",0)

ret,thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)

thresh1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# cv2.adaptiveThreshold parametreleri:
# 255 > maksimum beyaz değeri
# cv2.ADAPTIVE_THRESH_MEAN_C > Eşik değeri, komşuluk alanının ortalamasına göre belirlenir
# cv2.THRESH_BINARY > Çıktı siyah-beyaz olur
# 11 > Komşuluk alanı (blok boyutu, tek sayı olmalı)
# 2 > Hesaplanan ortalamadan çıkarılacak sabit

thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# Mean ile farkı: Komşuluk piksellerinin ortalaması yerine Gaussian ağırlıklı ortalama kullanılır
# kenar detaylarını daha net çıkarır.

cv2.imshow("original",image)
cv2.imshow("simple threshold",thresh)
cv2.imshow("mean",thresh1)
cv2.imshow("gaussian",thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()