"""
Travel With Python during Covid
ExTupedia - Your travel Agency
https://www.youtube.com/watch?v=85ya9lA9asQ

inpixio/remove-background
"""

from PIL import Image


me = Image.open('me2.jpg')
taj = Image.open('taj-mahal.jpg')


taj.paste(me, (30, 0), me)

# taj.save('me in India.jpg')
taj.show()

