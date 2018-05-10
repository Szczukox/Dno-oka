import cv2
import numpy as np


def image_processing(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range(len(img_gray)):
        for j in range(len(img_gray[0])):
            if img_gray[i][j] < 35:
                img_gray[i][j] = 255

    MIN = 48
    MAX = 140

    norm = ((img_gray - MIN) / (MAX - MIN)) * 255.0
    norm[norm > 255] = 255.0
    norm[norm < 0] = 0.0

    r = 16
    for i in range(0, len(norm) - r, r):
        for j in range(0, len(norm[i]) - r, r):
            matrix = norm[i: i + r, j: j + r]
            mean = np.median(matrix) * 0.87
            matrix[matrix < mean] = 0.0
            matrix[matrix > mean] = 255.0

    norm = np.abs(norm - 255)

    marker = np.copy(image)
    marker[norm == 255] = 0

    return norm, marker
