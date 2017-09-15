





import random
import time
import sys
import time

def exitRoutine():
    print (' _______ _______ _______ _______      _______ ___ ___ _______ ______  ')
    print ('|     __|   _   |   |   |    ___|    |       |   |   |    ___|   __ \ ')
    print ('|    |  |       |       |    ___|    |   -   |   |   |    ___|      < ')
    print ('|_______|___|___|__|_|__|_______|    |_______|\_____/|_______|___|__| ')
    exit ()

def displayIntro():
    print('                                       _           _     __ _  __  ')    
    print(' /\ /\ _ __   _____  ___ __   ___  ___| |_ ___  __| |   / /(_)/ _| ___') 
    print("/ / \ \ '_ \ / _ \ \/ / '_ \ / _ \/ __| __/ _ \/ _` |  / / | | |_ / _ \ ")
    print('\ \_/ / | | |  __/>  <| |_) |  __/ (__| ||  __/ (_| | / /__| |  _|  __/')
    print(' \___/|_| |_|\___/_/\_\ .__/ \___|\___|\__\___|\__,_| \____/_|_|  \___|')
    print('                      |_|                                             ')

    time.sleep(2)
    print("You are on a train traveling through uncharted area")
    time.sleep(2)
    print('')
    print('       o o o o o .  .  . . ')
    print('     o  ____                         ')
    print('   _][__[] |  ______   ______   ______')
    print('  (        | |______| |______| |______|')
    print('  /-O----O-- ~O----O   O----O ~ O----O ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Ascii done by me
    print('')
    time.sleep(2)
    print('The conductor passes out and you are left to conduct the train!!')
    time.sleep(4)
    print('You cannot stop the train... There is a 2 way switch ahead on the tracks,')
    time.sleep(4)
    print('one will lead you to the next station the other will derail the train.')
    time.sleep(4)
    
def chosenRail ():
#RAIL CHOICE
    rail = ' '
    while rail != '1' and rail != '2':
        print('which direction do you choose?')
        print('Left  = "1"')
        print('Right = "2"') 
        rail = input()

    return rail


def checkRail(chosenRail):
#I used golbal variables for money
    global money
    money = 0
#RAIL NAME
    if chosenRail == str(1):
        RailD = "LEFT"
    if chosenRail == str(2):
        RailD = "RIGHT"

    print ('You approach the swtich...') 
    time.sleep(2)
    print ('Eveyone on the train is screaming...')
    time.sleep(2)
    print ('You change the switch to go ' + RailD )
    print ()
    time.sleep(2)

    friendlyRail = random.randint(1,2)

    if chosenRail == str (friendlyRail):
        print('The train makes it to the station safely ')
        time.sleep(2)
        print('  ____||____')
        print(" /         /\ ")
        print("/_________/  \ ")
        print('|    _    |  |     //================\\ ')
        print('|[] | | []|[]|     ||                || ')
        print('|___|_|___|__|_____||________________||_')
        print('')
        #Ascii done by me
        time.sleep(2)
        print('The passengers reward you with $100')
#MONEY ADDED
        money = money + 100
        print()
        time.sleep(1)
        print('CASH = $' + str(money))
        time.sleep(3)

    else:
        print ("The train flips off the rails !!")
        time.sleep(1)

        print('     _.-^^---....,,--')
        print(' _--                  --_')
        print('<                        >)')
        print('|                         |')
        print(' \._                   _./')
        print("    ```--. . , ; .--'''")
        print('          | |   |')
        print('       .-=||  | |=-.')
        print("       `-=#$%&%$#=-'")
        print('          | ;  :|')
        print(' _____.,-#%&$@%#&#~,._____  ')
        time.sleep(3)
#EXIT ROUTINE
        print ('Would you like to play again? 1 for yes, 2 for no')
        choice = input()
        choice = int(choice)

        if int(choice) ==2:
            exitRoutine()
        else:
            displayIntro()
            railNumber = chosenRail()
            checkRail(railNumber)
            Level2 ()
            chosen2 ()
            checkChoice2()          
            levelThree()
            blackJack()
            levelFour()
            levelFour2()
#Level 2
def Level2 ():
    print ("You exit the train station and begin walking through the busy streets of New York.")
    time.sleep(3)
    print()
    print ('               |MMMMMMMMM|                _')
    print ('   ________    |MMMMMMMMM|              _|l|_')
    print ('  |!!!!!!!_|___|MMMMMMMMM|             |lllll|')
    print ('  |!!!!!!|=========|MMMMM|             |lllll|_______')
    print ('  |!!!!!!|=========|MMMMM|            _|lllll|HHHHHHH|')
    print ('  |!!!!!!|=========|MMMMM|   ________|lllllllll|HHHHH|')
    print ('  |!!!!!!|=========|MMMMM|  |unununun|lllllllll|HHHHH|______')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('  |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|')
    print ('---------------------------------------------------------------')
    time.sleep(2)

    print ("You are in a rush to get home, there are two different routes you can take to")
    time.sleep(3)
    print ("get home faster. The alley way, or the tunnel")

def chosen2 ():
#ALLEY OR TUNNEL CHOICE
    global choice2
    choice2 = ' '
    while choice2 != '1' and choice2 != '2':
        print('which route do you choose?')
        print('Alley  = "1"')
        print('Tunnel = "2"') 
        choice2 = input()




def checkChoice2():
    global money
#I used golbal variable to keep track of stealing money
    global BAD
    BAD = 0
    if choice2 == str(1):
        ChoiceD = "alley"
    if choice2 == str(2):
        ChoiceD = "tunnel"

    print ('You adjust your route and head towards the ' + ChoiceD) 
    time.sleep(2)
    print ('You enter the ' + ChoiceD + ' and begin speed walking  through it')
    time.sleep(2)
    print ('You here a noise behind you, you turn around and... ')
    time.sleep(2)
#ALLEY CHOICE
    if choice2 == str(1):
        print ("A robber is holding you at gunpoint!!!!!")
        time.sleep(1)
        print(" _______________")
        print("|   ____________|")
        print("|  |_]")
        print("|__|")
#Ascii done by me
        print()
        time.sleep(2)
        print("He says if you dont give him all of your money will shoot you.")
        time.sleep(2)
        global choice1
        choice1 = '  '
        print("You have two options, fight back, or give him all your money")
        time.sleep(2)
        print('what do you choose?')
        print('Fight  = "1"')
        print('Loose Money = "2"') 
        choice1 = input()

        if choice1 == str(1):
            win = random.randint(1,2)
            print("You turn around and grab hold of his gun, you both begin to struggle for control")
            time.sleep(5)
            if win == 1:
                print("You could not overpower him and you get shot!")
                print()
                time.sleep(2)
                print ('Would you like to play again? 1 for yes, 2 for no')
                choice = input()
                choice = int(choice)

                if int(choice) ==2:
                    exitRoutine()
                else:
                    displayIntro()
                    railNumber = chosenRail()
                    checkRail(railNumber)
                    Level2 ()
                    chosen2 ()
                    checkChoice2()          
                    levelThree()
                    blackJack()
                    levelFour()
                    levelFour2()
            else:
                print("You overpower the robber and knock him out cold...")
                time.sleep(2)
                print("you notice he has $200 in his pocket do you take it?.")
                time.sleep(2)
                print('Yes  = "1"')
                print('No = "2"')
                choice3 = input()
#STEAL MONEY 
                if choice3 == str(1):
                    money = money + 200
                    print('you bend over and grab the money')
                    time.sleep(2)
                    print('CASH + $' + str(money))
                    time.sleep(2)
                    print("You continue walking and make it out of the alley")      
#BAD IS SET TO 1
                    BAD = BAD +1
                else:
                    print('You continue walking and make it out of the alley')
#TUNNEL CHOICE                      
    else:
        print ("A bat flies down and begins to attack you!!!")
        time.sleep(1)
        print(' /\                 /\ ')
        print("/ \'._   (\_/)   _.'/ \ ")
        print("|.''._'--(o.o)--'_.''.| ")
        print(' \_ / `;=/ " \=;` \ _/ ')
        print("   `\__| \___/ |__/` ")
        print("        \(_|_)/ ")
        print('         " ` " ')
        print()
        time.sleep(2)
        print("You try swatting the bat away")
        bat = random.randint(1,4)
        time.sleep(2)
#random chance to die from bat
        if bat == 1:

            print("The bat is poisonous and kills you!")
            time.sleep(4)
            print()
            print ('Would you like to play again? 1 for yes, 2 for no')
            choice = input()
            choice = int(choice)

            if int(choice) ==2:
                exitRoutine()
            else:
                displayIntro()
                railNumber = chosenRail()
                checkRail(railNumber)
                Level2 ()
                chosen2 ()
                checkChoice2()          
                levelThree()
                blackJack()
                levelFour()
                levelFour2()
        else:
            print("You scare the bat and it flies away!")
            time.sleep(2)
            print("You continue down the tunnel and then you feel something cold")
            time.sleep(2)
            print("pressed against the back of your head...")
            print ("A robber is holding you at gunpoint!!!!!")
            time.sleep(2)
         
            print(" ")
            print("            ||||||||||||||")
            print("           =              \  ")
            print("           =               |")
            print("          _=            ___/")
            print("         / _\           (o)\ ")
            print("        | | \            _  \ ")
            print("        | |/            (____)")
            print("         \__/          /   |")
            print("          /           /  ___)")
            print("         /    \       \    _)                       )")
            print("        \      \           /                       (")
            print("      \/ \      \_________/   |\_________________,_ )")
            print("       \/ \      /            |     ==== _______)__)")
            print("       \/ \    /           __/___  ====_/")
            print("         \/ \  /           (O____)\\_(_/")
            print("                          (O_ ____)")
            print("                           (O____)")
            print("")
            print()
            time.sleep(2)
            print("He says if you dont give him all of your money, he will shoot you.")
            time.sleep(2)
            global cchoice1
            choice1 = '  '
            print("You have two options, fight back, or give him all your money")
            time.sleep(2)
            print('what do you choose?')
            print('Fight  = "1"')
            print('Loose Money = "2"') 
            cchoice1 = input()

            if cchoice1 == str(1):
                win = random.randint(1,2)
                print("You turn around and grab hold of his gun, you both begin to struggle for control")
                time.sleep(4)
                if win == 1:
                    print("You could not overpower him and you get shot!")
                    time.sleep(4)
                    print()
                    print ('Would you like to play again? 1 for yes, 2 for no')
                    choice = input()
                    choice = int(choice)

                    if int(choice) ==2:
                        exitRoutine()
                    else:
                        displayIntro()
                        railNumber = chosenRail()
                        checkRail(railNumber)
                        Level2 ()
                        chosen2 ()
                        checkChoice2()          
                        levelThree()
                        blackJack()
                        levelFour()
                        levelFour2()
                else:
                    print("You overpower the robber and knock him out cold...")
                    time.sleep(2)
                    print("you notice he has $200 in his pocket do you take it?.")
                    time.sleep(3)
                    print('Yes  = "1"')
                    print('No = "2"')
                    choice3 = input()

                    if choice3 == str(1):    
                        BAD = 1
                        
                        money = money + 200
                        print('you bend over and grab the money')
                        time.sleep(2)
                        print('CASH + $'+str(money))
                        time.sleep(2)
                        print("you continue walking and make it out of the alley")
                    else:
                        print('You continue walking and make it out of the alley')
                          
def levelThree():
    print ('You continue on your way home and are stopped by a man sitting')
    time.sleep(3)
    print ('on the side of the road, he offers to play you in a game of blackjack.')
    time.sleep(3)
    print ('you have to bet all your money, the winner takes all')
    time.sleep(3)
    print('what do you choose?')
    print('Yes  = "1"')
    print('No   = "2"') 
    global choice3
    choice3 = input()
           
def blackJack():
    global choice3
    global money
    if choice3 == str(1):            


#initalizing variables
        number= random.randint(1,11)
        aceChoice=0
        playerWins=0
        dealerWins=0
        playerCards =[]
        dealerCards =[]
        print("Reach a final score higher than the man without exceeding 21")
        time.sleep(3)
        print("Over 21 is a bust and automatic win for the man sitting on the road")
        time.sleep(3)
        while playerWins <3 or dealerWins <3:

            if dealerWins == 3:
                break
            if playerWins == 3:
                break

    # Creating dealers staring deck
            while len(dealerCards) != 2:
                cardD=random.randint(1, 11)
        #Adds card to deck
                dealerCards.append(cardD)
    # Creating players starting deck
            while len(playerCards) != 2:
                cardP = random.randint(1, 10)
        #If ace is drawn you are given the option to choose 1 or 11
                if cardP == 1:
                    print('You drew an Ace')
                    print('Would you like it to be worth 11 or 1?')
                    aceV=input()
                    if aceV == "11":
                        cardP = 11
                    if aceV == "1":
                        cardD = 1
        #Adds card to deck
                playerCards.append(cardP)
        
                if len(playerCards) == 2:
                    print()
                    print("Your total is " + str(sum(playerCards)) + " You drew a ", playerCards)
           
    #Asks player for hit or stick
            while sum(playerCards) < 21:
                choice=str(input('"hit" or "stick?"'))
                print()
        #If hit then another random interval is drawn from 1-10
                if choice == "hit":
                    number= random.randint(1,10)
            #If ace is drawn you are given the option to choose 1 or 11
                    if number ==1:
                        print('You drew an Ace')
                        print('Would you like it to be worth 11 or 1?')
                        aceV=input()
                        if aceV == "11":
                            number = 11
                        if aceV == "1":
                            number = 1
            #Adds card to deck
                    playerCards.append(number)
    
                    print("Your total is now " + str(sum(playerCards)) + " with these cards ",playerCards)
        #if stick then dealer hits until over 17
                elif choice == "stick":
                    while sum(dealerCards) < 17:
                        number= random.randint(1,11)
                #Adds card to deck
                        dealerCards.append(number)

                    print("The man has a total of " + str(sum(dealerCards)) + " with ", dealerCards)
                    print("You have a total of " + str(sum(playerCards)) + " with ", playerCards)
            #Checking dealer's deck sum for Bust or Blackjack
            #greater than 21 is instant bust
                    if sum(dealerCards) > 21:
                        print("man has BUSTED!")
                        playerWins = playerWins +1
                        print("You " +str(playerWins)+ " - " +str(dealerWins)+ " Man")
                        break

                #excatly 21 is instant win
                    elif sum(dealerCards) == 21:
                        print("man has BLACKJACK and wins! 21")
                        dealerWins = dealerWins + 1
                        print("You " +str(playerWins)+ " - " +str(dealerWins)+ " Man")
                        break

    #Deck sums used to see who wins
            #Checking for Draw
                    if sum(dealerCards) == sum(playerCards):
                        print("DRAW")
                        print("You " +str(playerWins)+ " - " +str(dealerWins)+ " Man")
                        break
            #Checking dealers deck sum
                    if sum(dealerCards) > sum(playerCards):
                        print("MAN WINS")
                        dealerWins = dealerWins + 1
                        print("You " +str(playerWins)+ " - " +str(dealerWins)+ " Man")
                        break
         
                    else:
                        print("YOU WIN")
                        playerWins = playerWins + 1
                        print("You " +str(playerWins)+ " - " +str(dealerWins)+ " Man") 
                        break

   
    

    #excatly 21 is instant win
            if sum(playerCards) == 21:
                print("You have BLACKJACK! You Win! 21")
                playerWins = playerWins + 1
    #greater than 21 is instant bust
            elif sum(playerCards) > 21:
                print("You BUSTED! man wins.")
                dealerWins = dealerWins + 1
               

            playerCards=[]
            dealerCards=[]
        print()
#Checking first to five for bets
        if dealerWins>playerWins:
            print("You lost")
            money = money - money
            print('CASH  $' + str(money))
        else:
            print("You Won $")
            money = money*2
            print('CASH  $' + str(money))
        print("The man thanks you for playing and you continue on your way home")
    else:
        print("You tell the man you are not interested and continue on your way home")

def levelFour():
        print("You finally make it home, you walk into your kitchen and scratch your,")
        time.sleep(3)
        print("scratch card from last night...")
        time.sleep(3)
#CHANCE TO WIN MONEY
        print(" ________")
        print("|SCRATCHY|")
        print("| [][][] |")
        print("| [][][] |")
        print("| [][][] |")
        print("|________|")
#Ascii done by me
        time.sleep(5)
        winS=random.randint(1,5)
        if winS == 3:
            print("HOLY MOLEY!! YOU WON $1000!!!!")
            global money
            money = money + 1000
            print('CASH  $' + str(money))
        else:
            print("you didnt win anything...")

        print("You are tired and want to watch some TV before bed. You walk to your living room")
        time.sleep(3)
        print("and notice there is a letter sitting on your coffee table, you pick it up and read it")
        time.sleep(3)
        print(" __________________________________")
        print("|    ROBBER ASSOCIATION            |")
        print("|Dear Reader,                      |")
        print("|                                  |")
        print("|You have been chosen to take      |")
        print("|part in the biggest heist         |")  
        print("|ever. Our decision to involve     |")
        print("|you is based on your confrontaion |")
        print("| with Dan (our leader) earlier    |")
        print("|today you showed all the          |")                    
        print("|important traits of a true        |")
        print("|robber. You can not turn          |")
        print("|down this offer, we will          |")
        print("|see you in the morning.           |")
        print("|__________________________________|")
        time.sleep(15)
        print("You somehow are not worried about this letter, and just accept what")
        time.sleep(3)
        print("is going to happen. You are really tired and fall asleep while watching TV.")
        time.sleep(3)
        print("ZZZZzzzZZZzzzzzZZZZzzzzzZZZZzzzz")
        time.sleep(3)
        print("zzzzzzzzZZZZZZzzzZZZzzzZZzzZZZZzzzzzZZZZzzzz")
        time.sleep(3)
        print("You wake up to a room full of people with masks on, and they are all looking at you.")
        time.sleep(3)
        print("You see the robber from last night, and he seems to be the leader, he stands up from")
        time.sleep(3)
        print("your chair and tells you about the heist. You will be robbing the bank of New York,")
        time.sleep(3)
        print("They have it all planned out and its happening today. They have taken all the money")
        time.sleep(3)
        print("in your house, a total of $" + str(money) + " and bought you weapons")
        global strength
#IF STATEMENTS TO GET YOUR GEAR BASED ON MONEY
        if money == 0:
            print("because you had no money, they donated you a lollypop, to use fore the heist")
            time.sleep(3)
            print("     ___ ")
            print("    /   \ ")
            print("    \___/ ")
            print("      |  ")
            print("      |  ")
            print("      |  ")
#Ascii done by me
            strength = 1


        if 0 < money <= 200:
            print("because you had $200 or less you got a pistol")
            time.sleep(1)
            print(" _______________")
            print("|   ____________|")
            print("|  |_]")
            print("|__|")
#Ascii done by me
            print()
            time.sleep(2)
            strength = 2




        elif 200 < money <= 500:
            print("because you had $500 or less you got a SMG and a bullet proof vest")
            time.sleep(3)
            print("  ||")
            print("  ||_________________________/'|")
            print(" _| O======/                   |")
            print("|_|              ============  |")
            print("  |  __  ______________________|")
            print("  |_/  )(     |___||     O-   /")
            print("      (  )    /  / |_________/")
            print("      (  )   /  /    | ) |   |")
            print("      (__)  /  /     \___|__(")
            print("           /  / BigFoot  )   \ ")
            print("          /  /            )   \ ")
            print("         /  /              )___\ ")
            print("        /  /")
            print("       /__/")
            print("             _______          _______")
            print("            /       \        /       \ ")
            print("           |         \      /         |")
            print("           |   ====   \____/   ====   |")
            print("           |                          |")
            print("           |                          |")
            print("           |       BULLET PROOF       |")
            print("           |                          |")
            print("           |                          |")
            print("           |                          |")
            print("           |==========================|")
            print("           |                          |")
            print("           |==========================|")
            print("           |                          |")
            print("           |__________________________|")
            print("")
            strength = 3


        elif 500 < money <= 1000:
            print("because you had $1000 or less you got a assult rifle and a bullet proof vest")
            time.sleep(3)
            print( )
            print("                    \--+ +-______________________________________________")
            print("                _____/===%====/======------------------------------------!\ ")
            print(" ______________/ / //! ||||||||||||| (%) ================    ======      ! X")
            print("'______________! ! !!! ||||||||||||||| ._================_.. ======   -- ! X")
            print("               \\\\\\\ o||XX|||XX||o||_!  o   { o    }     |===----------!M|")
            print('                """"""\_!_!_|_!_!_!!!/ !________!-------___X____________ !-.')
            print("                                       |     X  ||__|  |.            ^\\ o |")
            print("                                       | |    / |!     ||              \\  |")
            print('                                       |     /""|!!!   |"               || |')
            print('                                       "----"   |!!!!! ".               || |')
            print("                                                |!!+-+!!|                | |")
            print("                                                |!!|:|!!|                | |")
            print("                                                `--+-+--                 `- ")

            print("             _______          _______")
            print("            /       \        /       \ ")
            print("           |         \      /         |")
            print("           |   ====   \____/   ====   |")
            print("           |                          |")
            print("           |                          |")
            print("           |       BULLET PROOF       |")
            print("           |                          |")
            print("           |                          |")
            print("           |                          |")
            print("           |==========================|")
            print("           |                          |")
            print("           |==========================|")
            print("           |                          |")
            print("           |__________________________|")
            print("")
            strength = 4


        elif 1000<= money:
            print("because you had less than $1000 you got a suit of armor and laser rifle")
            time.sleep(3)
            print("          ___")
            print("         /---\ ")
            print('        |[===]|')
            print('        |[===]|')
            print('         \_ _/')
            print('       _.d._.b.__')
            print('   +"i\  |\_/|  /i"+')
            print('   [_| \ |   | / |_]')
            print("  .' |  ):===:(  | `.")
            print('  |:./+-" | | "-+\.:|')
            print('  |_| |-. |_|   | |_|')
            print('  \:\ |-  /+\   ! |:| ')
            print('   \ \|n._\+/_.n| / /')
            print('    \::::::-:::::/ /')
            print('     \            /')
            print('      |: \   / :|')
            print('      |:  i-i  :|')
            print('      |:  | |  :|')
            print('      |:  | |  :|')
            print('      |;_ | |__;|')
            print('      (__() ()__)')
            print('      |:  | |  :|')
            print("      /---\ /---\ ")
            print("")
            print("        ")
            print(" _______|_|              .-.   .-|-===-|------|b|      .o8")
            print("|         |-------|------| |---| ||o  ||    | |88888888888")
            print("|_________|-------|______| `---' ||___||    o `~~~~~~~8888")
            print("`-------|_|-------|HHHHHHHHHHHHHH|-----|~~~________|_|8888")
            print("       =[_]=                   |++-----+--|  )888  \__8888")
            print("                               ||         `==='88b    `888")
            print("                                               888     `88")
            print("                                               `88b     `8")
            strength = 5
        
def levelFour2():
    time.sleep(4)
    print("Everyone in the room cheers for your awesome gear!! And then you all stand up")
    time.sleep(2)
    print("and head towards the bank")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("You make it to the bank, they ask you if they should enter through the roof or the front door")
    time.sleep(3)
    print('Roof  = "1"')
    print('Door   = "2"') 
    qchoice4 = input()
    global BAD
    global strength
#global money 2 is used to keep track of stolen money
    global money2
    money2 = 0
#ROOF CHOICE
    if qchoice4 == str(1):
        print("You use a grapple hook to make it to the roof")
        roof = random.randint(1,4)
        time.sleep(2)
        if roof == 3:

            print("The hook breaks and you fall and die!")
            time.sleep(4)
            print()
            print ('Would you like to play again? 1 for yes, 2 for no')
            choice = input()
            choice = int(choice)

            if int(choice) ==2:
                exitRoutine()
            else:
                displayIntro()
                railNumber = chosenRail()
                checkRail(railNumber)
                Level2 ()
                chosen2 ()
                checkChoice2()          
                levelThree()
                blackJack()
                levelFour()
                levelFour2()
        else:
            print("You make it to the roof,and begin drilling through it into the safe room.")
            time.sleep(2)
            print("The drill makes it through and you jump down into the room and begin taking")
            time.sleep(2)
            print("all the money and putting it into duffle bags.")
            money2 = money2 +1256524626
            print('CASH  $' + str(money2))      
            time.sleep(2)
            money2 = money2 +40245645624
            print('CASH  $' + str(money2))      
            time.sleep(2)
            money2 = money2 +1267424645624562456
            print('CASH  $' + str(money2))      
            time.sleep(2)
   
            print("You here someone unlocking the safe room what do you do?")
            time.sleep(2)
            print('Tell them the safe is occupied  = "1"')
            print('Nothing = "2"') 
            choice5 = input()
            if choice5 == str(1):
                print("The Person gets scared and calls the police! there is a shootout in the bank!!")
                time.sleep(3)
                print("                    ____            ____            ____")
                print("                   /....\          /....\          /....\ ")
                print("                  |::::::|    .-. |::::::|    .-. |::::::|")
                print("                  |::::::|    | | |::::::|    | | |::::::|")
                print("                  (`:'':')    | | (`:'':')    | | (`:'':')")
                print("                 _--|__|--__  | |.--|__|--__  | |_--|__|--__")
                print("                |   ________|_|_|_  ________|_|_|_  ________|_____")
                print("      __       /    |            |  |            |  |            |")
                print("    |____ |   /  /  |            |  |            |  |            |")
                print("        | |_ /  /|  |            |  |            |  |            |")
                print("           ----- |  |  M  U  P   |  |  M  U  P   |  |  M  U  P   |")
                print("                 |`-|            |`-|            |`-|            |")
                print("                 |`-|            |`-|            |`-|            |")
                print("                 |  |            |  |            |  |            |")
                print("                 |  |            |  |            |  |            |")
                print("                 |  |            |  |            |  |            |")
                print("                 |`-|            |`-|            |`-|            |")
                print("                 |__|            |__|            |__|            |")
                print("                 /_ |            |_ |            |_ |            |")
                print("                |___`-__________-'__`-__________-'__`-__________-'")
                time.sleep(2)
                if strength == 1:
                    print("You cant fight back with a lolly pop... you die")
                    time.sleep(4)
                    print()
                    print ('Would you like to play again? 1 for yes, 2 for no')
                    choice = input()
                    choice = int(choice)

                    if int(choice) ==2:
                        exitRoutine()
                    else:
                        displayIntro()
                        railNumber = chosenRail()
                        checkRail(railNumber)
                        Level2 ()
                        chosen2 ()
                        checkChoice2()          
                        levelThree()
                        blackJack()
                        levelFour()
                        levelFour2()
                elif strength == 2:
                    print("you put up a good fight with your weapons...")
                    time.sleep(2)
                    print("But you get shot and die")
                    time.sleep(4)
                    print()
                    print ('Would you like to play again? 1 for yes, 2 for no')
                    choice = input()
                    choice = int(choice)

                    if int(choice) ==2:
                        exitRoutine()
                    else:
                        displayIntro()
                        railNumber = chosenRail()
                        checkRail(railNumber)
                        Level2 ()
                        chosen2 ()
                        checkChoice2()          
                        levelThree()
                        blackJack()
                        levelFour()
                        levelFour2()
                elif strength ==3:
                    print("you put up a good fight with your weapns...")
                    time.sleep(2)
                    print("You just manage to fight off the cops and escape, but loose $10000 while running")
                    time.sleep(2)
                    money2 = money2 - 100000
                    time.sleep(2)
                    print('CASH  $' + str(money))      
                    time.sleep(2)
                elif strength ==4:
                    print("you put up a great fight with your weapons...")
                    time.sleep(2)
                    print("You just manage to fight off the cops and escape!")
                elif strength ==5:
                    print("your weapons are so cool the cops refuse to fight you...")
                    time.sleep(2)
                    print("each cop give you all the money in their to stop you from fighting them")
                    time.sleep(3)
                    money2 = money2 + 20000
                    print('CASH  $' + str(money))      
                    time.sleep(2)
                    print("The cops let you walk out of the bank without a fight") 
            else:
                print("They stop unlocking the door and walk away")
                time.sleep(2)
                print("You gather up all you stuff and escape the bank")
                  
    else:
        print("You run inside the bank with your weapons drawn!!")
        time.sleep(2)
        print("You tie up everyone and get an employee to open the safe")
        time.sleep(2)
        print("you start taking all the money and putting it into duffle bags.")
        money2 = money2 +134235435
        print('CASH  $' + str(money2))      
        time.sleep(2)
        money2 = money2 +4345345235
        print('CASH  $' + str(money2))      
        time.sleep(2)
        money2 = money2 +14352346452456452445
        print('CASH  $' + str(money2))      
        time.sleep(2)
        print("You forgot to tie up somebody and they call the police! there is a shootout in the bank!!")
        time.sleep(2)
        print("                    ____            ____            ____")
        print("                   /....\          /....\          /....\ ")
        print("                  |::::::|    .-. |::::::|    .-. |::::::|")
        print("                  |::::::|    | | |::::::|    | | |::::::|")
        print("                  (`:'':')    | | (`:'':')    | | (`:'':')")
        print("                 _--|__|--__  | |.--|__|--__  | |_--|__|--__")
        print("                |   ________|_|_|_  ________|_|_|_  ________|_____")
        print("      __       /    |            |  |            |  |            |")
        print("    |____ |   /  /  |            |  |            |  |            |")
        print("        | |_ /  /|  |            |  |            |  |            |")
        print("           ----- |  |  M  U  P   |  |  M  U  P   |  |  M  U  P   |")
        print("                 |`-|            |`-|            |`-|            |")
        print("                 |`-|            |`-|            |`-|            |")
        print("                 |  |            |  |            |  |            |")
        print("                 |  |            |  |            |  |            |")
        print("                 |  |            |  |            |  |            |")
        print("                 |`-|            |`-|            |`-|            |")
        print("                 |__|            |__|            |__|            |")
        print("                 /_ |            |_ |            |_ |            |")
        print("                |___`-__________-'__`-__________-'__`-__________-'")
        time.sleep(3)
        if strength == 1:
            print("You cant fight back with a lolly pop... you die")
            time.sleep(4)
            print()
            print ('Would you like to play again? 1 for yes, 2 for no')
            choice = input()
            choice = int(choice)

            if int(choice) ==2:
                exitRoutine()
            else:
                displayIntro()
                railNumber = chosenRail()
                checkRail(railNumber)
                Level2 ()
                chosen2 ()
                checkChoice2()          
                levelThree()
                blackJack()
                levelFour()
                levelFour2()
        elif strength == 2:
            print("you put up a good fight with your weapons...")
            time.sleep(2)
            print("But you get shot and die")
            time.sleep(4)
            print()
            print ('Would you like to play again? 1 for yes, 2 for no')
            choice = input()
            choice = int(choice)

            if int(choice) ==2:
                exitRoutine()
            else:
                displayIntro()
                railNumber = chosenRail()
                checkRail(railNumber)
                Level2 ()
                chosen2 ()
                checkChoice2()          
                levelThree()
                blackJack()
                levelFour()
                levelFour2()
        elif strength ==3:
            print("you put up a good fight with your weapons...")
            time.sleep(2)
            print("You just manage to fight off the cops and escape, but loose $10000 while running")
            money2 = money2 - 10000
            print('CASH  $' + str(money2))      
            time.sleep(2)
        elif strength ==4:
            print("you put up a great fight with your weapons...")
            print("You just manage to fight off the cops and escape!")
        elif strength ==5:
            print("your weapons are so cool the cops refuse to fight you...")
            time.sleep(2)
            print("each cop give you all the money in their to stop you from fighting them")
            money2 = money2 + 20000
            print('CASH  $' + str(money2))      
            time.sleep(2)
            print("The cops let you walk out of the bank without a fight")
            
    print("Everyone makes it back to your house saftely and you begin to split up the money")
    if BAD == 1:
    
        print("Dan is walking around the house and notices there is $200 missing from his pocket.")
        time.sleep(3)
        print("He stops and thinks for a minute and then realizes what happened, he slowly starts")
        time.sleep(3)
        print("walking towards you! He starts yelling, YOU STOLE $200 FROM ME WHEN I WAS KNOCKED")
        time.sleep(3)
        print("OUT YESTERDAY!!! Dan pulls out his gun!")
        print(" ")
        print("            ||||||||||||||")
        print("           =              \  ")
        print("           =               |")
        print("          _=            ___/")
        print("         / _\           (o)\ ")
        print("        | | \            _  \ ")
        print("        | |/            (____)")
        print("         \__/          /   |")
        print("          /           /  ___)")
        print("         /    \       \    _)                       )")
        print("        \      \           /                       (")
        print("      \/ \      \_________/   |\_________________,_ )")
        print("       \/ \      /            |     ==== _______)__)")
        print("       \/ \    /           __/___  ====_/")
        print("         \/ \  /           (O____)\\_(_/")
        print("                          (O_ ____)")
        print("                           (O____)")      
        time.sleep(3)
        print("Dan shoots you! and you die")
        time.sleep(4)
        print()
        print ('Would you like to play again? 1 for yes, 2 for no')
        choice = input()
        choice = int(choice)

        if int(choice) ==2:
            exitRoutine()
        else:
            displayIntro()
            railNumber = chosenRail()
            checkRail(railNumber)
            Level2 ()
            chosen2 ()
            checkChoice2()          
            levelThree()
            blackJack()
            levelFour()
            levelFour2()
    else:
        print("you finish spliting up the money and you share is $1000000000!!")
        time.sleep(3)
        print("Everyone takes theri share and leave, they promis to never approach you again")
        time.sleep(3)
        print("You are now are rich!!!! and never work another day in your life!!")
        time.sleep(3)
        print("__   _______ _   _   _    _ _____ _   _ ")
        print("\ \ / /  _  | | | | | |  | |_   _| \ | |")
        print(" \ V /| | | | | | | | |  | | | | |  \| |")
        print("  \ / | | | | | | | | |/\| | | | | . ` |")
        print("  | | \ \_/ / |_| | \  /\  /_| |_| |\  |")
        print("  \_/  \___/ \___/   \/  \/ \___/\_| \_/")
displayIntro()
railNumber = chosenRail()
checkRail(railNumber)
Level2 ()
chosen2 ()
checkChoice2()          
levelThree()
blackJack()
levelFour()
levelFour2()






