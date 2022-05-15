import cv2

img = cv2.imread('winter.jpg')
img2 = cv2.resize(img,(1000,1000))

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow("winter",img2)
cv2.imshow("WinterGray",gray)

while True:
    if cv2.waitKey() == ord('q'):
        break
cv2.imwrite("../output/winterNormal.jpg",img2)
cv2.imwrite("../output/winterGray.jpg",gray)
cv2.destroyAllWindows()