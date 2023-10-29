from PIL import Image
from PIL import ImageFilter
# для бонусного завданя
from PIL import ImageEnhance


with Image.open('img.png') as pic_original:
    pic_gray = pic_original.convert('L')
    pic_gray.save('gruy.png')
    print('Зображення відкрито\nРозмір:', pic_original.size)
    print('Фрмат:', pic_original.format)
    print('Тип', pic_original.mode) #чб
    pic_original.show()