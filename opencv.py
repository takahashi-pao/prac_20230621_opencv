import cv2

image1 = cv2.imread('ルッチ1.png')
image2 = cv2.imread('ルッチ2.png')

result = cv2.subtract(image1, image2)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()