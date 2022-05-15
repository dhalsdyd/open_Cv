import cv2

img = cv2.imread('winter.jpg')
img = cv2.resize(img,(1000,1000))

cv2.imshow("winter",img)


edge0 = cv2.Canny(img,50,80)
edge1 = cv2.Canny(img,50,100)
edge2 = cv2.Canny(img,100,150)
edge3 = cv2.Canny(img,150,200)

cv2.imshow('edge0',edge0)
cv2.imshow('edge1',edge1)
cv2.imshow('edge2',edge2)
cv2.imshow('edge3',edge3)
cv2.waitKey(0)

cv2.destroyAllWindows()