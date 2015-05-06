import numpy as np #import numpy
import cv2 #import opencv
from matplotlib import pyplot as plt

plt.close('all') #close all open plots
cv2.destroyAllWindows()

img = cv2.imread('Dropbox/BE107_G2/Lab_5/Test_Images/frame0006.jpg',0)

"""
below defines images
"""
img_inv = 255 - img #invert image
thresh_value, img_thresh = cv2.threshold(img_inv, 90, 255, cv2.THRESH_BINARY_INV)
img_ad_thresh = cv2.adaptiveThreshold(img_inv, 255, \
cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 2)

"""
below defines contours
"""
img_cont = np.copy(img_inv)
contours, hierarchy = \
cv2.findContours(img_cont, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_cont, contours, -1, (128, 255, 0), 3)

img_cont_thresh = np.copy(img_thresh)
contours_thresh, hierarchy_thresh = \
cv2.findContours(img_cont_thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_cont_thresh, contours_thresh, -1, (128, 255,0), 3)

img_cont_ad = np.copy(img_ad_thresh)
contours_ad, hierarchy_ad = \
cv2.findContours(img_cont_ad, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_cont_ad, contours_ad, -1, (128, 255,0), 3)

"""
define arrays to add centers and radii to, run for loops to populate arrays
with centers (just centers for now, but could easily implement for radii)
"""
cont_centers = []
cont_radii = []
thresh_centers = []
thresh_radii = []
ad_centers = []
ad_radii = []

for i in range(len(contours)):
    cont_center, cont_radius = cv2.minEnclosingCircle(contours[i])
    cont_centers.append(cont_center)
for i in range(len(contours_thresh)):
    thresh_center, thresh_radius = cv2.minEnclosingCircle(contours_thresh[i])
    thresh_centers.append(thresh_center)
for i in range(len(contours_ad)):
    ad_center, ad_radius = cv2.minEnclosingCircle(contours_ad[i])
    ad_centers.append(ad_center)

"""
below plots imgs w/ contours
"""
plt.figure('Comparison of Methods')

#plt.subplot(2,3,1).axis('off') #create 2x2 grid of subplots, define 3 plot
#plt.title('no thresh')
#plt.imshow(img_inv, cmap='gray') #plot image
#
#plt.subplot(2,3,2).axis('off') #create 2x2 grid of subplots, define 3 plot
#plt.title('simple thresh')
#plt.imshow(img_thresh, cmap='gray') #plot image
#
#plt.subplot(2,3,3).axis('off') #create 2x2 grid of subplots, define 4 plot
#plt.title('adaptive thresh')
#plt.imshow(img_ad_thresh, cmap='gray') #plot image

plt.subplot(1,4,1).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('cont_none')
plt.imshow(img_cont, cmap='gray') #plot image
for i in range(len(cont_centers)):
    plt.plot(cont_centers[i][0], cont_centers[i][1], '.r')

plt.subplot(1,4,2).axis('off') #create 2x2 grid of subplots, define 1 plot
plt.title('cont_simple')
plt.imshow(img_cont_thresh, cmap='Blues') #plot image
for i in range(len(thresh_centers)):
    plt.plot(thresh_centers[i][0], thresh_centers[i][1], '.r')

plt.subplot(1,4,3).axis('off') #create 2x2 grid of subplots, define 2 plot
plt.title('cont_adaptive')
plt.imshow(img_cont_ad, cmap='Blues') #plot inverted image
for i in range(len(ad_centers)):
    plt.plot(ad_centers[i][0], ad_centers[i][1], '.r')


plt.show() #show image