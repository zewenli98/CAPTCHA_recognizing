"""
预测1
BY 李说啥都对
2018.3
"""
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from cfg import MAX_CAPTCHA, CHAR_SET_LEN, model_path
from cnn_sys import crack_captcha_cnn, X, keep_prob
from utils import convert2gray, vec2text
from PyQt5.QtWidgets import QApplication, QMessageBox


def msg(QtWidgets):
    QMessageBox.information(QtWidgets, "提示", "有错误发生，请检查输入文件是否有误！", QMessageBox.Ok)

def hack_function(sess, predict, captcha_image):
    text_list = sess.run(predict, feed_dict={X: [captcha_image], keep_prob: 1})
    text = text_list[0].tolist()
    vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
    i = 0
    for n in text:
        vector[i * CHAR_SET_LEN + n] = 1
        i += 1
    return vec2text(vector)


def batch_hack_captcha(inroad, outroad):
    try:
        fw = open(outroad, 'w')
        with tf.Session() as sess:
            output = crack_captcha_cnn()
            saver = tf.train.Saver()
            saver.restore(sess, tf.train.latest_checkpoint(model_path))

            dirs = os.listdir(inroad)

            for i in dirs:
                QApplication.processEvents()
                image = Image.open(inroad + '/' + i)
                # 用于测试测试集准确率
                # text = lines[i].split(",")[1].strip()
                # text1 = text.split("=")[0]
                # label_ans = eval(text1)
                image = convert2gray(image)
                image = image.flatten() / 255
                pred = hack_function(sess, tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2), image)
                predict_text = eval(pred)
                # if label_ans == predict_text:
                #     right_cnt += 1
                # else:
                #     pass
                i = i.split(".")[0]
                print("{},{}".format(i, str(pred) + "=" + str(predict_text)))
                fw.write("{},{}\n".format(i, str(pred) + "=" + str(predict_text)))
                fw.flush()

    except:
        print("ERROR!")
        return -1


if __name__ == '__main__':
   inroad = r'E:\Users\Dell\PycharmProjects\CNN-first\all/'
   outroad = r'C:\Users\Servon\Desktop/mappings.txt'
   batch_hack_captcha(inroad, outroad)
   print('end...')
