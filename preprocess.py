import os

train_csv = open("train.csv", "a")
test_csv = open("test.csv", "a")

train_csv.write("video_name,tag\n")
test_csv.write("video_name,tag\n")

counter = 0

for category in os.listdir("UCF11_updated_mpg"):
    category_path = f"UCF11_updated_mpg/{category}"
    if not os.path.isdir(category_path):
        continue

    for dir in os.listdir(category_path):
        dir_path = f"UCF11_updated_mpg/{category}/{dir}"
        if not os.path.isdir(dir_path) or dir == "Annotation":
            continue

        for filename in os.listdir(dir_path):
            file_path = f"UCF11_updated_mpg/{category}/{dir}/{filename}"
            if not os.path.isfile(file_path):
                continue

            if counter % 5 == 0:
                test_csv.write(f"{file_path},{category}\n")
            else:
                train_csv.write(f"{file_path},{category}\n")
            counter += 1
