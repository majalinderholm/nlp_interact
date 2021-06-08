import cv2
import os

# Read input
FILE_NAME = 'IMG_4966.jpg'
FOLDER_PATH = r'C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact'
color = cv2.imread(os.path.join(FOLDER_PATH, FILE_NAME), cv2.IMREAD_COLOR)
color = cv2.resize(color, (0, 0), fx=0.15, fy=0.15)
# RGB to gray
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output/gray.png', gray)
# cv2.imwrite('output/thresh.png', thresh)
# Edge detection
edges = cv2.Canny(gray, 100, 200, apertureSize=3)
# Save the edge detected image
cv2.imwrite('output/edges.png', edges)