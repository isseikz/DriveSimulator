# 車の運転シミュレータ
# 実行用プログラム
# Kuzumaki Issei

import model
import keyInput as key
import carImage



def main():
    # 自動車のモデルの作成
    car0 = model.Car()
    # 画像描画用のモデルの作成
    image = carImage.CarImage()
    cnt = 0
    while True:
        status, input = key.getInputWin32() # キー入力の取得と終了判定
        if status == 0:
            break

        t, state = car0.run(input)     # 入力
        print(state)
        if cnt % 10 == 0:
            image.updateFrom(state)        # 画像更新
        cnt += 1
    pass

if __name__ == '__main__':
    main()
