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

ad_centers = np.empty(len(contours_ad))
ad_radii = np.empty(len(contours_ad))
ad_center, ad_radius = cv2.minEnclosingCircle(contours_ad[215])

#for i in range(len(contours_ad)):
#    ad_centers[i], ad_radii[i] = cv2.minEnclosingCircle(contours_ad[i])
#np.append


"""
below plots imgs w/ contours
"""
plt.figure('Comparison of Methods')
plt.subplot(2,3,1).axis('off') #create 2x2 grid of subplots, define 3 plot
plt.title('no thresh')
plt.imshow(img_inv, cmap='gray') #plot image
plt.subplot(2,3,2).axis('off') #create 2x2 grid of subplots, define 3 plot
plt.title('simple thresh')
plt.imshow(img_thresh, cmap='gray') #plot image
plt.subplot(2,3,3).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('adaptive thresh')
plt.imshow(img_ad_thresh, cmap='gray') #plot image
plt.subplot(2,3,4).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('cont_none')
plt.imshow(img_cont, cmap='gray') #plot image
plt.subplot(2,3,5).axis('off') #create 2x2 grid of subplots, define 1 plot
plt.title('cont_simple')
plt.imshow(img_cont_thresh, cmap='Blues') #plot image
plt.subplot(2,3,6).axis('off') #create 2x2 grid of subplots, define 2 plot
plt.title('cont_adaptive')
plt.imshow(img_cont_ad, cmap='Blues') #plot inverted image
#plt.plot(center[0], center[1], '.r')


plt.show() #show image