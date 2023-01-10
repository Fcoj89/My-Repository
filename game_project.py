name = input("Good Day! What is your name? \n")
print ("\n")
print ("Hello, " + name + ", welcome to your first adventure!\n")

while True:
        print ("Which class would you like to choose?\n" "Warrior\n" "Rogue\n" "Sorcerer\n")
        chosen_class = input()
        if chosen_class == "Warrior":
            print("Congratulations for joining our mighty forces, Warrior " + name)
            break
        elif chosen_class == "Rogue":
            print ("Welcome to our Brotherhood, fellow Rogue")
            break
        elif chosen_class == "Sorcerer":
            print ("We sense your native talent in the mystic arts, brother " + name)
            break
        else:
            print ("We're sorry, but the " + str(chosen_class) + " class is not a valid choice")

print ("\n")

print("As you take your first steps into this perilous world, you approach the barren town of Tristram.")
print("Your eyes gaze on what has remained of this once flourishing settlement; from a distance, you recognize the silhouettes of the few remaining townsfolk...")












