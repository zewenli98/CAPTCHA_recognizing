"""
配置1
BY 李说啥都对
2018.3
"""
import os
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
          '20']
sig = ['+', '-', '*']

gen_char_set = number + sig  # 用于生成验证码的数据集

IMAGE_HEIGHT = 80
IMAGE_WIDTH = 350
MAX_CAPTCHA = 5

CHAR_SET_LEN = len(gen_char_set)

model_path = '../CAPTCHA_program/program/model/model1/'
# print(os.listdir(model_path))

tb_log_path = "" # log文件地址
save_model = "" # 模型保存地址
rand = 0 # 图片获取时随机