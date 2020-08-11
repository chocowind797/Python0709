from time import sleep

max_floor = 101
print("有一棟 %d 層大樓的電梯系統, 運作如下:" % max_floor)
current_floor = 1
while True:
    try:
        target_floor = int(input("您現在在 %d 樓。請問要去哪一樓？\n>>> " % current_floor))
    except ValueError:
        print("格式錯誤!請輸入數字!\n")
        continue

    if not 1 <= target_floor <= max_floor:
        print("輸入錯誤,請輸入 1 ~ %d 樓" % max_floor)
        continue

    if target_floor > current_floor:
        print("正在上樓...")
        for i in range(current_floor+1, target_floor+1):
            sleep(1)
            print(i)
    elif target_floor < current_floor:
        print("正在下樓...")
        r = current_floor - target_floor
        for i in range(r):
            sleep(1)
            print(current_floor - i - 1)
    current_floor = target_floor
    sleep(0.5)
