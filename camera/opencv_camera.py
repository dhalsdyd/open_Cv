import cv2

cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print('Camera open failed')
    exit()


#동영상 촬영
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Frame', frame)
    cv2.imshow("Grey",cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
    cv2.imshow("HSV",cv2.cvtColor(frame,cv2.COLOR_BGR2HLS_FULL))
    cv2.imshow("YUV",cv2.cvtColor(frame,cv2.COLOR_BGR2YUV))
    cv2.imshow("Canny",cv2.Canny(frame,50,100))
    cv2.imshow("Blur",cv2.blur(frame,(10,10)))
    
    #1000-> 1초 10->0.01초
    if cv2.waitKey(10) == ord('q'):
        break

cv2.waitKey(0)

#사용자 자원 해제 
cap.release()
cv2.destroyAllWindows()