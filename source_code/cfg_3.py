"""
配置3
BY 李说啥都对
2018.3
"""
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

gen_char_set = number + ALPHABET

IMAGE_HEIGHT = 80
IMAGE_WIDTH = 200
MAX_CAPTCHA = 4

CHAR_SET_LEN = len(gen_char_set)

model_path_3_1 = "../CAPTCHA_program/program/model/model3_1/"
model_path_3_2 = "../CAPTCHA_program/program/model/model3_2/"
model_path_3_3 = "../CAPTCHA_program/program/model/model3_3/"

tb_log_path = "" # log文件地址
save_model = "" # 模型保存地址
rand = 0 # 图片获取时随机