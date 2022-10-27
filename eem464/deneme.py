import cv2

lennaImage = cv2.imread("lenna_image.png")

image_bit = cv2.imread("bmpfiles/lena.bmp")

cv2.imshow("dd",lennaImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("wait")

