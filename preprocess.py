from config import *

import os

train_csv = open(TRAIN_CSV_PATH, "a")
test_csv = open(TEST_CSV_PATH, "a")

train_csv.write("video_name,tag\n")
test_csv.write("video_name,tag\n")

counter = 0

for category in os.listdir(DATASET_PATH):
    category_path = f"{DATASET_PATH}/{category}"
    if not os.path.isdir(category_path):
        continue

    for dir in os.listdir(category_path):
        dir_path = f"{DATASET_PATH}/{category}/{dir}"
        if not os.path.isdir(dir_path) or dir == "Annotation":
            continue

        for filename in os.listdir(dir_path):
            file_path = f"{DATASET_PATH}/{category}/{dir}/{filename}"
            if not os.path.isfile(file_path):
                continue

            if counter % TEST_MULTIPLIER == 0:
                test_csv.write(f"{file_path},{category}\n")
            else:
                train_csv.write(f"{file_path},{category}\n")
            counter += 1
