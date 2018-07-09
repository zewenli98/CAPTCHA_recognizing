"""
预测2
BY 李说啥都对
2018.3
"""
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from cfg_2 import MAX_CAPTCHA, CHAR_SET_LEN, model_path_2
from cnn_sys_2 import crack_captcha_cnn, X, keep_prob
from utils_2 import vec2text, get_clear_bin_image
from PyQt5.QtWidgets import QApplication


def hack_function(sess, predict, captcha_image):
    text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})
    text = text_list[0].tolist()
    vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
    i = 0
    for n in text:
        vector[i * CHAR_SET_LEN + n] = 1
        i += 1
    return vec2text(vector)


def batch_hack_captcha_2(inroad, outroad):
    try:
        output = crack_captcha_cnn()
        predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
        fw = open(outroad, 'w')
        saver = tf.train.Saver()

        with tf.Session() as sess:
            saver.restore(sess, tf.train.latest_checkpoint(model_path_2))
            dirs = os.listdir(inroad)

            for i in dirs:
                QApplication.processEvents()
                image = Image.open(inroad + "/" + i)
                image = get_clear_bin_image(image)
                image = np.array(image)
                image = 1 * image.flatten()
                predict_text = hack_function(sess, predict, image)
                i = i.split(".")[0]
                print("{},{}".format(i, predict_text))
                fw.write("{},{}\n".format(i, predict_text))
                fw.flush()
    except:
        print("ERROR!")
        return -1


# if __name__ == '__main__':
#    batch_hack_captcha()
#    print('end...')
