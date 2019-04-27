image = cv2.imread(image_path, -1)
# Ne zelim umanjiti sliku
s_x = np.random.rand() + 1 
s_y = np.random.rand() + 1
image = cv2.resize(image, fx=s_x, fy=s_y)