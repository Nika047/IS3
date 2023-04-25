import cv2
import imutils

image = cv2.imread("C:/Users/1/Desktop/IS3 img/IS3_3.png")
cv2.imshow("Input", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)

cnts = imutils.grab_contours(cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE))
output = image.copy()

for c in cnts:
    cv2.drawContours(output, [c], -1, (0, 0, 0), 1)

text = "FIO. {} objects".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0), 1)

height, width, _ = image.shape
cv2.rectangle(output, (height//2+15, width//2+15), (height//2-15, width//2-15), (0, 0, 0), 1)
cv2.circle(output, (50, width-100), 1, (0, 0, 0), 1)

cv2.imshow("Output", output)
print(text)

cv2.waitKey(0)
