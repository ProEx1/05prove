"""
File: 05prove.py
Author: Joshua Smith

Purpose: A simple choose your own advendure game.
"""

dash = "------------------------------------------"
print(dash)
print("Welcome to the forests of Serenwilde. ")
print("Today is the 15th of Shanthin, 631 CE. ")
print(dash)
print("You awake, tired and sore. \nYou feel moss and earth in your hands as you lift yourself up.")
print("As you regain your senses you see the sun is starting to set. \nThe soft orange glow filters though the leaves of the trees. ")
print(dash)
answer1 = input("You see pathways to the NORTH, WEST, and EAST. \nWhich way do you chose? ")
print(dash)
#NORTH - FARM HOUSE
if answer1.lower() == "north":
    print("You slowly move down the path to the north, \ntaking in the calm air as you go. ")
    print("The trees are well spaced and the path looks \nlike it is in common use. ")
    print("You come to a small clearing in the forest. ")
    print("You notice a stone farm house covered in \nmoss and ivy with a wooden roof painted blue. ")
    print(dash)
    answer1_north_close = input("Would you like to get closer? YES or No? ")
    print(dash)
    if answer1_north_close.lower() == "no":
        print("You sneak around the edges of the tree line. \nYou pass along a sheep pin with a corgi working the flock. ")
        print("The dog is very distracted with the sheep and does not notice you. \nYou see a small barn that looks like it does not get much use. ")
        print(dash)
        answer1_north_close_barn = input("Do you want to enter the barn? YES or NO? ")
        print(dash)
        if answer1_north_close_barn.lower() == "yes":
            print("You enter the barn, it is old but comfortable and warm. \nFinding some soft hay, you lay down and drift off. ")
            print("Everything is going to be alright. ")
            print(dash)
        elif answer1_north_close_barn.lower() == "no":
            print("Thoughts of hunger overwhelm your senses and you wake up in your own bed. \nWhat a strange dream! ")
            print(dash)
        else:
            print("You have entered an incorrect response. \nPlease restart the program. ")
            print(dash)
    elif answer1_north_close.lower() == "yes":
        print("As you approach the farm you see the house \nhas light coming from inside, smoke from the chinmey, \nand the smell of stew cooking. ")
        print("You hear a dog bark from your left. \nAs you turn you see a small corgi \nrunning to you from a sheep pin. ")
        print(dash)
        answer1_north_close_puppy = input("Do you want to try to PET the dog or RUN? ")
        print(dash)
        if answer1_north_close_puppy.lower() == "run":
            print("You turn to run but the corgi \nhas already caught up to you. \nYou are pulled to the ground by the puppy \nand covered in lots of puppy kisses. ")
            print("You smile and pet the corgi, \neverything is going to be alright. ")
            print(dash)
        elif answer1_north_close_puppy.lower() == "pet":
            print("You smile and pet the corgi. \nThe owner of the farm aproaches, shakes your hand, \nand invites you in for dinner. \nEverything is going to be alright. ")
            print(dash)
        else:
            print("You have entered an incorrect response. \nPlease restart the program. ")
            print(dash)
    else:
        print("You have entered an incorrect response. \nPlease restart the program. ")
        print(dash)
#WEST - ELVES
elif answer1.lower() == "west":
    print("You turn and slowly move down the path to the west, \ntaking in the calm air as you go. ")
    print("The trees grow closer and closer together, \nfeeling like they will become one solid mass. ")
    print("The sun is glowing a faint dark red \nin the little space left between the trees. ")
    print(dash)
    answer1_west_lights = input("You see bright lights dancing in the distance! \nDo you run to the lights? YES or NO? ")
    print(dash)
    if answer1_west_lights.lower() == "no":
        print("You avoid the lights, but not trouble. \nAs you walk further down the path, \ndeeper into the woods, you keep your focus on the lights. ")
        print("Feeling eyes upon you, you tear your gaze away from the lights, \njust in time to see elves of green with bows drawn. ")
        print(dash)
        answer1_west_lights_miria = input("A tall wood elf ranger named Miria puts her bow down and waves. \nDo you WAVE or RUN? ")
        if answer1_west_lights_miria.lower() == "run":
            print("You quickly turn to run, but smash directly into a tree. ")
            print("You wake up in your own bed. \nWhat a strange dream! ")
        elif answer1_west_lights_miria.lower() == "wave":
            print("")


#EAST - DARKNESS
elif answer1.lower() == "east":
    print("You turn and slowly move down the path to the east, taking in the calm air as you go. ")


else:
    print("You have entered an incorrect response. \nPlease restart the program. ")
    print(dash)