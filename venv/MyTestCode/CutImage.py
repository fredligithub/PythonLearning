import cv2
import os
from PIL import Image
import random
import string

# 生成随机字符串用作文件名
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

# 字符串集合
chars = string.ascii_letters

# print( random_string_generator(6, chars))

# 剪裁文件夹中的图片
def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        i = Image.open(folder + "/" + filename)
        frame2 = i.crop(((0, 0, 1024, 883)))
        frame2.save('C:/OpenCV/ImagesFromRnD/1130/Test/Result/' + random_string_generator(6, chars) + ".jpg")
        
allImage = load_images_from_folder("C:/OpenCV/ImagesFromRnD/1130/training set")
