import os
import json


# Extracts the graphics features from their respective json Files

def convert():
    # configuring the path for the files
    BASE_DIR = ""
    RAW_DIR = os.path.join(BASE_DIR, "raw Files")
    JSON_DIR = os.path.join(BASE_DIR, "json Files")
    # list of all the .json files
    graphics_list = [
        "/geforce 940mx.json",
        "/geforce gt 640.json",
        "/geforce gt 730.json",
        "/geforce gt 1030.json",
        "/geforce gtx 670.json",
        "/geforce gtx 760.json",
        "/geforce gtx 770.json",
        "/geforce gtx 970.json",
        "/geforce gtx 1050.json",
        "/geforce gtx 1060 6gb.json",
        "/geforce gtx 1060.json",
        "/geforce rtx 2070.json",
        "/geforce rtx 2080.json",
    ]

    for file in graphics_list:

        input_file = RAW_DIR + file
        output_file = JSON_DIR + file

        # Opening the json files and extracting the features from it
        with open(input_file, 'r') as f:
            data = json.load(f)

            features = data['environment']

        # Storing the Extracted features in the new .json Files.
        with open(output_file, 'a') as f:
            json.dump(features, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    convert()