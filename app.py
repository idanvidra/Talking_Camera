from utils import google_cloud
from utils import text_to_speech
from utils import camera
import io
import os


FILE_PATH = 'image.png'

# take picture
# camera.take_picture()

# if picture exists
if os.path.isfile('image.png'):

    # open the picture
    with io.open(FILE_PATH, 'rb') as image_file:
            content = image_file.read()
    # get the lables
    lables = google_cloud.analyze_photo(content)
    # read lables out loud
    text_to_speech.text_to_speech(lables)

else:

    print("Take picture first")