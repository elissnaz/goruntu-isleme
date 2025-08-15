import cv2

image=cv2.imread(r"C:\Users\USER\Downloads\ucak.png",0)

ret,thresh=cv2.threshold(image,120,255,cv2.THRESH_BINARY)
ret1,thresh1=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#otomatik 0-255 arası eşik değeri tespit eder (otsu)

cv2.imshow("original",image)
cv2.imshow("simple threshold",thresh)
cv2.imshow("otsu",thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()