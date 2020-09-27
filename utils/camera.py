import cv2


'''
Function to take a single picture and save it as image.png in the main directory
'''
def take_picture():
    camera = cv2.VideoCapture(0)

    return_value, image = camera.read()
    cv2.imwrite('image.png', image)

    del(camera)