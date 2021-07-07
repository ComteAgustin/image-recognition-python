from cv2 import cv2

# Asign the image in the var with the name "img"
img = cv2.imread('image.jpeg')
# Converting img to grey scale
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Umbraling
_,umbral = cv2.threshold(grey, 225, 255, cv2.THRESH_BINARY)
# Find and drawing contourns
contourn, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contourn, -1, (0, 0, 0), 2)

# Show
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows