import cv2
import matplotlib.pyplot as plt

image=cv2.imread("prg1.png")
plt.imshow(image,cmap="winter",interpolation="bicubic")
plt.show()
