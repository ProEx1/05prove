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
            print("Thoughts of hunger overwhelm your senses \nand you wake up in your own bed. \nWhat a strange dream! ")
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
        print(dash)
        if answer1_west_lights_miria.lower() == "run":
            print("You quickly turn to run, but smash directly into a tree. ")
            print("You wake up in your own bed. \nWhat a strange dream! ")
        elif answer1_west_lights_miria.lower() == "wave":
            print("Miria motions for the other elves to lower their bows. \nShe beckons you to follow, and leads you to their banquet. ")
            print("The buffet of strange and delicious foods in front of you \nmake you feel joyous and welcome. \nEverything is going to be alright. ")
        else:
            print("You have entered an incorrect response. \nPlease restart the program. ")
        #print(dash)
    elif answer1_west_lights.lower() == "yes":
        print("You blindly run at the lights but as you reach them \nthey all go out at once leaving you confused.")
        print("Thoughts of hunger overwhelm your senses \nand you wake up in your own bed. \nWhat a strange dream! ")
    else:
        print("You have entered an incorrect response. \nPlease restart the program. ")
    print(dash)


#EAST - DARKNESS
elif answer1.lower() == "east":
    print("You turn and slowly move down the path to the east, \ntaking in the calm air as you go. ")
    print("The trees tower and curl over you \nlike an ocean wave ready to break. ")
    print("The air gets thicker and thicker the further in you go. ")
    print("You start to ponder if you already had claustiphobia \nor if this is a new feeling. ")
    print(dash)
    answer1_fire = input("As the sun gets lower the forest \ngets too dark to see the trail. \nYou bump into a pile of wood, \ndo you want to try to build a fire? YES or NO? ")
    print(dash)
    if answer1_fire.lower() == "yes":
        print("In the dark you stumble around and put together \nsome logs and kindlin. \nWhile blindly reaching around, you find a box of matches. ")
        print("The flame is somehow darker than the \nsurrounding area and you feel even colder. ")
        print(dash)
        answer1_fire_fire2 = input("Do you want to try to EXTINGUISH the fire or STAY? ")
        print(dash)
        if answer1_fire_fire2.lower() == "extinguish":
            print("You scramble the logs and air rushes into where the flame was. \nYou hear a loud bang and are pushed back. ")
            print("You wake up in your own bed. \nWhat a strange dream! ")
        elif answer1_fire_fire2.lower() == "stay":
            print("You lay down and cover yourself with some leaves to stay warm, \nNot noticing the darkness of the flame is slowly spreading. ")
            print("The absolute darkness comsumes everything, including you. ")
            print("You wake up in your own bed. \nWhat a strange dream! ")
        else:
            print("You have entered an incorrect response. \nPlease restart the program. ")
        print(dash)
    elif answer1_fire.lower() == "no":
        print("You press on, the air smells foul, and the \nground below you feels more spongey. ")
        print("You feel water entering your shoes, \nyou can't see it, but you're sure you're in a swamp. ")
        print(dash)
        answer1_fire_water = input("The water is up to your knees now. Do you turn back? YES or NO? ")
        print(dash)
        if answer1_fire_water.lower() == "yes":
            print("You start to turn back but the swamp does not let go. ")
            print("You begin sinking, slowly at first, \nand faster as you struggle more. ")
            print("As the water starts to get to you face \nyou feel overcome with terror. ")
            print("You wake up in your own bed. \nWhat a strange dream! ")
        elif answer1_fire_water.lower() == "no":
            print("You press on, feeling the weight of the water \nand soft sand pulling you down. ")
            print("You see a light in the distance, \nit fills you with hope. ")
            print("You focus on the light as you keep \ntelling yourself it's just a bit further. ")
            print("In the light you can make out a large building. ")
            print("As you get closer you see a towering \nwhite building with gold windows. ")
            print("You make it to shore and pull yourself out \nof the water and mud. ")
            print('You see a sign that says, \n"Welcome to LAuberge Casino" ')
            print("You're horrified to realize you ended up in Louisiana. ")
        else:
            print("You have entered an incorrect response. \nPlease restart the program. ")
        print(dash)
            
    else:
        print("You have entered an incorrect response. \nPlease restart the program. ")
    #print(dash)



else:
    print("You have entered an incorrect response. \nPlease restart the program. ")
    print(dash)
