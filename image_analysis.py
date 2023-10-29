import cv2
img = cv2.imread('test.jpg')
cv2.imshow('original',img)
cv2.waitKey(0)  # print original image #

# convert to grayscale

img_gray = cv2.cvtcolor(img, cv2.COLOR_BAYER_BG2GRAY)
cv2.imshow('gray',img_gray)
cv2.waitKey(0)