import cv2
import os

img_dir = os.path.dirname(__file__) + "/test_images"
for count, filename in enumerate(os.listdir(img_dir)):
    object_cascade = cv2.CascadeClassifier("cascade.xml")
    
    img = cv2.imread(img_dir + "/" + filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    objects = object_cascade.detectMultiScale(gray, 1.01, 7)
    for (x, y, w, h) in objects:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)
    
    cv2.namedWindow(filename, cv2.WINDOW_NORMAL)
    cv2.imshow(filename, img)
    cv2.waitKey(0)

cv2.destroyAllWindows()