import os
from PIL import Image
from PIL import ImageColor

'''
os.chdir("C:/Users/GG/Pictures/Saved Pictures")
myGirl = Image.open("Girl.jpg")
print(myGirl.size)
print(myGirl.filename)
print(myGirl.format)
'''
# 获取到red对应的RGBA的值是：(255,0,0,255)
# print(ImageColor.getcolor('red', 'RGBA'))

# 创建了一个宽度100， 高度200的纯紫色图片并保存为New.png
newIm = Image.new('RGBA', (100,200), 'purple')
newIm.save("C:/Users/GG/Pictures/Saved Pictures/New.png")