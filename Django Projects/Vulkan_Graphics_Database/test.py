import os
import json
import pprint


def add_data(db):

    # configuring the path for the files
    BASE_DIR = ""
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
        "/geforce rtx 2070.json",
        "/geforce rtx 2080.json",
    ]

    # reading the files and extracting required data to store in Database
    # for file in graphics_list:

    file_name = JSON_DIR + "/geforce rtx 2080.json"

    with open(file_name, 'r') as f:
        data = json.load(f)

        # features = data['VkPhysicalDeviceFeatures']
        # print(features)
        # for i in features:
        #     print(i + " :", features[i])

    # Storing the features in the Database
    db.geforce_rtx_2080.insert_one(data)


def get_db():

    # importing MongoClient from pymongo
    from pymongo import MongoClient

    # Creating MongoClient instance at localhost:27017
    client = MongoClient('localhost:27017')

    # creating the database with  name  = 'vulkan_graphics'
    db = client.vulkan_graphics

    # returnng the created database
    return db


if __name__ == "__main__":

    # getting the instance of the db
    db = get_db()
    # adding the data to the Database
    add_data(db)
