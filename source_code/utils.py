"""
工具类1
BY 李说啥都对
2018.3
"""
import numpy as np
import re
from cfg import MAX_CAPTCHA, CHAR_SET_LEN


def char2pos(c):
    if c == '0':
        k = 0
    elif c == '1':
        k = 1
    elif c == '2':
        k = 2
    elif c == '3':
        k = 3
    elif c == '4':
        k = 4
    elif c == '5':
        k = 5
    elif c == '6':
        k = 6
    elif c == '7':
        k = 7
    elif c == '8':
        k = 8
    elif c == '9':
        k = 9
    elif c == '10':
        k = 10
    elif c == '11':
        k = 11
    elif c == '12':
        k = 12
    elif c == '13':
        k = 13
    elif c == '14':
        k = 14
    elif c == '15':
        k = 15
    elif c == '16':
        k = 16
    elif c == '17':
        k = 17
    elif c == '18':
        k = 18
    elif c == '19':
        k = 19
    elif c == '20':
        k = 20
    elif c == '+':
        k = 21
    elif c == '-':
        k = 22
    elif c == '*':
        k = 23
    else:
        raise ValueError('No Map')

    return k


def pos2char(char_idx):
    if char_idx == 0:
        char_code = '0'
    elif char_idx == 1:
        char_code = '1'
    elif char_idx == 2:
        char_code = '2'
    elif char_idx == 3:
        char_code = '3'
    elif char_idx == 4:
        char_code = '4'
    elif char_idx == 5:
        char_code = '5'
    elif char_idx == 6:
        char_code = '6'
    elif char_idx == 7:
        char_code = '7'
    elif char_idx == 8:
        char_code = '8'
    elif char_idx == 9:
        char_code = '9'
    elif char_idx == 10:
        char_code = '10'
    elif char_idx == 11:
        char_code = '11'
    elif char_idx == 12:
        char_code = '12'
    elif char_idx == 13:
        char_code = '13'
    elif char_idx == 14:
        char_code = '14'
    elif char_idx == 15:
        char_code = '15'
    elif char_idx == 16:
        char_code = '16'
    elif char_idx == 17:
        char_code = '17'
    elif char_idx == 18:
        char_code = '18'
    elif char_idx == 19:
        char_code = '19'
    elif char_idx == 20:
        char_code = '20'
    elif char_idx == 21:
        char_code = '+'
    elif char_idx == 22:
        char_code = '-'
    elif char_idx == 23:
        char_code = '*'
    else:
        raise ValueError('error')

    return char_code


def convert2gray(imgs):
    gray = np.mean(imgs, -1)
    return gray


def text2vec(text):
    vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)
    text = re.findall('(\d + |\+| - |\*|/)', text)

    for i, c in zip(range(5), text):
        t = char2pos(c)
        idx = i * CHAR_SET_LEN + t
        vector[idx] = 1

    return vector


def vec2text(vec):
    char_pos = vec.nonzero()[0]
    text = []
    for i, c in enumerate(char_pos):
        char_at_pos = i  # c/63
        char_idx = c % CHAR_SET_LEN

        char_code = pos2char(char_idx)

        text.append(char_code)
    return "".join(text)


if __name__ == '__main__':
    text = '14+2+12'
    ptext = text2vec(text)
    print(text2vec(text),len(ptext))
    textt = vec2text(ptext)
    print(textt)
