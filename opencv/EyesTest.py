import cv2

# 匯入辨識檔
eyes_cascade = cv2.CascadeClassifier('./xml/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    # 取得灰階圖樣
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # 偵測眼
    eyes = eyes_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        minNeighbors=15,  # 每個目標至少檢測到幾次以上，才可被認定是真數據(愈大愈準,但速度愈慢)。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print(eyes)

    # 在眼部四周繪製方形
    for (x, y, w, h) in eyes:                   # B  G  R  線的寬
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)

    # 顯示影像
    cv2.imshow('OpenCV', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
