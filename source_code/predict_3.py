"""
预测3
BY 李说啥都对
2018.3
"""
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from cfg_3 import MAX_CAPTCHA, CHAR_SET_LEN, model_path_3_1, model_path_3_2, model_path_3_3
from cnn_sys_3 import crack_captcha_cnn, X, keep_prob
from utils_3 import vec2text, get_clear_bin_image
from PyQt5.QtWidgets import QApplication


def hack_function(sess, predict, captcha_image):
    text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1.})
    text = text_list[0].tolist()
    vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
    i = 0
    for n in text:
        vector[i * CHAR_SET_LEN + n] = 1
        i += 1
    return vec2text(vector)


def batch_hack_captcha_3(inroad, outroad):
    try:
        output = crack_captcha_cnn()
        predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)
        fw = open(outroad, 'w')
        saver = tf.train.Saver()
        with tf.Session() as sess:

            predict_list = []

            # first model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_3_1))
            dirs = os.listdir(inroad)

            predict_list1 = []
            for i in dirs:
                QApplication.processEvents()
                image = Image.open(inroad + "/" + i)
                image = get_clear_bin_image(image)
                image = np.array(image)
                image = 1 * image.flatten()

                predict_text = hack_function(sess, predict, image)
                i = i.split(".")[0]
                print("{},{}".format(i, predict_text))
                predict_list1.append(predict_text)
                # fw.write("{},{}\n".format(i, predict_text))
                fw.flush()

            # second model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_3_2))

            predict_list2 = []
            for i in dirs:
                QApplication.processEvents()
                image = Image.open(inroad + "/" + i)
                image = get_clear_bin_image(image)
                image = np.array(image)
                image = 1 * image.flatten()

                predict_text = hack_function(sess, predict, image)
                i = i.split(".")[0]
                print("{},{}".format(i, predict_text))
                predict_list2.append(predict_text)
                # fw.write("{},{}\n".format(i, predict_text))
                fw.flush()

            #third model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_3_3))

            predict_list3 = []
            for i in dirs:
                QApplication.processEvents()
                image = Image.open(inroad + "/" + i)
                image = get_clear_bin_image(image)
                image = np.array(image)
                image = 1 * image.flatten()

                predict_text = hack_function(sess, predict, image)
                i = i.split(".")[0]
                print("{},{}".format(i, predict_text))
                predict_list3.append(predict_text)
                # fw.write("{},{}\n".format(i, predict_text))
                fw.flush()


            for i in range(len(predict_list1)):
                if predict_list1[i] == predict_list2[i] and predict_list1[i] == predict_list3[i]:
                    predict_list.append(predict_list1[i])
                elif predict_list1[i] == predict_list2[i]:
                    predict_list.append(predict_list1[i])
                elif predict_list1[i] == predict_list3[i]:
                    predict_list.append(predict_list1[i])
                elif predict_list2[i] == predict_list3[i]:
                    predict_list.append(predict_list2[i])
                else:
                    predict_list.append(predict_list1[i])

            for dir, i in zip(dirs, range(len(predict_list))):
                dir = dir.split(".")[0]
                print(dir, predict_list[i])
                fw.write("{},{}\n".format(dir, predict_list[i]))
                fw.flush()

    except:
        print("ERROR!")
        return -1


if __name__ == '__main__':
    # inroad = r'C:\Users\Servon\Desktop\fff/'
    inroad = "E:/Users/Dell/PycharmProjects/CNN-third/all/"
    outroad = r'C:\Users\Servon\Desktop\mappings3.txt'
    batch_hack_captcha_3(inroad, outroad)
