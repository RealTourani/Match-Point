#region libraries
import cv2
import numpy as np
#endregion

#region process
def process(img_path,template_path): # This Function takes the path and name of basic image and template image
    img_bgr = cv2.imread(img_path) # read the image by opencv(cv2)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY) # convert the color of the image to gray

    img_template = cv2.imread(template_path,0) # read the template image(pattern)
    h,w = img_template.shape # it will get the height and width of the template image as h,w

    match = cv2.matchTemplate(img_gray, img_template, cv2.TM_CCOEFF_NORMED) # This function will compare the template image with input image to find the template image in input image by CCOEDD_NORMED Method

    threshold = 0.9 # we have to define a threshold for accuracy of matching

    loc = np.where(match >= threshold) # we use numpy to recognize the accuracy in found template in input image , we definded the accuracy (threshold)
    
    for points in zip(*loc[::-1]): # we need a loop to draw a rectangle for detected template and we need to zip the 'loc' to have all arrays together 
        
        img_bgr = cv2.rectangle(img_bgr, points, (points[0]+w ,points[1]+h), (0,255,0),1) # a rectangle will be drawn around the detected template

    cv2.imshow('result', img_bgr) # the result will be shown by opencv (cv2) 
#endregion




process('images/image.jpg', 'images/pattern.jpg') # You can call the function and enter its input arguments to perform the operation


cv2.waitKey(0)
cv2.destroyAllWindows()