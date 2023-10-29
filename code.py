from PIL import Image
from PIL import ImageFilter
# для бонусного завданя
from PIL import ImageEnhance



with Image.open('img.png') as pic_original:
    print('Зображення відкрито\nРозмір:', pic_original.size)
    print('Фрмат:', pic_original.format)
    print('Тип', pic_original.mode) # Кольорове
    pic_original.show()
