Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import cv2
... import numpy as np
... 
... # Read an image
... img = cv2.imread('example.jpg')
... 
... # Convert to grayscale
... gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
... 
... # Apply a Gaussian blur
... blurred = cv2.GaussianBlur(gray, (5, 5), 0)
... 
... # Detect edges using Canny
