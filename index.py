# take image 1.png and see it from perspective of image 2.png
import cv2
import numpy as np

# read images
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')

# convert to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# usign mouse select 4 points then close window then show points
# points are selected in order: top-left, top-right, bottom-right, bottom-left
# these points will be used to calculate perspective transform

# select points in image 1
points1 = []


def select_points1(event, x, y):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img1, (x, y), 5, (0, 255, 0), -1)
        points1.append([x, y])


cv2.namedWindow('image1')
cv2.setMouseCallback('image1', select_points1)
while len(points1) < 4:
    cv2.imshow('image1', img1)
    cv2.waitKey(1)
cv2.destroyAllWindows()

# select points in image 2
points2 = []


def select_points2(event, x, y):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img2, (x, y), 5, (0, 255, 0), -1)
        points2.append([x, y])


cv2.namedWindow('image2')
cv2.setMouseCallback('image2', select_points2)
while len(points2) < 4:
    cv2.imshow('image2', img2)
    cv2.waitKey(1)
cv2.destroyAllWindows()

# log points
print('points1 =', points1)
print('points2 =', points2)

# calculate perspective transform
M = cv2.getPerspectiveTransform(np.float32(points1), np.float32(points2))

# apply perspective transform
img1_transformed = cv2.warpPerspective(img1, M, (img2.shape[1], img2.shape[0]))

# show result
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image1_transformed', img1_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
