import numpy as np
import cv2;
img= cv2.imread("butterfly.jpg",0);
cv2.imshow('image',img);
#print(img.ndim)
#print(img)
cv2.waitKey(0);
cv2.destroyAllWindows()
brightness=round((np.sum(img))/(np.size(img)))
contrast=np.max(img)-np.min(img)
print("The brightness of the image is {}\nThe contrast of the image is {}".format(brightness,contrast))
