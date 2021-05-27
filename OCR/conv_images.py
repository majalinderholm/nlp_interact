from PIL import Image
import os

directory = r'C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact/DataCollection/ValterSchytt-2-1962'

for filename in os.listdir(directory):
    if filename.endswith(".NEF"):
        print(filename)
        im = Image.open(directory + '/' + filename)
        filename = filename.replace(".NEF","")
        name=str(filename) +'.png'
        rgb_im = im.convert('RGB')
        rgb_im.save(name)
        print(os.path.join(directory, filename))
        continue
    else:
        continue