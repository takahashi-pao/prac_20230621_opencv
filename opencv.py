import cv2

# ファイル名は英数字（半角）
# xxx.pyと同じ階層に置く（ここで言うとopencv.pyと同じ階層）
image1 = cv2.imread('1.png')
image2 = cv2.imread('2.png')

# 差分を取得
result = cv2.subtract(image1, image2)

# resultというウィンドウ名で差分を表示
cv2.imshow('result', result)

# 何かしらのキーが押下されるまで待機
cv2.waitKey(0)
# キー押下でウィンドウを破棄
cv2.destroyAllWindows()