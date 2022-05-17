# 3.10.3
from PIL import Image                                                                                
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

img = Image.open(os.path.join(__location__, 'images/0.png'))
img.show() 