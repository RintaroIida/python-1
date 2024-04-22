
# # 1レシートの合計金額の計算
# receipt = input().split()
# N = 0
# for i in range(len(receipt)):
#     N += int(receipt[i])

# print(N)



# 2ローマ字にするやつ
# import romkan
# def convert_to_roma(text):
#     roma_text = romkan.to_roma(text)
#     return roma_text
# def main():
#     text = "東京"
#     roma_text = convert_to_roma(text)
#     print(roma_text)
# main()

#2ローマ字にするやつ第二
# import pykakasi

# kks = pykakasi.kakasi()

# print(kks.convert("トウキョウ")[0]['kunrei'])


#顔認証
import cv2

# 画像ファイルのパス
image_path = 'FwgD_vIaAAAR60d.jpeg'
# OpenCVで画像を読み込む
image = cv2.imread(image_path)

# OpenCVの顔検出用の事前学習済み分類器のパス
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'

# 事前学習済みの顔検出器を読み込む
face_cascade = cv2.CascadeClassifier(cascade_path)

# 画像をグレースケールに変換する（顔検出はグレースケール画像で行う）
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔を検出する
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 顔を囲む資格を描画する
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# 結果を表示する
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
