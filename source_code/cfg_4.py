"""
配置4
BY 李说啥都对
2018.3
"""
number = ['0', '1', '2', '3']

gen_char_set = number

IMAGE_HEIGHT = 45
IMAGE_WIDTH = 150
MAX_CAPTCHA = 1

CHAR_SET_LEN = len(gen_char_set)

model_path_4 = "../CAPTCHA_program/program/model/model4/"

tb_log_path = "" # log文件地址
save_model = "" # 模型保存地址
rand = 0 # 图片获取时随机