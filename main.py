try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gs = cv2.imread('imgs/3.jpg', cv2.IMREAD_GRAYSCALE)
thres_img = cv2.adaptiveThreshold(image_gs,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,41,3)

print(pytesseract.image_to_string(image_gs, lang='eng'))

cv2.imshow('img', image_gs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(pytesseract.image_to_string(Image.open('imgs/2.png'), lang='kor'))