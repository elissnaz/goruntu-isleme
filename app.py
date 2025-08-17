import cv2
import numpy as np

img  = cv2.imread(r"C:\Users\USER\Downloads\Image.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)

# Paralar beyaz, zemin siyah olsun:
_, mask = cv2.threshold(gray, 0, 255,
                        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Morfoloji işlemleri
ker = np.ones((5,5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, ker, 1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,  ker, 1)

H, W = img.shape[:2]
img_area = H * W

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#En büyük konturu bul
max_area = 0
largest_contour = None
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 200 < area < 0.95*img_area:  # filtreler
        if area > max_area:
            max_area = area
            largest_contour = cnt

# Tüm konturlar üzerinde dön
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 200 or area > 0.95*img_area:
        continue

    peri   = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.01*peri, True)

    # merkez
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
    else:
        cx, cy = approx[0][0]

    # basit sınıflandırma
    n = len(approx)
    if n == 3: name = "Triangle"
    elif n == 4:
        x,y,w,h = cv2.boundingRect(approx)
        ar = w/float(h)
        name = "Square" if 0.9 <= ar <= 1.1 else "Rectangle"
    elif n == 5: name = "Pentagon"
    elif 6 < n < 15: name = "Ellipse"
    else: name = "Circle"

    #  Çizim rengi: en büyükse kırmızı, değilse yeşil
    color = (0,0,255) if cnt is largest_contour else (0,255,0)
    cv2.drawContours(img, [approx], -1, color, 2)

    # Yazılar aynı
    cv2.putText(img, name, (cx, cy-18), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255,0,0), 2)
    cv2.putText(img, f"Area: {area:.0f}px^2", (cx, cy+4),  cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
    cv2.putText(img, f"Peri: {peri:.1f}px",   (cx, cy+22), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)

cv2.imshow("mask", mask)
cv2.imshow("result2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


