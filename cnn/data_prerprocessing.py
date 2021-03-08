import cv2
import tensorflow as tf
import os
import numpy as np


def get_cv2_image(path, img_rows, img_cols):
    # Loading as Grayscale image
    # if color_type == 1:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # elif color_type == 3:
    # img = cv2.imread(path, cv2.IMREAD_COLOR)
    # Reduce size
    # print("@@@img_rows", img_rows)
    # print("@@@img_cols", img_cols)
    # print("@@@img", img)
    img = cv2.resize(img, (img_rows, img_cols))
    return img


def get_data(img_rows, img_cols):
    cnn_test_data = list()
    # for i in range(1, 11):
        # print("@@@cur dir", os.getcwd())
    path = os.path.join('img', 'img_' + "1" + '.jpg')
        # print("@@@path", path)
    img = get_cv2_image(path, img_rows, img_cols)
    cnn_test_data.append(img)
    cnn_test_data = np.array(cnn_test_data, dtype=np.uint8)
    cnn_test_data = cnn_test_data.reshape(-1, img_rows, img_cols, 1)
    return cnn_test_data


if __name__ == '__main__':
    test_data = get_data(64, 64)
    x = test_data
    while len(x) > 0:
        print(len(x))
        x = x[0]
