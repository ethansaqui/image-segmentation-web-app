import numpy as np
import cv2 as cv2

# All this code is from https://www.geeksforgeeks.org/image-segmentation-using-k-means-clustering/
def image_segmentation(image):
    image = np.asarray(bytearray(image.read()), dtype=np.uint8)
    image = cv2.imdecode(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    pixel_values = image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    k = 3
    retval, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape((image.shape))
 
    return segmented_image