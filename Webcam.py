#How to use webcam
import cv2
cap=cv2.VideoCapture(0)
cap.set(3,640)  # this defines the weidth of frame and from webcam id
cap.set(4,480)  # webcam id=4 for height
cap.set(10,100)  # id 10 is for brightness

while True:
    success, img=cap.read()
    cv2.imshow("Webcam",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(1) & 0xff ==ord('q'):        # ord is for exit while we type q key 
        break
