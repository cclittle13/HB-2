"""Utility file to seed ratings database from Yoga JSON file data in seed_data/"""

import json 

# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from model import (User, Category, Pose)
from model import connect_to_db, db
from posesite import app

def load_users():
    """
    load existing users from "yoga_users.txt" into database
    """

    print "Users"

    #yoga_users is a csv file 
    users_file = open("yoga_users")

    for line in users_file:
        line = line.rstrip()
        line = line.split(",")
        a_user = User(email=line[0],
                      password=line[1])
        db.session.add(a_user)

    # user = User(user_id=user_id, email=email)

    db.session.commit()


def load_categories(data_dict):
    """Loads categories from yoga_asanas.json file"""

    # import pdb; pdb.set_trace()
    # data = open("yoga_asanas.json")
    # data_dict = json.load(data)
    # print data_dict

    print "Categories"
    
    for category in data_dict:
        new_category = Category(category_name=category)
        print new_category
        db.session.add(new_category)

    db.session.commit()


def load_poses():
    """
    load poses from poses.txt into database
    """

    print "Poses"

    #yoga_users is a csv file 
    # users_file = open("poses_yoga.csv")
    users_file = open("poses.txt")

    for line in users_file:
        line = line.rstrip()
        line = line.split("|")
        pose = Pose(common_name=line[1],
                    sanskrit_name=line[2])
        db.session.add(pose)

    # user = User(user_id=user_id, email=email)


    #              common_name,
    #              sanskrit_name,
    #              breathe,
    #              image_url,
    #              category,
    #              random,

    db.session.commit()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    # users_file = open("./seed_data/users.csv.odt")
    users_file = ("poses.txt")
    data = open("yoga_asanas.json")
    print data
    data_dict = json.load(data)
    connect_to_db(app)
    db.create_all()
    #load_categories(data_dict)
    load_poses()
    #load_users()
    print "Connected to DB."