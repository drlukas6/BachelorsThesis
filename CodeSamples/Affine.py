image = cv2.imread(image_path, -1)
height, width = image.shape
# Tocke u pripadajucim uglovima
affine_ref_points_1 = np.float32([[0, 0],[s_height, 0],[0, s_width]])

t1_delta = [random_float(0, height / 3), random_float(0, width / 3)]
t2_delta = [random_float(2 * height / 3, height), 
	    	random_float(0, width / 3)]
t3_delta = [random_float(0, height /3), 
			random_float(2 * width / 3, width)]
affine_ref_points_2 = [t1_delta, t2_delta, t3_delta]

M = cv2.getAffineTransform(affine_ref_points_1, affine_ref_points_2)

image = cv2.warpAffine(image, M, (width, height))