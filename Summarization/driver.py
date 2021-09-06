import os, io
from google.cloud import vision_v1 as vision
import ocr
import summarization

def main():
    ###OCR###

    # Provide the API with the Google Cloud Vision API
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'Keys/key_vision.json'

    # Initialize a Google Cloud Vision client
    client = vision.ImageAnnotatorClient()

    # Define file name and path
    FILE_NAME = 'DSC_0104.NEF'
    FOLDER_PATH = r'DataCollection/ValterSchytt-2-1962'
    response = detect_text(os.path.join(FOLDER_PATH, FILE_NAME))
    write_to_file(response)

if __name__ == "__main__":
    main()