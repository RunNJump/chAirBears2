from imageai.Detection import ObjectDetection
from datetime import datetime

# access / parse related
import os
import glob
import json

# process related
import statistics
import preprocess_image as im

FILE_EXTENSIONS = ['*.jpg', '*.jpeg', '*.png']
ROOT = os.getcwd()

# setup paths
IMG_PATH = os.path.join(ROOT, 'images/input')
INPUT_PATH = os.path.join(ROOT, 'images/output')
OUTPUT_PATH = os.path.join(ROOT, 'output')

# setup model
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(ROOT, "yolo.h5"))
detector.loadModel()
stat = dict()

# heuristics
heuristics = {
    'person': 1,
    'laptop': 1,
    'backpack': 0.6,
    'book': 0.4,
    'chair': 0.3,
    'cell phone': 0.2,
}

# object customization
objects = detector.CustomObjects(
    person=True,
    laptop=True,
    backpack=True,
    book=True,
    chair=True,
    cell_phone=True,
)

# retrieve image array
images = []

os.chdir('./images/input')
for ext in FILE_EXTENSIONS:
    images.extend(glob.glob(ext))
os.chdir('../../../records')

# seat assignment
seats = dict()  # true if it's occupied

# # crop images
# for f in images:
#     im.crop(os.path.join(img_path, f))
# # get actual images
# images.clear()
# os.chdir('./images/output')
# images.extend(glob.glob("*.jpeg"))
# os.chdir('../../')
# cd = os.getcwd()

# update
for fn in images:
    detections = detector.detectObjectsFromImage(input_image=os.path.join(IMG_PATH, fn),
                                                 output_image_path=os.path.join(OUTPUT_PATH, fn),
                                                 minimum_percentage_probability=70)

    number_of_people, number_of_seats = 0, 0
    precision = 0
    for obj in detections:
        if obj['name'] == 'person':
            number_of_people += 1
        if obj['name'] == 'chair':
            number_of_seats += 1
        precision += heuristics[obj['name']] * obj['percentage_probability'] if obj['name'] in heuristics else 0.01

    available_seats = number_of_seats - number_of_people if number_of_seats > number_of_people else 0
    seats[fn] = available_seats if precision > 0.8 else 0

    if fn not in stat:
        stat[fn] = []
    stat[fn].append((
        number_of_seats,
        number_of_people,
        available_seats,
    ))
    print(stat)

now = datetime.now()
# records data
with open('{}--data.json'.format(now), 'w', encoding="utf-8") as f:
    json.dump(seats, f, indent=4, sort_keys=True, ensure_ascii=False)
    f.close()

# record stats
with open('{}--stat.json'.format(now), 'w', encoding="utf-8") as f:
    json.dump(stat, f, indent=4, sort_keys=True, ensure_ascii=False)
    f.close()

print(seats)

# We also stored all the metadata in the records folder as the form of JSON.