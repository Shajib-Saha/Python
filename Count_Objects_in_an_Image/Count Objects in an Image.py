import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Loading and Viewing the image
img = cv2.imread('C:/Users/User/PycharmProjects/pythonProject/cars.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 10))
plt.axis("off")
plt.imshow(img1)

# Creating box around various objects
box, label, count = cv.detect_common_objects(img)
output = draw_bbox(img, box, label, count)
output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 10))
plt.axis("off")
plt.imshow(output)
plt.show()

# Count objects in the image
print("Number of objects in this image are " + str(len(label)))
