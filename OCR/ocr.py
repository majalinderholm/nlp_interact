import os, io
from google.cloud import vision_v1 as vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/paw472/OneDrive - AFRY\Documents/Projects/nlp_interact/key_vision.json'

client = vision.ImageAnnotatorClient()

FILE_NAME = 'DSC_0104.NEF'
FOLDER_PATH = r'C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact/DataCollection/ValterSchytt-2-1962'

with io.open(os.path.join(FOLDER_PATH, FILE_NAME), 'rb') as image_file:
    content = image_file.read()