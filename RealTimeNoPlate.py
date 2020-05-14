import cv2

NumberPlateCascade =cv2.CascadeClassifier("Temp/NumberPlate.xml")

cap=cv2.VideoCapture(0)
cap.set(3, 640)  # this defines the weidth of frame and from webcam id
cap.set(4, 480)  # webcam id=4 for height
cap.set(10, 100)  # id 10 is for brightness

while True:
    success, img = cap.read()
    PGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Plate=NumberPlateCascade.detectMultiScale(PGray, 1.1, 4)

    for x,y,w,h in Plate:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("No. Plate", img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
