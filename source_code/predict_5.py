"""
预测5
BY 李说啥都对
2018.3
"""
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from cfg_5 import MAX_CAPTCHA, CHAR_SET_LEN,  model_path_5_1, model_path_5_2, model_path_5_3
from cnn_sys_5 import crack_captcha_cnn, X, keep_prob
from utils_5 import vec2text, get_clear_bin_image
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


def batch_hack_captcha_5(inroad, outroad):
    try:
        fw = open(outroad, 'w')
        output = crack_captcha_cnn()
        predict = tf.argmax(tf.reshape(output, [-1, MAX_CAPTCHA, CHAR_SET_LEN]), 2)

        region1 = (0, 0, 38, 45)
        region2 = (37, 0, 75, 45)
        region3 = (75, 0, 113, 45)
        region4 = (112, 0, 150, 45)

        saver = tf.train.Saver()
        with tf.Session() as sess:

            # first model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_5_1))
            dirs = os.listdir(inroad)

            answer = [[], [], [], []]
            for i in dirs:
                QApplication.processEvents()
                ans = []
                predict_text = [-1, -1, -1, -1]
                num = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                image = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(i).zfill(4) + '.jpg')
                img1 = image.crop(region1)
                #img1.show()
                img1 = get_clear_bin_image(img1)
                img1 = np.array(img1)
                img1 = 1 * img1.flatten()

                img2 = image.crop(region2)
                # img2.show()
                img2 = get_clear_bin_image(img2)
                img2 = np.array(img2)
                img2 = 1 * img2.flatten()

                img3 = image.crop(region3)
                # img3.show()
                img3 = get_clear_bin_image(img3)
                img3 = np.array(img3)
                img3 = 1 * img3.flatten()

                img4 = image.crop(region4)
                # img4.show()
                img4 = get_clear_bin_image(img4)
                img4 = np.array(img4)
                img4 = 1 * img4.flatten()

                # print(img1.shape)
                predict1 = hack_function(sess, predict, img1)
                predict2 = hack_function(sess, predict, img2)
                predict3 = hack_function(sess, predict, img3)
                predict4 = hack_function(sess, predict, img4)

                for j in range(9):
                    img = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(j) + '.jpg')
                    img = img.crop((0, 0, 38, 45))
                    img = get_clear_bin_image(img)
                    img = np.array(img)
                    img = 1 * img.flatten()
                    pred = hack_function(sess, predict, img)
                    ans.append(pred)

                if predict1 in ans:
                    predict_text[0] = ans.index(predict1)
                    if predict_text[0] in num:
                        num.remove(predict_text[0])
                else:
                    predict_text[0] = -1
                if predict2 in ans:
                    predict_text[1] = ans.index(predict2)
                    if predict_text[1] in num:
                        num.remove(predict_text[1])
                else:
                    predict_text[1] = -1
                if predict3 in ans:
                    predict_text[2] = ans.index(predict3)
                    if predict_text[2] in num:
                        num.remove(predict_text[2])
                else:
                    predict_text[2] = -1
                if predict4 in ans:
                    predict_text[3] = ans.index(predict4)
                    if predict_text[3] in num:
                        num.remove(predict_text[3])
                else:
                    predict_text[3] = -1

                for k in range(4):
                    if predict_text[k] == -1:
                        # rr = random.choice(num)
                        predict_text[k] = num[k]
                        # num.remove(rr)

                answer[0].append(predict_text[0])
                answer[1].append(predict_text[1])
                answer[2].append(predict_text[2])
                answer[3].append(predict_text[3])
                print("{},{}{}{}{}".format(i, predict_text[0], predict_text[1], predict_text[2], predict_text[3]))
                # fw.write("{},{}{}{}{}\n".format(i, predict_text[0], predict_text[1], predict_text[2], predict_text[3]))
                # fw.flush()

            # second model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_5_2))

            answer2 = [[], [], [], []]
            for i in dirs:
                QApplication.processEvents()
                ans = []
                predict_text = [-1, -1, -1, -1]
                num = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                image = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(i).zfill(4) + '.jpg')
                img1 = image.crop(region1)
                # img1.show()
                img1 = get_clear_bin_image(img1)
                img1 = np.array(img1)
                img1 = 1 * img1.flatten()

                img2 = image.crop(region2)
                # img2.show()
                img2 = get_clear_bin_image(img2)
                img2 = np.array(img2)
                img2 = 1 * img2.flatten()

                img3 = image.crop(region3)
                # img3.show()
                img3 = get_clear_bin_image(img3)
                img3 = np.array(img3)
                img3 = 1 * img3.flatten()

                img4 = image.crop(region4)
                # img4.show()
                img4 = get_clear_bin_image(img4)
                img4 = np.array(img4)
                img4 = 1 * img4.flatten()

                # print(img1.shape)
                predict1 = hack_function(sess, predict, img1)
                predict2 = hack_function(sess, predict, img2)
                predict3 = hack_function(sess, predict, img3)
                predict4 = hack_function(sess, predict, img4)

                for j in range(9):
                    img = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(j) + '.jpg')
                    img = img.crop((0, 0, 38, 45))
                    img = get_clear_bin_image(img)
                    img = np.array(img)
                    img = 1 * img.flatten()
                    pred = hack_function(sess, predict, img)
                    ans.append(pred)

                if predict1 in ans:
                    predict_text[0] = ans.index(predict1)
                    if predict_text[0] in num:
                        num.remove(predict_text[0])
                else:
                    predict_text[0] = -1
                if predict2 in ans:
                    predict_text[1] = ans.index(predict2)
                    if predict_text[1] in num:
                        num.remove(predict_text[1])
                else:
                    predict_text[1] = -1
                if predict3 in ans:
                    predict_text[2] = ans.index(predict3)
                    if predict_text[2] in num:
                        num.remove(predict_text[2])
                else:
                    predict_text[2] = -1
                if predict4 in ans:
                    predict_text[3] = ans.index(predict4)
                    if predict_text[3] in num:
                        num.remove(predict_text[3])
                else:
                    predict_text[3] = -1

                for k in range(4):
                    if predict_text[k] == -1:
                        # rr = random.choice(num)
                        predict_text[k] = num[k]
                        # num.remove(rr)

                answer2[0].append(predict_text[0])
                answer2[1].append(predict_text[1])
                answer2[2].append(predict_text[2])
                answer2[3].append(predict_text[3])
                print("{},{}{}{}{}".format(i, predict_text[0], predict_text[1], predict_text[2], predict_text[3]))

            # third model predict
            saver.restore(sess, tf.train.latest_checkpoint(model_path_5_3))

            answer3 = [[], [], [], []]
            for i in dirs:
                QApplication.processEvents()
                ans = []
                predict_text = [-1, -1, -1, -1]
                num = [0, 1, 2, 3, 4, 5, 6, 7, 8]

                image = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(i).zfill(4) + '.jpg')
                img1 = image.crop(region1)
                # img1.show()
                img1 = get_clear_bin_image(img1)
                img1 = np.array(img1)
                img1 = 1 * img1.flatten()

                img2 = image.crop(region2)
                # img2.show()
                img2 = get_clear_bin_image(img2)
                img2 = np.array(img2)
                img2 = 1 * img2.flatten()

                img3 = image.crop(region3)
                # img3.show()
                img3 = get_clear_bin_image(img3)
                img3 = np.array(img3)
                img3 = 1 * img3.flatten()

                img4 = image.crop(region4)
                # img4.show()
                img4 = get_clear_bin_image(img4)
                img4 = np.array(img4)
                img4 = 1 * img4.flatten()

                # print(img1.shape)
                predict1 = hack_function(sess, predict, img1)
                predict2 = hack_function(sess, predict, img2)
                predict3 = hack_function(sess, predict, img3)
                predict4 = hack_function(sess, predict, img4)

                for j in range(9):
                    img = Image.open(inroad + '/' + str(i).zfill(4) + '/' + str(j) + '.jpg')
                    img = img.crop((0, 0, 38, 45))
                    img = get_clear_bin_image(img)
                    img = np.array(img)
                    img = 1 * img.flatten()
                    pred = hack_function(sess, predict, img)
                    ans.append(pred)

                if predict1 in ans:
                    predict_text[0] = ans.index(predict1)
                    if predict_text[0] in num:
                        num.remove(predict_text[0])
                else:
                    predict_text[0] = -1
                if predict2 in ans:
                    predict_text[1] = ans.index(predict2)
                    if predict_text[1] in num:
                        num.remove(predict_text[1])
                else:
                    predict_text[1] = -1
                if predict3 in ans:
                    predict_text[2] = ans.index(predict3)
                    if predict_text[2] in num:
                        num.remove(predict_text[2])
                else:
                    predict_text[2] = -1
                if predict4 in ans:
                    predict_text[3] = ans.index(predict4)
                    if predict_text[3] in num:
                        num.remove(predict_text[3])
                else:
                    predict_text[3] = -1

                for k in range(4):
                    if predict_text[k] == -1:
                        # rr = random.choice(num)
                        predict_text[k] = num[k]
                        # num.remove(rr)

                answer3[0].append(predict_text[0])
                answer3[1].append(predict_text[1])
                answer3[2].append(predict_text[2])
                answer3[3].append(predict_text[3])
                print("{},{}{}{}{}".format(i, predict_text[0], predict_text[1], predict_text[2], predict_text[3]))

            daan = [[],[],[],[]]
            for i in range(len(answer[0])):
                for j in range(4):
                    if answer[j][i] == answer2[j][i] and answer[j][i] == answer3[j][i]:
                        daan[j].append(answer[j][i])
                    elif answer[j][i] == answer2[j][i]:
                        daan[j].append(answer[j][i])
                    elif answer[j][i] == answer3[j][i]:
                        daan[j].append(answer[j][i])
                    elif answer2[j][i] == answer3[j][i]:
                        daan[j].append(answer2[j][i])
                    else:
                        daan[j].append(answer[j][i])

            for dir, i in zip(dirs, range(len(answer[0]))):
                print(dir, end=",")
                fw.write(dir + ',')
                for j in range(4):
                    print(daan[j][i], end="")
                    fw.write(str(daan[j][i]))
                print()
                fw.write('\n')
    except:
        print("ERROR!")
        return -1


if __name__ == '__main__':

    # inroad = r'E:\Users\Dell\PycharmProjects\CNN-fif\all/'
    inroad = r"C:\Users\Servon\Desktop\fff/"
    outroad = r'C:\Users\Servon\Desktop\mappings5v2.txt'
    batch_hack_captcha_5(inroad, outroad)

    # predict_text = [-1, 3, 2, -1]
    # print(predict_text)

    # num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # num.remove(0)
    # num.remove(1)
    # num.remove(2)
    # num.remove(3)
    # print(num)
    # print(len(num))
    # print()
    # print(random.choice(num))
    # print(random.choice(num))
    # print(random.choice(num))
    # print(random.choice(num))
    # print(random.choice(num))
