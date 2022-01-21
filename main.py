import cv2
import winsound
cam =cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thrsh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dialated = cv2.dilate(thrsh, None, iterations=3)
    contours, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   #detects movement
    #  cv2.drawContours(frame1, contours, -1, (0,255,0), 2)    #detects display movement
    for c in contours:
         if cv2.contourArea(c) < 5000:
             continue

         x, y, w, h = cv2.boundingRect(c)
         cv2. rectangle(frame1, (x,y), (x+w,y+h), (0, 255, 0), 2)
         winsound.PlaySound('alert.wav', winsound.SND_ASYNC)


    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Cam', frame1)


