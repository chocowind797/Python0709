import cv2

# 匯入辨識檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    # 取得灰階圖樣
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # 偵測笑容
    smile = smile_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        minNeighbors=300,  # 每個目標至少檢測到幾次以上，才可被認定是真數據(愈大愈準,但速度愈慢)。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    faces = face_cascade.detectMultiScale(
        gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
        scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
        minNeighbors=15,  # 每個目標至少檢測到幾次以上，才可被認定是真數據(愈大愈準,但速度愈慢)。
        minSize=(30, 30),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print(smile)

    # 在嘴部四周繪製方形
    for (x, y, w, h) in faces:  # B  G  R  線的寬
        for (x2, y2, w2, h2) in smile:
            if x + w > x2 > x and y + h > y2 > y:              # B  G  R  線的寬
                cv2.rectangle(frame, (x2, y2), (x2+w2, y2+h2), (255, 0, 0), 5)

    # 顯示影像
    cv2.imshow('OpenCV', frame)
    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
