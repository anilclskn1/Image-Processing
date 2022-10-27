import cv2 as cv

# READING IMAGES

image = cv.imread('photos/warcraft.jpeg')
cv.imshow('RGB', image)

image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", image_gray)

print(image.shape)
print(image_gray.shape)

B, G, R = cv.split(image)
print(B.shape)
print(G.shape)
print(R.shape)

cv.imshow("R", R)
cv.imshow("G", G)
cv.imshow("B", B)

cv.waitKey(0)

# READING VIDEOS
