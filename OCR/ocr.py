import os, io
from google.cloud import vision_v1 as vision
from google.cloud.vision_v1 import types
import pandas as pd

#Method for performing OCR on an image
def detect_text(img):
    # Open image
    with open(img, 'rb') as image_file:
        content = image_file.read()

    #Define input and perform ocr to get the response
    image = vision.types.Image(content=content)
    response = client.document_text_detection(
                                            image=image,
                                            image_context = {"language_hints": ['sv']} #swedish text
                                            )

    return response

#Get confidence of each letter classified
def get_confidence(pages):
    for page in pages:
        for block in page.blocks:
            print('block confidence:', block.confidence)

            for paragraph in block.paragraphs:
                print('paragraph confidence:', paragraph.confidence)

                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])
                    print('Word text: {0} (confidence: {1}'.format(word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {0} (confidence: {1}'.format(symbol.text, symbol.confidence))

# Provide the API with the Google Cloud Vision API
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:/Users/paw472/OneDrive - AFRY\Documents/Projects/nlp_interact/key_vision.json'

# Initialize a Google Cloud Vision client
client = vision.ImageAnnotatorClient()

# Define file name and path
# FILE_NAME = 'DSC_0104.NEF'
# FOLDER_PATH = r'C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact/DataCollection/ValterSchytt-2-1962'
FILE_NAME = 'IMG_4972.jpg'
FOLDER_PATH = r'C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact'
response = detect_text(os.path.join(FOLDER_PATH, FILE_NAME))
print(response.full_text_annotation.text)
#get_confidence(response.full_text_annotation.pages)