import numpy as np #import numpy
import os
import cv2 #import opencv
from matplotlib import pyplot as plt

plt.close('all') #close all open plots
cv2.destroyAllWindows()

#arrange files for easier access
pics = dict()
for folder in ['fly_with_food_stills', 'larvae_stills']:
	pics[folder] = []
	allpics = 'videos_for_tracking/' + folder
	for root, dirs, filenames in os.walk(allpics):
		for file_name in filenames:
			filename = os.path.join('videos_for_tracking', folder, file_name)
			all_imgs = cv2.imread(filename, 0)
			pics[folder].append(all_imgs)
			output_filename = os.path.join('output', folder, file_name)
			cv2.imwrite(output_filename, all_imgs)

#invert images, apply thresholds, and find contours
for animal_type in pics.keys():
	for x in range(len(pics[animal_type])):
		img_inv = 255 - pics[animal_type][x] #invert
		#cv2.imshow('inverted imgs', img_inv)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		thresh_value, img_thresh = cv2.threshold(img_inv, 100, 255, cv2.THRESH_BINARY_INV)
		#cv2.imshow('thresh imgs', img_thresh)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		img_ad_thresh = cv2.adaptiveThreshold(img_inv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 2)
		#cv2.imshow('adapt thresh imgs', img_thresh)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()

		img_cont = np.copy(img_inv)
		contours, hierarchy = \
		cv2.findContours(img_cont, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img_cont, contours, -1, (128, 255,0), 3)
		cont_avg = np.average(img_cont)
		 
		img_cont_thresh = np.copy(img_thresh)
		contours_thresh, hierarchy_thresh = \
		cv2.findContours(img_cont_thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img_cont_thresh, contours_thresh, -1, (128, 255,0), 3)
		 
		img_cont_ad = np.copy(img_ad_thresh)
		contours_ad, hierarchy_ad = \
		cv2.findContours(img_cont_ad, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(img_cont_ad, contours_ad, -1, (128, 255,0), 3)

		#subtract bkgd
		cum_img = np.float64(pics[animal_type][0])	#cumulative images
		cum_img /= 255 #not all equal to one color

		#cv2.imshow('show initial cumulative image', cum_img_inv)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		
		weight = 1.0 / 6.0
		for z in range(6):
			for y in range(len(pics[animal_type])):
				cv2.accumulateWeighted(pics[animal_type][y]/255.0, cum_img, weight)
				pass
			cum_img_inv = 255 - cum_img
			diff = cv2.absdiff(cum_img_inv, np.float64(img_inv))
			
			thresh_value_bkgd, img_thresh_bkgd = cv2.threshold(np.uint8(diff), 90, 255, cv2.THRESH_BINARY_INV)

			img_cont_bkgd = np.copy(img_thresh_bkgd)
			contours_bkgd, hierarchy_bkgd = \
			cv2.findContours(np.uint8(img_cont_bkgd), mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
			cv2.drawContours(img_cont_bkgd, contours_bkgd, -1, (128, 255,0), 3)
			#cv2.imshow('show abs diff', diff - 200) #diff - 100 flies, diff - 200 larvae
			#cv2.waitKey(0)
			#cv2.destroyAllWindows()
			pass

		#cv2.imshow('show accum weighted img', cum_img_inv)
		#cv2.waitKey(0)

		#cv2.imshow('contours', img_cont)

			xcoor = np.empty(len(contours))
			ycoor = np.empty(len(contours))
			rad = np.empty(len(contours))
			circle = []
			for i in range(len(contours)):
				(xcoor[i], ycoor[i]), rad[i] = cv2.minEnclosingCircle(contours[i])
				circle.append(circle)
				cv2.circle(img_inv, (np.uint8(xcoor[i]), np.uint8(ycoor[i])), np.uint8(rad[i]),(0,255,0), 2)

			xcoor_thresh = np.empty(len(contours_thresh))
			ycoor_thresh = np.empty(len(contours_thresh))
			rad_thresh = np.empty(len(contours_thresh))
			circle_thresh = []
			for i in range(len(contours_thresh)):
				(xcoor_thresh[i], ycoor_thresh[i]), rad_thresh[i] = cv2.minEnclosingCircle(contours_thresh[i])
				circle_thresh.append(circle_thresh)
				circles_thresh = cv2.circle(img_thresh, (np.uint8(xcoor_thresh[i]), np.uint8(ycoor_thresh[i])), np.uint8(rad_thresh[i]),(0,255,0), 2)

			xcoor_ad = np.empty(len(contours_ad))
			ycoor_ad = np.empty(len(contours_ad))
			rad_ad = np.empty(len(contours_ad))
			circle_ad = []
			for i in range(len(contours_ad)):
				(xcoor_ad[i], ycoor_ad[i]), rad_ad[i] = cv2.minEnclosingCircle(contours_ad[i])
				circle_ad.append(circle_ad)
				circles_ad = cv2.circle(img_ad_thresh, (np.uint8(xcoor_ad[i]), np.uint8(ycoor_ad[i])), np.uint8(rad_ad[i]),(0,255,0), 2)

			xcoor_bkgd = np.empty(len(contours_bkgd))
			ycoor_bkgd = np.empty(len(contours_bkgd))
			rad_bkgd = np.empty(len(contours_bkgd))
			circle_bkgd = []
			for i in range(len(contours_bkgd)):
				(xcoor_bkgd[i], ycoor_bkgd[i]), rad_bkgd[i] = cv2.minEnclosingCircle(contours_bkgd[i])
				circle_bkgd.append(circle_bkgd)
				circles_bkgd = cv2.circle(img_thresh_bkgd, (np.uint8(xcoor_bkgd[i]), np.uint8(ycoor_bkgd[i])), np.uint8(rad_bkgd[i]),(0,255,0), 2)
		
	import time
	starttime = time.time()
	#.... do something
	now = time.time()		

filename = "test.txt"
filename = "Image"+i+".txt"
myfile = open(filename, "w")
myfile.write(data)
myfile.close()

plt.figure('Comparison of Methods')
plt.subplot(2,4,1).axis('off') #create 2x2 grid of subplots, define 3 plot
plt.title('no thresh')
plt.imshow(img_inv, cmap='gray') #plot image
plt.subplot(2,4,2).axis('off') #create 2x2 grid of subplots, define 3 plot
plt.title('simple thresh')
plt.imshow(img_thresh, cmap='gray') #plot image
plt.subplot(2,4,3).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('adaptive thresh')
plt.imshow(img_ad_thresh, cmap='gray') #plot image
plt.subplot(2,4,4).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('bkgd subtract')
plt.imshow(img_thresh_bkgd, cmap='gray') #plot image
plt.subplot(2,4,5).axis('off') #create 2x2 grid of subplots, define 4 plot
plt.title('cont_none')
plt.imshow(img_cont, cmap='gray') #plot image
plt.subplot(2,4,6).axis('off') #create 2x2 grid of subplots, define 1 plot
plt.title('cont_simple')
plt.imshow(img_cont_thresh, cmap='Blues') #plot image
plt.subplot(2,4,7).axis('off') #create 2x2 grid of subplots, define 2 plot
plt.title('cont_adaptive')
plt.imshow(img_cont_thresh, cmap='Blues') #plot image
plt.subplot(2,4,8).axis('off') #create 2x2 grid of subplots, define 2 plot
plt.title('cont_bkgd')
plt.imshow(img_cont_bkgd, cmap='Blues') #plot inverted image
	 
plt.show() #show image
