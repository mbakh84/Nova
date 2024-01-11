import cv2
import numpy as np
import matplotlib.pyplot as plt

images_List = []
Raw_template = input('enter template image address : ')
images_List.append(Raw_template)
while True:
    images = input('please enter image address : ')
    images_List.append(images)
    ask = int(input('Do you have another picture?(1/0) : '))
    if ask == 0:
        break

chartList = []

template = cv2.imread(Raw_template, 0)
for picture in images_List:
    img_rgb = cv2.imread(picture)
    gray_img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    main_gray_img = cv2.imread(picture, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.65
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        crp_img = main_gray_img[pt[1]:pt[1] + h, pt[0]:pt[0] + w]

    Y = template.shape[0]
    X = template.shape[1]
    Yb = -1
    Xa = -1
    LBT = 0
    CBT = 0
    while Yb < int(((Y - 1) / 10)):
        Yb += 1
        while Xa < X - 1:
            Xa += 1
            px = template[Yb, Xa]
            LBT += px
            CBT += 1
        Xa = 0
    Yb = int(Y - ((Y - 1) / 10))
    while Yb < Y - 1:
        Yb += 1
        while Xa < X - 1:
            Xa += 1
            px = template[Yb, Xa]
            LBT += px
            CBT += 1
        Xa = 0

    Y = crp_img.shape[0]
    X = crp_img.shape[1]
    Yb = -1
    Xa = -1
    LBC = 0
    CBC = 0
    while Yb < int(((Y - 1) / 10)):
        Yb += 1
        while Xa < X - 1:
            Xa += 1
            px = crp_img[Yb, Xa]
            LBC += px
            CBC += 1
        Xa = 0
    Yb = int(Y - ((Y - 1) / 10))
    while Yb < Y - 1:
        Yb += 1
        while Xa < X - 1:
            Xa += 1
            px = crp_img[Yb, Xa]
            LBC += px
            CBC += 1
        Xa = 0
    Light_pollution_Coefficient = LBT / LBC

    Y = crp_img.shape[0]
    X = crp_img.shape[1]
    Yb = -1
    Xa = -1
    Raw_Lighting = 0
    while Yb < Y - 1:
        Yb += 1
        while Xa < X - 1:
            Xa += 1
            px = crp_img[Yb, Xa]
            Raw_Lighting = Raw_Lighting + px
        Xa = 0

    processed_Lighting = round(Raw_Lighting * Light_pollution_Coefficient, 5)
    chartList.append(processed_Lighting)

yChart = []
xChart = []
n = 0
for char in chartList:
    yChart.append(char)
    xChart.append(1 + n)
    n += 1
plt.ylabel('Lighting')
plt.xlabel('picture number')
plt.plot(xChart, yChart)
print(f"\a")
plt.show()

print(f"{X * Y} pixels scanned in each picture")
print(f"{CBT} pixels scanned in Border of each picture")
cv2.imshow("pat", template)
cv2.imshow("11", crp_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
