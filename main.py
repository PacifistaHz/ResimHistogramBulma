import cv2

from matplotlib import pyplot as plt

img = cv2.imread("1.png",0)
hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.xlabel("Renk Değeri")
plt.ylabel("Frekans")
plt.plot(hist)
plt.show()
