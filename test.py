import pytesseract
import cv2
from PIL import Image

print("Tesseract version:", pytesseract.get_tesseract_version())
print("OpenCV version:", cv2.__version__)
print("Pillow version:", Image.__version__)