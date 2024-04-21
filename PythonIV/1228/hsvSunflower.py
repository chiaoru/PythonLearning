import cv2
import numpy as np

img = cv2.imread('/opt/Python IV影像辨識與機器學習/2023/1228/sunflower.jpeg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

yellow = cv2.inRange(hsv_img, (15,34,0), (25,255,255))
#green = cv2.inRange(hsv_img, (36,0,0), (70,255,255))

output = cv2.bitwise_and(img, img, mask=yellow)

cv2.imshow('img', output)
cv2.waitKey() 
cv2.destroyAllWindows()
