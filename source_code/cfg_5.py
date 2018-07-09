"""
配置5
BY 李说啥都对
2018.3
"""
f = open("../CAPTCHA_program/program/src/chinese.txt", "r")
CH_CHAR = []
lines = f.read()
f.close()
CH_CHAR = eval(lines)

gen_char_set = CH_CHAR

IMAGE_HEIGHT = 45
IMAGE_WIDTH = 38
MAX_CAPTCHA = 1

CHAR_SET_LEN = len(gen_char_set)

model_path_5_1 = "../CAPTCHA_program/program/model/model5_1/"
model_path_5_2 = "../CAPTCHA_program/program/model/model5_2/"
model_path_5_3 = "../CAPTCHA_program/program/model/model5_3/"

tb_log_path = "" # log文件地址
save_model = "" # 模型保存地址
rand = 0 # 图片获取时随机