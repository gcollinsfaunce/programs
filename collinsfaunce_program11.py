# Black Jack

import time
print(time.asctime(time.localtime(time.time())))
print("")

import random # This part invokes a random access function
from ch10ex11 import Card # This from ch10ex11 import invokes the use of one of
# our programs where we created cards in a deck
from collinsfaunce_ch11ex15 import Deck # This section invokes the deck that we
# created from Chapter 11
class Player(object): # This invokes the use of created class: Player which
    # allows for us to play our hand

    def __init__(self,name,hand=[0,0],value = 0,bal=100,debt=0): # This invokes the usage of self, name, hand and creates the values of the hands
        self.name = name # This invokes the player's name
        self.bal = bal # This invokes the balance of the player's account
        self.hand = hand # This invokes what is in the player's hand
        self.debt = debt # This Invokes what the player owes to the dealer
        self.value = value # This invokes the final tally
        
    def checkBal(self): # This defines the Balance of the player's account
        print (self.name + ", your current balance is: $",self.bal) # This Invokes the ability to print/display the current balance of the player
        
    def placeBet(self,amount): # This defines the setup that allows for the player to place a bet in the amount in which he/she wishes to use
        while True: # This setups up the if and else code for the amount and balance of a player's account
            if (amount > self.bal): # This invokes the amount in the player's current balance
                print ("You don't have enough money!") # This is to display a positive or negative point in the player's balance
                amount = int(input("Try again. Please look at how much money you have :("))# In this section it allows the player to re-enter the amount they wish to play with
                continue # the "continue clausing allows for the player to move forward
            else: break # In this part the player doesn't have enough and loses the game
        while True: # While True invokes the means to continue and opens the parameters of the if/else clause
            if (amount < 0): # This shows that if the balance is less then 0
                print ("You can't place a negative bet!") # This printout will display on the screen if the player doesn't have enough
                amount = input("Try again: ") # Amount = input("Try again:") invokes the player to try and put in a positive amount
                continue # This allows for the player to move forward if the balance is positive
            else: break # this else: break clause means Otherwise the player has lost the game
        self.bal -=amount # This clause shows the negative balance of the player's account balance
        return amount # This returns the Amount in the player's balance
    
class Dealer(object): # this creates a Dealer class to handle the computer player
    
    def __init__(self,hand=[0,0],value=0): # Creates the instance of dealer
        self.hand = hand # Makes his hand
        self.value = value # gives the hand a value
        
    def dealerPlay(self): # Controls the dealers logic
        while valueHand(self.hand) < 17: # Decides if the dealer takes a hit
            hitMe(self.hand) # Cause the dealer to take a hand (abuse was necessary)
            
cardDeck = Deck() # Create the deck
cardDeck.shuffle() # Shuffle the deck

def dealHand(): # Deal one hand at a time (Sorry it is not back and forth)
    return [cardDeck.dealCard(), cardDeck.dealCard()] # two cards to one player

def valueHand(hand): # Set the hand value
    crdSum = 0 # Default value set to zero

    for card in hand: # Number of cards in the hand
        crdSum += card.value() # 
    return crdSum
    
def hitMe(hand):
    hand.append(cardDeck.dealCard())
    
#################################################
def main():
    print ("Welcome to My Casino!")
    name = input("Please enter your name: ")

    player = Player(name, dealHand())
    win = 0 # Keep track of the wins
    loose = 0 # Keep track of loses or as professor said looses

    while True:
        
        player.hand = dealHand()
        player.value = valueHand(player.hand)
        
        house = Dealer(dealHand())
        house.value = valueHand(house.hand)
        
        print ("")
        player.checkBal()

        while True:
            try: z = float(input("Please place your bet: "))
            except: z = (input("Invalid bet! Try again: "))
            else: break 

        betAmount = player.placeBet(z)

        print ("")
        print ("Blackjack will now begin.")
        print ("")

        print ("Your hand is: ",end="")
        for num in range(0,len(player.hand)):
            print (player.hand[num],end="  ")

        print ("")
        print ("The dealer's hand is showing: ", house.hand[0])
        
        ddchoice = input("Would you like to take a hit and double down ending your turn? y/n: ")
        print("")
        if ddchoice.lower() == "y":
            player.bal -= betAmount
            betAmount *= 2
            hitMe(player.hand)
            print ("Your hand is now: ",end="")
            for num in range(0,len(player.hand)):
                print (player.hand[num],end="  ")
            print ("")
            player.value = valueHand(player.hand)
        else: 
            while player.value < 21:
                choice = input("Input 'y' for a hit, or 'n' to stand: ")
                if choice.lower() == 'y':
                    hitMe(player.hand)
                    print ("Your hand is now: ",end="")
                    for num in range(0,len(player.hand)):
                        print (player.hand[num],end="  ")
                    print ("")
                    player.value = valueHand(player.hand)
                else: break 

        print ("")
        print ("The dealer reveals his hand: ",end="")
        for num in range(0,len(house.hand)):
                print (house.hand[num],end="  ")
        print ("")

        if house.value < 17:
            house.dealerPlay()
            print ("The dealer deals himself and finishes with: ", end="")
            for num in range(0,len(house.hand)):
                print (house.hand[num],end="  ")
            print ("")

        house.value = valueHand(house.hand)
        player.value = valueHand(player.hand)

        print ("The value of your hand is",player.value)
        print ("The value of the dealer's hand is", house.value)
        print ("")

        if (player.value > house.value and player.value <= 21) or (house.value > 21 and player.value <= 21):
            print ("Thus, you win!")
            print ("$",betAmount, " goes to you.")
            player.bal += (betAmount*2)
            win += 1
            
        else:
            if player.value > 21:
                print ("You've gone bust!")
            print ("Thus, you lose!")
            print ("$",betAmount, " goes to the dealer.")
            loose += 1
            if player.bal <= 0:
                print(player.name, "Won ", str(win), " and Lost ", str(loose))
                print ("You are not too good at this game are you loser?")
                break
                
        print ("")
        playAgain = input("Would you like to play again? y/n: ")
        if playAgain.lower() == "y":
            continue
        elif playAgain.lower() == "n":
            print(player.name, "Won ", str(win), " and Lost ", str(loose))
            break
        else:
            print("You caused an ERROR by not putting in a y/n Thanks for nothin' ")
            continue
        
    print("")
    print("Your final balance is $", player.bal)
    if player.bal > 100:
        print ("This represents a GAIN of $", (player.bal-100))
    elif player.bal == 0: 
        print ("Sucks to be you, loser!")
    elif player.bal < 100:
        print ("This represents a LOSS of $", (100-player.bal))

    if player.debt > 0:
        print("You owe the casino $", player.debt)
        if (player.bal - player.debt) > 100:
            print("Your net winnings are $",(player.bal-100-player.debt))
        elif (player.bal - player.debt) < 100:
            print("Your net loss is $", (100 - (player.bal - player.debt)))
            
    print ("")
    print ("Goodbye!")

main()
