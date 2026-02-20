import cv2

image = cv2.imread('./data/1 (1).jpeg')

print(type(image))   #<class 'numpy.ndarray'> 

# images are numpy array

print(image.shape)   #image shape is given as its height, width and no of channels

# an image is made by "pixels"