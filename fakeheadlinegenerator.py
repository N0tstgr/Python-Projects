#1- import the random module

import random

#2 - creating subjects

subjects=[
    "vikash",
    "Not",
    "luxxy",
    "zuxxy",
    "A group of founders"
    "A alone leader"
]
actions = [
    "launches",
    "created",
    "builded",
    "changing",
    "created billion dollar company",
    "will lead the world and change  the world"
]
places_or_thing = [
    "rocket in the india",
    "a robot in the bangalore",
    "rocket",
    "the world",
    "at the age of 22",
    "and make the humanity multiplanetry"
]
#3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_thing)

    headline = f" BREAKING NEWS : {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

        #printing the  goodbye message
print("\n Thanks for using the fake news Headline gEnerator . Have a fun dssay")
