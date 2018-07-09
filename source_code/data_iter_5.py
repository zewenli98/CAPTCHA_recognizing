"""
Servon 2018.2

get data iterator
"""
import numpy as np
from PIL import Image
from cfg_5 import IMAGE_HEIGHT, IMAGE_WIDTH, CHAR_SET_LEN, MAX_CAPTCHA
from utils_5 import text2vec, get_clear_bin_image


dirs = ""
root = ""
def get_next_batch(batch_size=128, cnt=0):
    """
    # 生成一个训练batch
    :param batch_size:
    :return:
    """

    batch_x = np.zeros([batch_size, IMAGE_HEIGHT * IMAGE_WIDTH])
    batch_y = np.zeros([batch_size, MAX_CAPTCHA * CHAR_SET_LEN])

    i = 0
    for j in range(cnt * batch_size, (cnt+1) * batch_size):
        text = dirs[j].strip()[0]
        image = Image.open(root + dirs[j])
        # # image = image.filter(ImageFilter.MedianFilter)
        # # print(j)
        # print(text)
        # # image.show()
        image = get_clear_bin_image(image)
        # image.show()
        image = np.array(image)
        # image = convert2gray(image)
        # print(image)

        batch_x[i, :] = 1 * image.flatten()
        batch_y[i, :] = text2vec(text)
        i += 1

    return batch_x, batch_y


# get_next_batch(3, 2667)
get_next_batch(128, 2264)
# get_gen_batch(8000)
# get_test_batch(3, 0)