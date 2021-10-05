# CSC 308 Assignment 1
# Rudolph Hanzes, Kristen Hartz, Stacy Hartz

import random
import sys

# Lists the set of choices before each play
def Choices():
    print("\nWould you like to:\n" +
      """1 "Run"\n2 "Pass"\n3 "Kick"\n4 "Status"\n5 "Quit\"""")
    answ = input("\nYour Choice: ")

    if (answ == "1" or answ.lower() == "run"):
        Run()
    elif (answ == "2" or answ.lower() == "pass"):
        Pass()
    elif (answ == "3" or answ.lower() == "kick"):
        Kick()
    elif (answ == "4" or answ.lower() == "status"):
        Status()
    elif (answ == "5" or answ.lower() == "quit"):
        Quit()
    else:
        print("Invalid Choice, Please Try Again")
    input("\nPress Enter to continue...")
    Choices()

# Lists options for conservative run or risky run
def Run():
    print("\nWould you like to:\n" +
          """1 "Conservative Run"\n2 "Risky Run" """)
    answ = input("\nYour Choice: ")

    if (answ == "1" or answ.lower() == "conservative"):
        # Gained yards 0 through 2
        Update(random.randint(0,2))
    elif (answ == "2" or answ.lower() == "risky"):
        # Gained yards -5 through 15
        Update(random.randint(-5,15))
    else:
        print("\nInvalid Choice, Please Try Again")
        Run()

# Lists options for short or long passes
def Pass():
    print("\nWould you like to:\n" +
          """1 "Short Pass"\n2 "Long Pass""")
    answ = input("\nYour Choice: ")

    if (answ == "1" or answ.lower() == "short"):
        # 75% chance for completed short pass
        if (random.randint(0, 3) <= 2):
            print("\nPass Completed")
            # Completed pass results in randome gained yards 4 though 10
            Update(random.randint(4, 10))
        else:
            print("\nPass Incomplete")
            Update(0)
    elif (answ == "2" or answ.lower() == "long"):
        # 33% chance for completed long pass
        if (random.randint(0,2) < 1):
            print("\nPass Completed")
            # Completed pass results in random gained yards 10 through 20
            Update(random.randint(10,20))
        else:
            print("\nPass Incomplete")
            Update(0)
    else:
        print("\nInvalid Choice, Please Try Again")
        Pass()
        
# Function for kicking for field goal
def Kick():
    global home
    # Cant be selected if > 50 yards
    if (tYards < 50):
        # 2 times Yards until touchdown must be < randome number 1-100
        if (tYards * 2 < random.randint(1, 100)):
            print("I'ts Good!")
            home += 3
            OtherSide()
        else:
            print("Field Goal attempt failed")
            OtherSide()
    else:
        print("\nYou must be within 50 yards of the endzone to attempt a kick..")

# Exits the program
def Quit():
    print("Thanks For Playing!")
    sys.exit()

# Provides the current status of the game
def Status():
    print("\nScore:\n" + "You  ->\t" , home , "\nThem ->\t" , away)
    print("\nCurrent Yard Line:\t" , cYards)
    print("Yards Untill Touchdown:\t" , tYards)
    print("Downs: ", down)

# Function which updates the yards gained or lost and how far until touchdown
def Update(yds):
    global cYards
    global tYards
    
    cYards = cYards + yds
    tYards = 100 - cYards
    
    print("\nYards Moved: ", yds);

    Downs(yds)

# Calculated the number of downs and increments when needed
def Downs(yds):
    global ytd
    global down
    
    ytd = ytd + yds

    # Has entered / passed through the endzone
    if (tYards < 0):
        down = 1
        Touchdown()
    # Reached First Down and reset Downs
    elif (ytd >= 10):
        down = 1
        ytd = 0
        print("First Down!")
    # Failed to reach 4th down
    elif (down >= 4):
        print("First Down not achieved")
        down = 1
        OtherSide()
    # Within 10 yards of a touchdown
    elif tYards in range(0, 11):
        down += 1
        print("Yards Until Touchdown: ", tYards)
        print("Downs: ", down)
    # Did not reach 1st down, increment downs
    else:
        down += 1
        print("Yards Until First Down: ", 10 - ytd)
        print("Downs: ", down)
        
# Touchdown function where the home score is updated
def Touchdown():    
    global home

    print("\nTOUCHDOWN!")
    
    home += 7
    OtherSide()

# Function which swaps the sides for the other team,
# updates oponent score and increments turns
def OtherSide():
    global away
    global turns

    # Gives opponent 0, 3, or 7 for a score
    pts = random.choice([0, 3, 7])
    away += int(pts)
    turns += 1
    
    print("\nSwitched Sides!")
    print("The Other Team Scored: ", pts, "pts")
    # If out of turns, game ends, if not, switches back to home turn
    if (turns < 2):
        Reset()
    else:
        Final()
        
# Function which resets after sides switched back to home or game restarted
def Reset():
    global turns
    global cYards
    global tYards
    global ytd
    global away

    turns += 1
    cYards = 20
    tYards = 80
    ytd = 0
    
# Function to display the final score, declare winner/ loser, and offer to play again
def Final():
    global turns
    
    print("\nFinal Score:\n" + "You  ->\t" , home , "\nThem ->\t" , away)
    if (home > away):
        print("\nCongradulations! You Win!")
    else:
        print("\nGood Game, maybe next time")
    print("\nWould you like to play again?:\n" +
          """1 "Yes"\n2 "No""")
    
    replay = input("\nYour Choice: ")
    if (replay == "1" or replay.lower() == "yes"):
        Reset()
        turns = 0
    elif (replay == "2" or replay.lower() == "no"):
        print("Thanks For Playing!")
        sys.exit()
    else:
        print("Invalid Choice, Please Try Again")
        Final()

# Start of Program
# Prints begining message and calls the begining function
print("Welcome to the football game!\n")
print("You get two possesions to try and beat the opposing team")
print("You will begin with the ball at the 20 yard line.")
print("You have 80 yards to go")
print("You have to make at least 10 yards in 4 downs to continue the possession")
print("\nYou have three options for plays:")
print("1 Run Ball, 2 Pass Ball, 3 Field Goal Attempt, 4 Status, 5 Quit\n")
print("In order to kick a fieldgoal, you must be less than 50 yards to the endzone")

home = 0
away = 0
turns = 0
cYards = 20	# Current Yard Line
tYards = 80	# Yarks until Touchdown
down = 1
ytd = 0	# Yards Until Down

Choices()
