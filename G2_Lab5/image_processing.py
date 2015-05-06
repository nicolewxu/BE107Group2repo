#!/usr/bin/env python
# image_processing.py is bare-bones subscriber, in Object Oriented form. 
# If something is publishing to /camera/image_mono, it receives that 
# published image and writes "image received". 
# To run, use roslaunch on camera.launch or <bagfile>.launch and then, 
# in another terminal, type "python image_processing.py"
# Used in Lab 5 of BE 107 at Caltech
# By Melissa Tanner, mmtanner@caltech.edu, April 2015

import rospy
import cv2, cv 
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Image_Processor:
    def __init__(self):
       self.image_source = "/camera/image_mono"
       self.cvbridge = CvBridge()
       self.counter = 0

       # Raw Image Subscriber
       self.image_sub = rospy.Subscriber(self.image_source,Image,self.image_callback)

    def image_callback(self, rosimg):
        print "image recieved"
        self.counter +=1
        if self.counter%100 is 0: #changed from 10 to 15 (step 5), then to 100 (step 6)
            # Convert the image.
            try:
                 # might need to change to bgr for color cameras
                img = self.cvbridge.imgmsg_to_cv2(rosimg, 'passthrough')
            except CvBridgeError, e:
                rospy.logwarn ('Exception converting background image from ROS to opencv:  %s' % e)
                img = np.zeros((320,240))
            
            #invert img and apply adaptive thresh
            img_inv = 255 - img 
            img_ad_thresh = cv2.adaptiveThreshold(img_inv, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            img_cont_ad = np.copy(img_ad_thresh)
            contours_ad, hierarchy_ad = \
            cv2.findContours(img_cont_ad, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(img_cont_ad, contours_ad, -1, (128, 255,0), 3)

            print(len(contours_ad))

            xcoor_ad = np.empty(len(contours_ad))
            ycoor_ad = np.empty(len(contours_ad))
            rad_ad = np.empty(len(contours_ad))
            circle_ad = []
						
            for i in range(len(contours_ad)):
							(xcoor_ad[i], ycoor_ad[i]), rad_ad[i] = cv2.minEnclosingCircle(contours_ad[i])
							circle_ad.append(circle_ad)
							circles_ad = cv2.circle(img_ad_thresh, (np.uint8(xcoor_ad[i]), np.uint8(ycoor_ad[i])), np.uint8(rad_ad[i]),(0,255,0), 2)

            #Display
            cv2.namedWindow('img_ad_thresh', cv2.WINDOW_NORMAL)
            cv2.imshow('img_ad_thresh', img_cont_ad)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



################################################################################
def main():
  print "running"
  image_processor = Image_Processor()
  try:
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()     
  except KeyboardInterrupt:
    print "Shutting down"
  cv.DestroyAllWindows()

################################################################################
if __name__ == '__main__':
    rospy.init_node('image_processor', anonymous=True)
    main()
