import cv2

# Update coordinates to your needs
x1,y1,x2,y2 = 250,175,420,400

# Update the path to your image file
img = cv2.imread("")
cropped_img = img[y1:y2, x1:x2]

# Display coordinates box around the image
# cv2.rectangle(img, (x1, y1), (x2, y2), (0,0,0), 2)

cv2.imshow("original", img)
cv2.imshow("cropped", cropped_img)

# Update image name to your own
cv2.imwrite(f"", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
