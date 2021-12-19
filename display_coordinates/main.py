import cv2

# Update the path to your image file
image = cv2.imread("")

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:        
        cv2.putText(image, str(x) + "," + str(y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        cv2.imshow("image", image)

        print("{}, {}".format(x, y))

cv2.imshow("image", image)
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
