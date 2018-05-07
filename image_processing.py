import cv2
import  numpy as np


def image_processing(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = np.copy(image[:, :, 1])
    # image = cv2.Laplacian(image, cv2.CV_64F)
    # image = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=5)
    # img = cv2.normalize(image, image, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    '''for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < (np.max(image) - np.min(image)):
                image[i][j] = 0
            else:
                image[i][j] = 255
    print(image)'''
    for i in range(len(img_gray)):
        for j in range(len(img_gray[0])):
            if img_gray[i][j] < 35:
                img[i][j] = 255

    # img = cv2.bitwise_not(img)
    # image = cv2.Laplacian(image, cv2.CV_64F)

    MIN = 30
    MAX = 80

    norm = ((img - MIN) / (MAX - MIN)) * 255.0
    norm[norm > 255] = 255.0
    norm[norm < 0] = 0.0

    norm[norm > 160] = 0.0
    norm[norm > 0] = 255.0

    # norm = cv2.Sobel(norm, cv2.CV_64F, 1, 1, ksize=5)

    '''kernel = np.ones((2, 2), np.uint8)
    # norm = cv2.dilate(image, kernel, iterations=1)
    norm = cv2.erode(norm, kernel, iterations=1)
    # kernel = np.ones((5, 5), np.uint8)
    norm = cv2.dilate(norm, kernel, iterations=5)
    # norm = cv2.erode(norm, kernel, iterations=15)
    # norm = cv2.erode(norm, kernel, iterations=3)
    # norm = cv2.dilate(norm, kernel, iterations=5)
    # norm = cv2.erode(norm, kernel, iterations=5)'''

    marker = np.copy(image)
    marker[norm == 255] = 0

    return norm, marker
