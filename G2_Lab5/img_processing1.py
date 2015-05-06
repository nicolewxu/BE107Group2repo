import numpy as np
import cv2

img = cv2.imread('frame0006.jpg',0)
cv2.imshow('Group 2 Fly',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Group2Fly.png',img)
