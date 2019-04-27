image = cv2.imread(image_path, -1)
# Prevelika rotacija bi mogla izazvati dvosmislenost
theta = np.random.randint(-45, high=45)
rows, cols = image.shape
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), theta, 1)
image = cv2.warpAffine(image, M, (cols, rows))