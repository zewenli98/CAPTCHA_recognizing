"""
Servon 2018.2

get data iterator
"""
import numpy as np
from PIL import Image
from cfg import IMAGE_HEIGHT, IMAGE_WIDTH, CHAR_SET_LEN, MAX_CAPTCHA
from utils import convert2gray, text2vec

root = "E:/Users/Dell/PycharmProjects/CNN-first/all/"


def get_next_batch(batch_size=64, cnt=0):
    """
    # 生成一个训练batch
    :param batch_size cnt
    :return:
    """
    batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA * CHAR_SET_LEN])

    f = open(root + "mappings.txt", 'r')
    lines = f.readlines()
    f.close()

    i = 0
    for j in range(cnt*batch_size, (cnt+1)*batch_size):
        text = lines[j].split(",")[-1]
        text = text.split("=")[0]
        image = Image.open(root + str(j).zfill(4) + ".jpg")
        # print(j)
        # print(text)
        # image.show()
        image = convert2gray(image)

        batch_x[i, :] = image.flatten() / 255  # (image.flatten()-128)/128  mean为0
        batch_y[i, :] = text2vec(text)

        i += 1

    return batch_x, batch_y

get_next_batch(64 ,155)