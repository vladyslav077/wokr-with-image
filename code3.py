from PIL import Image
from PIL import ImageFilter
# для бонусного завданя
from PIL import ImageEnhance


with Image.open('img.png') as pic_original:
    pic_blured = pic_original.filter(ImageFilter.GaussianBlur(4))
    pic_blured.save('blured.png')
    pic_blured.show()