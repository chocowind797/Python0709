import cv2
import os

# 匯入辨識檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

img = '2'
frame = cv2.imread('./image/%s.jpg' % img)

# 取得灰階圖樣
gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

# 偵測笑容
smile = smile_cascade.detectMultiScale(
    gray,  # 待檢測圖片，一般為灰度圖像加快檢測速度
    scaleFactor=1.1,  # 檢測粒度 scaleFactor 。更大的粒度將會加快檢測的速度，但是會對檢測準確性產生影響。相反的，一個更小的粒度將會影響檢測的時間，但是會增加準確性。
    minNeighbors=5,  # 每個目標至少檢測到幾次以上，才可被認定是真數據(愈大愈準,但速度愈慢)。
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
for (fx, fy, fw, fh) in faces:
    for (sx, sy, sw, sh) in smile:
        if fx + fw > sx > fx and fy + fh > sy > fy:
            cv2.putText(frame, 'smile', (sx, sy-7), 2, 1.2, (255, 0, 0), 2)
            cv2.rectangle(frame, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
        else:
            cv2.putText(frame, 'no smile', (0, 23), 2, 0.8, (0, 0, 255), 1)

# 顯示影像
cv2.imshow('OpenCV', frame)

if not os.path.exists('./result'):
    os.mkdir('./result')
cv2.imwrite('./result/%s.jpg' % img, frame)

cv2.waitKey(0)

cv2.destroyAllWindows()
