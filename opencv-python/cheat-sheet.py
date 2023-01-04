import cv2

# Read an image
img = cv2.imread('image.jpg')

# Write an image
cv2.imwrite('image.jpg', img)

# Resize image
resized_img = cv2.resize(img, (100, 50))

# Resize image while maintaining aspect ratio
resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Crop image
cropped_img = img[y:y+h, x:x+w]

# Rotate image
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated_img = cv2.warpAffine(img, M, (w, h))

# Apply a blur filter
blur_img = cv2.blur(img, (5, 5))

# Apply a Gaussian blur filter
gaussian_img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply a median blur filter
median_img = cv2.medianBlur(img, 5)

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert image to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Draw a line
cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 5)

# Draw a rectangle
cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 0), 5)

# Draw a circle
cv2.circle(img, (100, 100), 50, (255, 0, 0), 5)

# Draw a text
cv2.putText(img, 'Hello World!', (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
