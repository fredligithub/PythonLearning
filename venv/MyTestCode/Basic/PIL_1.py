# 导入Python Imaging Library 中的图像处理库:Image
from PIL import Image

# 通过Open方法打开图片， 并把其转换为灰度图
pil_im = Image.open('C:/Users/GG/Pictures/Saved Pictures/car.jpg').convert('L')

# 保存图片为新文件
pil_im.save('C:/Users/GG/Pictures/Saved Pictures/new_car.jpg')