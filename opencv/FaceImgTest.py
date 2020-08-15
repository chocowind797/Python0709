import cv2

# 匯入辨識檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

frame = cv2.imread('./image/tzuyu.jpg')

# 取得灰階圖樣
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# 偵測臉
faces = face_cascade.detectMultiScale(
    gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
    scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
    minNeighbors=4,  # 每個目標至少檢測到幾次以上，才可被認定是真數據(愈大愈準,但速度愈慢)。
    minSize=(1, 1),  # 設定數據搜尋的最小尺寸 ，如 minSize=(30,30)
    flags=cv2.CASCADE_SCALE_IMAGE
)

print(faces)

# 在臉部四周繪製方形
for (x, y, w, h) in faces:                  # B  G  R  線的寬
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

# 顯示影像
cv2.imshow('OpenCV', frame)

# 按下任意鍵離開
c = cv2.waitKey(0)

cv2.destroyAllWindows()
