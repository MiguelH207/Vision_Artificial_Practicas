# Miguel Angel Huerta Castillo      21310236

import cv2
cap=cv2.VideoCapture(0)


while True:
    f,frame=cap.read()
    frame=cv2.Canny(frame,50,100)
    if f==True:
        cv2.imshow("canny",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else: print("No detecta camara")
cap.release()
cv2.destroyAllWindows()