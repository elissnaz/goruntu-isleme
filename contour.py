import cv2
import numpy as np

img = cv2.imread(r"C:\Users\USER\Downloads\ornek.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(img_gray, 245, 255, cv2.THRESH_BINARY_INV)

#kontür bulma
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

colors = {
    "Triangle": (0, 255, 255),   # Sarı
    "Rectangle": (255, 0, 0),    # Mavi
    "Pentagon": (0, 0, 255),     # Kırmızı
    "Ellipse": (0, 255, 0),      # Yeşil
    "Circle": (255, 0, 255)      # Pembe
}

# En büyük şekil bilgisi
max_area, best = 0, None

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 50: #küçük görüntüleri elemek
        continue
    peri = cv2.arcLength(cnt, True)#çevre
    approx = cv2.approxPolyDP(cnt, 0.01*peri, True)#köşe sayılarına göre yaklaşım

    #kütle merkezi
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = approx[0][0]

    # Şekil adı
    name = "Circle"
    if len(approx) == 3: name = "Triangle"
    elif len(approx) == 4: name = "Rectangle"
    elif len(approx) == 5: name = "Pentagon"
    elif 6 < len(approx) < 15: name = "Ellipse"

    cv2.drawContours(img, [approx], -1, colors[name], 2)# kontur çizme

    # isim , alan, çevre yazısı
    cv2.putText(img, f"{name}", (cx, cy-18), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0), 2)
    cv2.putText(img, f"Area: {area:.0f}px^2", (cx, cy+4), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(img, f"Peri: {peri:.1f}px",  (cx, cy+22), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

    if area > max_area:
        x,y,w,h = cv2.boundingRect(approx)
        best = {"crop": img[y:y+h, x:x+w].copy(),
                "name": name, "area": area, "peri": peri}

# En büyük şekil için ayrı görsel oluştur
if best:
    panel = best["crop"].copy()
    h = panel.shape[0] + 100
    w = max(panel.shape[1], 250)
    info = np.ones((h, w, 3), dtype=np.uint8)*255
    info[0:panel.shape[0], 0:panel.shape[1]] = panel

    y0 = panel.shape[0] 
   

    cv2.imshow("Largest Shape", info)

cv2.imshow("All Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
