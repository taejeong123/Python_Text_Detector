try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gs = cv2.imread('imgs/eng_hand.png', cv2.IMREAD_GRAYSCALE)
thres_img = cv2.threshold(image_gs, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(pytesseract.image_to_string(image_gs, lang='eng'))

cv2.imshow('img', image_gs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(pytesseract.image_to_string(Image.open('imgs/2.png'), lang='kor'))