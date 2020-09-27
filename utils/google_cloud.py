from google.cloud import vision
from utils import text_to_speech


'''
Function that recieves a photo and uses google cloud vision to return lables
'''
def analyze_photo(content):


    client = vision.ImageAnnotatorClient()
    image = vision.types.Image(content=content)
    response = client.label_detection(image=image)
    

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    labels = response.label_annotations

    print('Labels:')

    for label in labels:
        print(label.description)
    
    return labels