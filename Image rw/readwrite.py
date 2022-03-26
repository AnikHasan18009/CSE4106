import cv2
#reading image
i = cv2.imread('butterfly.jpg',0)

cv2.imshow('Butterfly',i)

cv2.waitKey(0)
#writing image
cv2.imwrite('copy.jpg',i)