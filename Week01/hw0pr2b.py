# coding: utf-8
#
# hw0pr2b.py
#


import time


def adventure():
    sdelay = 1.0          # change to 0.0 for testing or speed runs,
    mdelay = 2.0                     # ..larger for dramatic effect!
    ldelay = 3.0
    print()
    print("Notice!! Please follow the instruction to enter the answer and make sure there's no typo")
    print("Please also follow the upper or the lower case that hint provide")
    print("Otherwise you might cause the program crash or the story mignt now show correctly.")
    print()
    time.sleep(ldelay)
    print("Let's start now!")
    time.sleep(mdelay)
    print()
    print("Recently, I went to a road trip.")
    print("So, if you are interested, I can share my story with you.")
    print()
    interested =  input("Please tell me are you interested to my story? [yes/no]")
    #4 An if, elif, ... control structure (with one or more elifs but no trailing else at all)
    time.sleep(sdelay)
    if interested =='yes':
        print("Cool, so let's start now!")
    elif interested != 'yes':
        print("Alright, I think you can force quit this program now :(")
    print()
    cityvisited = input("Before we start, do you want to make a guess how long did I drive? [yes/no]")
    #5 An if control structure (with no trailing elif nor trailing else at all)

    if cityvisited =='yes':
        print("Cool, but I will keep this as secret now!")
    print()
    time.sleep(sdelay)
    username = input("Now, tell me a name that you prefer me to call you: [Enter a name] ")

    print()
    print("Welcome,", username, "Now, let me start to tell you my story")
    print("If you want to go on a roadtrip, where do you want to go?")
    print("For me, I study in LA now, so I want to drive all the way up to Vancouver")
    print("However, there is a limitation for my visa so I decided only drive to Seattle")
    print("The total distance is 3152 miles, crazy huh?")
    print("During this trip, I visited Sacramento,Portland and Seattle")
    print("There are two of them I love most, make a guess which two cities are my best love")
    time.sleep(sdelay)
    print()
    firstg = input("Please make a first guess: [Sacramento/Portland/Seattle]")
    print('Remember, DO NOT enter the same guess for your second guess')
    time.sleep(mdelay)
    print('Ready for the second guess now? ')
    time.sleep(sdelay)
    print()
    secondg = input("Please make a second guess: [Sacramento/Portland/Seattle]")
    time.sleep(mdelay)
    print('......loading')
    time.sleep(ldelay)
    #2 An if, elif, elif, ... and else control structure (with at least two elifs)
    if firstg =='Sacramento' and secondg =='Portland':
        print("Nice guess, but Sacramento is too quiet and there was nothing I can visit when I went there")
    elif firstg =='Sacramento' and secondg =='Seattle':
        print("Nice guess, but Sacramento is too quiet and there was nothing I can visit when I went there")
    elif firstg =='Portland' and secondg =='Seattle':
        print("Brilliant, you go me!")
    elif firstg =='Seattle' and secondg =='Portland':
        print("Brilliant, you go me!")
    elif firstg =='Portland' and secondg =='Sacramento':
        print("Nice guess, but Sacramento is too quiet and there was nothing I can visit when I went there")
    elif firstg =='Seattle' and secondg =='Sacramento':
        print("Nice guess, but Sacramento is too quiet and there was nothing I can visit when I went there")
    print()
    time.sleep(ldelay)
    print('Now, I am thinking my next trip, but I am not sure where to visit')
    print('Can you give me a hand?')
    print("Your quest: Choose to visit Kyoto or Osaka")
    print()
    Destination = input("Where should I go? [Kyoto/Osaka]")
    #1 An if, elif, and else control structure (with exactly one elif)

    if Destination == "Kyoto":
        print("Nice, I heard Kyoto has lots of cool building, I want to get there and get some photos")
    elif Destination == "Osaka":
        print("OMG! I want to go to Universal, I am a fan of Harry Potter?")
    else:
        print("you chose somewhere I never though to go, is it fun?")
    print()

    time.sleep(sdelay)
    print("Hmmm......")
    print("Kyoto has some famous buildings\n")
    time.sleep(sdelay)
    print("Universal Studio has Harry Potter theme park, sounds amazing to me")
    print("Hmmm......So hard to decide")
    time.sleep(ldelay)
    print()
    print("Hmmm.....I think I make a decision")
    print("Do you know where do I want to go next time?")
    time.sleep(mdelay)
    print()
    print("A magic wand and two desination sign shows in front of you, grab the wand and point it to the correct answer")
    print()
    choice = input("Where do I want to go next time? [Kyoto/Osaka] ")

    #3 An if, else control structure (with zero elifs)
    if choice == "Osaka":
        print("the magic wand is waving it self and seems it is reading some spell...?\n")
        time.sleep(sdelay)
        print("the wand made a door in front of you, open the door and walk in..")
        time.sleep(sdelay)
        print("You see the corner shows the sign of 'Hogsmeade'\n")
        time.sleep(sdelay)
        print("You succeed, you got me that I want to visit Osaka for Harry Potter theme park")
        print("Enjoy Universal,", username, "!")

    else:
        print("the magic wand is waving it self and seems it is reading some spell...?")
        time.sleep(sdelay)
        print("the wand made a door in front of you, open the door and walk in..")
        time.sleep(sdelay)
        print()
        print("There are lots of famous buildings")
        print("but there are also a lot of snow too")
        print("I don't really like to visit the city during snowing day, you made a wrong guess.")
        print("Farewell,", username, ".")




