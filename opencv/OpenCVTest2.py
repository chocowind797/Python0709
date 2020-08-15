import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    print(ret, frame)
    cv2.imshow('OpenCV', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# cap.destroyAllWindows()
