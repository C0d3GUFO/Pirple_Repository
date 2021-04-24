from random import shuffle
from time import sleep
from sys import exit

WELCOME = """
_______________________WELCOME TO BRISCOLA_________________________

This is a game for 2 players only.

Every time you want, you can exit game by digit 'ctrl+c' command.

There’s a guide of the game available after put in the name of the players.
To call guide section type ‘—help’
________________________________________________________________________

So let’s start with your name and have FUN!!!


"""

RULES_GAME = """
To quit this guide and resume game type ‘—resume’

THE GAME:

Briscola is a popular Italian card game. Usually is played by elders in bar to have some funny time in company.
This version is only for 2 players.
There are different version of this game with more players, but it must to take out some cards based on the number of players.
With 5 players is another version of this game called Briscolone or Briscola chiamata (Called Briscola).

THE DECK:
 Since Briscola is an Italian game we’ll use Italian cards which are different by the most common Poker cards.
The deck include 40 cards by 4 seeds. Every seed include cards’ number between 1 to 7.
Number 8 is represented by a ‘Fante’ which is a ‘regular soldier’.
Number 9 is represented by a ‘Cavaliere’ which is a ‘knight’.
Number 10 is represented by a ‘Re’ which is a ‘King’.

SEEDS:

In the game you’ll see four seeds in Italian language.

- ‘Ori’ which are ‘coins’
- ‘Spade’ which are ‘swords’
- ‘Coppe’ which are ‘cups’
- ‘Bastoni’ which are ‘sticks’

Here in the game we refer only a number 10 with ‘K’, the other cards you’ll se are represented with numbers.
After numbers of the card you can see the seed of that card, so your hand can be like this: [“1ori”, “Kcoppe”, “5spade”]

VALUE OF THE CARDS:

There are not many cards that give you points in this game:

1 = 11 points
3 = 10 points
8 = 2 points
9 = 3 points
K = 4 points
All the other cards has value of ZERO. (The number of the card can help only to determine who is the round winner, which is covered after here)

RULES:

Basic game process:
Players start with respectively 3 cards in their hands.
On the field we have a deck pile and an uncovered card which determine the Briscola.
In every round the two player choose one card from there own hand and put on the field, when 2 cards are on the field the player that win that round take the 2 cards and put in his personal pile which is the cards’ captured pile, covered.
The captured pile can’t see by the opposite player nor by the owner itself.
And the player that captured cards draw a cards from the deck pile, after him, the opposite player draw his card again from the deck pile.
The rounds continue like that until the cards in the deck pile are over, the last player that has to draw a card, will draw the uncovered card on the field.
At that point remain only 3 rounds to play and the game is over when all player has not cards in their hands and can’t draw card because the deck pile is over.

Start:
The game start with players draw respectively 3 cards from the deck pile. After that the top card on the deck pile is put uncovered on the field.
That card, we can call Briscola card, determine the seed of the Briscola during all game and that card is the last card that a player can draw.

Rounds:
We refer to a round that portion of the game when the player that have to start or that has captured cards in the round before, choose one card from the hand and put on the field.
At that point the opposite player can choose a card from his hand and put on the field.
Based on calculation that you can see in the ‘Round case scenarios’ sub-section below, one player take the 2 played cards and draw first a card by the deck pile, so the opposite player draw a card from the deck pile immediately after.

What is the Briscola:
The Briscola is the most powerful seed during the game. The Briscola can win on all other seeds easily. Only with another Briscola have to fight against.
Logically the card 1 of Briscola seed is the most powerful card in that game. The card 3 is the second, K is the third and so on…
                                     And for the card with value 0 point?
They fight each other based on the card number.
So, for instance, the card 2 basically is the less power, after that we find 4, 5 and so on. You can see the cards’ value in “VALUE OF CARDS” section above.
                                     And if no one player played Briscola?
That is the most interesting scenario.
The first player of that round, if play a card that is not a Briscola, that card determine another Briscola, that is less powerful than Game Briscola, but can rule that round until a Game Briscola come over.

Round case scenarios:
Base on what is write above we can call:

Game Briscola = Most powerful Briscola determined by the uncovered card on the field by start of the game.
One Time Briscola = Less powerful Briscola determined at the start of the round until
                                   Game Briscola come over.

In every round of the game we can see 5 scenarios:

1. Game Briscola - Game Briscola: In this case we check the value of the cards and win the card that has grater value. If the value of the cards is 0 we check for the grater number of the card.
2. Game Briscola - Other seeds: Basically the Game Briscola win on over other seeds.
3. One Time Briscola - One Time Briscola: Here is the same case of the first scenario, but with the One Time Briscola. So first check for the grater value, if there’s not, check for the greater number.
4. One Time Briscola - Game Briscola: We told that Game Briscola is the most powerful Briscola in all the game so Game Briscola win over One Time Briscola.
5. One Time Briscola - Other seeds but Game Briscola: This is the same case of the second scenario. If there’s no Game Briscola on the field and the second card played is not the seed of the One Time Briscola, that Briscola win.

WINNER:

After there’s no cards in the deck’s pile and the players’ hands are empty, the game is over.
The player that has the greater points from the cards captured pile WIN!
You can see the cards’ value in “VALUE OF CARDS” section above.

To quit this guide and resume game type ‘—resume’
"""

def player_win (x, y):
    print ("THE GAME IS OVER!!")
    if x > y:
        print ("Congratulation", player1.name, "!!!! You win with", player1.score, "points.")
    else:
        print ("Congratulation", player2.name, "!!!! You win with", player2.score, "points.")

def guide_display():
    print(chr(27) + "[2J")
    print (RULES_GAME)
    while input() != "--resume":
        print ("Type '--resume' to exit and resume the game.")
    print(chr(27) + "[2J")

def deck_make():
    deck = []
    seed = ["ori", "spade", "bastoni", "coppe"]
    for cards in seed: #seeds
        for x in range (1, 10): #numbers
            deck.append (str(x)+ cards)#adding seed and number in list together
    for cards in seed:
        deck.append ("K" + cards)
    shuffle (deck)
    return deck

class Player:
    def __init__ (self, hand = [], name = []):
        self.hand = hand
        self.name = name
        self.score = 0
        self.cardsCached = []

    def calc_score (self): #Function to calculate score at the end of the game
        global score
        for card in self.cardsCached:
            if card[0] in scoreCards:
                self.score += scoreCards[card[0]]
        return (self.score)

    def playingCard (self,action):
        try:
            cardPlayed = self.hand [int (action) -1]
            return cardPlayed
        except:
            pass

    def drawCard (self):#Function to draw card every play rounds
        try:
            self.hand.append(deckCards.pop())
        except IndexError:
            try:
                self.hand.append(Head_Briscola.pop())#At the end of the deck pile, player have to draw the Head Briscola
            except:
                pass

    def __str__ (self):
        Hand = " "
        for cards in self.hand:
            Hand += str(cards) + " "
        return Hand

def Field ():
    headBriscola = Briscola
    try:
        print ("The Briscola is: " + headBriscola [0][1:])
        print ("The last card is: " + "..:: " + headBriscola [0] + " ::.." +"\n")
    except:
        pass
    if player == 1:
        print (player1.name, "it's your turn.", "\n")
    else:
        print (player2.name, "it's your turn.", "\n")
    if len(playerMove) > 0:
        print ("Card on the field:", playerMove)

def roundCheck():
    global player
    valueCards = {"1" : 11, "2" : 0, "3" : 10,  "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 2, "9" : 3, "K" : 4}
    numCards = {"2" : 2,  "4" : 4, "5" : 5, "6" : 6, "7" : 7}
    oneTimeBriscola = []
    oneTimeBriscola.append (str(playerMove[0][1:]))
    if len (playerMove) < 2:#If there is only 1 card on the field
        if player == 1:#The opposite player have to play his card
            player = 2
        else:
            player = 1
    elif len(playerMove) == 2:#If there are 2 cards on the field, we have to check who win and take cards.
        if playerMove[0][1:] in Briscola[0][1:]:#Player1 has Head Briscola, we have to check for the second player.
            if playerMove[1][1:] in Briscola[0][1:]:#Player 2 has Head Briscola too; we have to check the vale of cards, if both are value 0 we check for greater number.
                if valueCards[playerMove[0][0]] > valueCards[playerMove[1][0]]:
                    if player == 1:#Value first card > of second. Which means the opposite player take the cards.
                        player = 2
                        print (player2.name, "has grater Briscola, takes all cards.")
                        player2.cardsCached.append(playerMove[0])
                        player2.cardsCached.append(playerMove[1])
                        player2.drawCard()
                        player1.drawCard()
                    else:
                        player = 1
                        print (player1.name, "has grater Briscola, takes all cards.")
                        player1.cardsCached.append(playerMove[0])
                        player1.cardsCached.append(playerMove[1])
                        player1.drawCard()
                        player2.drawCard()
                    playerMove.pop()
                    playerMove.pop()

                elif valueCards[playerMove[0][0]] < valueCards[playerMove[1][0]]:#Value first card < the second. Which means that the current player take all cards.
                    if player == 1:
                        print (player1.name, "has grater Briscola, takes all cards.")
                        player1.cardsCached.append(playerMove[0])
                        player1.cardsCached.append(playerMove[1])
                        player1.drawCard()
                        player2.drawCard()
                    else:
                        print (player2_name, "has grater Briscola, takes all cards.")
                        player2.cardsCached.append(playerMove[0])
                        player2.cardsCached.append(playerMove[1])
                        player2.drawCard()
                        player1.drawCard()
                    playerMove.pop()
                    playerMove.pop()
                else: #Value first card == the second. We have to check for the number of cards.
                    if numCards[playerMove[0][0]] > numCards[playerMove[1][0]]:
                        if player == 1:#Number first card > the second. Which means the opposite player take the cards.
                            player = 2
                            print (player2.name, "has grater Briscola, takes all cards.")
                            player2.cardsCached.append(playerMove[0])
                            player2.cardsCached.append(playerMove[1])
                            player2.drawCard()
                            player1.drawCard()
                        else:
                            player = 1
                            print (player1.name, "has grater Briscola, takes all cards.")
                            player1.cardsCached.append(playerMove[0])
                            player1.cardsCached.append(playerMove[1])
                            player1.drawCard()
                            player2.drawCard()
                        playerMove.pop()
                        playerMove.pop()
                    else:#Number first card < the second. Which means that the current player take all cards.
                        if player == 1:
                            print (player1.name, "has grater Briscola, takes all cards.")
                            player1.cardsCached.append(playerMove[0])
                            player1.cardsCached.append(playerMove[1])
                            player1.drawCard()
                            player2.drawCard()
                        else:
                            print (player2.name, "has grater Briscola, takes all cards.")
                            player2.cardsCached.append(playerMove[0])
                            player2.cardsCached.append(playerMove[1])
                            player2.drawCard()
                            player1.drawCard()
                        playerMove.pop()
                        playerMove.pop()

            else:#Player2 hasn't Head Briscola. Than the opposite player take all.
                if player == 1:
                    player = 2
                    print (player2.name, "has Briscola, takes all cards.")
                    player2.cardsCached.append(playerMove[0])
                    player2.cardsCached.append(playerMove[1])
                    player2.drawCard()
                    player1.drawCard()
                else:
                    player = 1
                    print (player1.name, "has Briscola, takes all cards.")
                    player1.cardsCached.append(playerMove[0])
                    player1.cardsCached.append(playerMove[1])
                    player1.drawCard()
                    player2.drawCard()
                playerMove.pop()
                playerMove.pop()

        else:#All scenario that player1 hasn't Head Briscola.
            if playerMove[1][1:] in Briscola[0][1:]:#The player2 has Head Briscola. So he take all. No player switch.
                if player == 1:
                    print (player1.name, "has Briscola, takes all cards.")
                    player1.cardsCached.append(playerMove[0])
                    player1.cardsCached.append(playerMove[1])
                    player1.drawCard()
                    player2.drawCard()
                else:
                    print (player2.name, "has Briscola, takes all cards.")
                    player2.cardsCached.append(playerMove[0])
                    player2.cardsCached.append(playerMove[1])
                    player2.drawCard()
                    player1.drawCard()
                playerMove.pop()
                playerMove.pop()

            elif playerMove[1][1:] in oneTimeBriscola[0]:#The player2 has One Round Briscola
                if valueCards[playerMove[0][0]] > valueCards[playerMove[1][0]]:
                    if player == 1:#Value first card > the second. Which means the opposite player take the cards.
                        player = 2
                        print ("The card played by", player2.name, "is greater,", player2.name, "takes all cards.")
                        player2.cardsCached.append(playerMove[0])
                        player2.cardsCached.append(playerMove[1])
                        player2.drawCard()
                        player1.drawCard()
                    else:
                        player = 1
                        print ("The card played by", player1.name, "is greater,", player1.name, "takes all cards.")
                        player1.cardsCached.append(playerMove[0])
                        player1.cardsCached.append(playerMove[1])
                        player1.drawCard()
                        player2.drawCard()
                    playerMove.pop()
                    playerMove.pop()
                elif valueCards[playerMove[0][0]] < valueCards[playerMove[1][0]]:#Value first card < the second. Which means that the current player take all cards.
                    if player == 1:
                        print ("The card played by", player1.name, "is greater,", player1.name, "takes all cards.")
                        player1.cardsCached.append(playerMove[0])
                        player1.cardsCached.append(playerMove[1])
                        player1.drawCard()
                        player2.drawCard()
                    else:
                        print ("The card played by", player2.name, "is greater,", player2.name, "takes all cards.")
                        player2.cardsCached.append(playerMove[0])
                        player2.cardsCached.append(playerMove[1])
                        player2.drawCard()
                        player1.drawCard()
                    playerMove.pop()
                    playerMove.pop()
                else: #Value first card == the second. We have to check for the number of cards.
                    if numCards[playerMove[0][0]] > numCards[playerMove[1][0]]:
                        if player == 1:#Number first card > the second. Which means the opposite player take the cards.
                            player = 2
                            print ("The card played by", player2.name, "is greater,", player2.name, "takes all cards.")
                            player2.cardsCached.append(playerMove[0])
                            player2.cardsCached.append(playerMove[1])
                            player2.drawCard()
                            player1.drawCard()
                        else:
                            player = 1
                            print ("The card played by", player1.name, "is greater,", player1.name, "takes all cards.")
                            player1.cardsCached.append(playerMove[0])
                            player1.cardsCached.append(playerMove[1])
                            player1.drawCard()
                            player2.drawCard()
                        playerMove.pop()
                        playerMove.pop()
                    else:#Number first card < the second. Which means that the current player take all cards.
                        if player == 1:
                            print ("The card played by", player1.name, "is greater,", player1.name, "takes all cards.")
                            player1.cardsCached.append(playerMove[0])
                            player1.cardsCached.append(playerMove[1])
                            player1.drawCard()
                            player2.drawCard()
                        else:
                            print ("The card played by", player2.name, "is greater,", player2.name, "takes all cards.")
                            player2.cardsCached.append(playerMove[0])
                            player2.cardsCached.append(playerMove[1])
                            player2.drawCard()
                            player1.drawCard()
                        playerMove.pop()
                        playerMove.pop()

            else:#The player 2 hasn't Head Briscola or One Round Briscola. The opposite player takes all cards.
                if player == 1:
                    player = 2
                    print (player2.name, "takes all cards.")
                    player2.cardsCached.append(playerMove[0])
                    player2.cardsCached.append(playerMove[1])
                    player2.drawCard()
                    player1.drawCard()
                else:
                    player = 1
                    print (player1.name, "takes all cards.")
                    player1.cardsCached.append(playerMove[0])
                    player1.cardsCached.append(playerMove[1])
                    player1.drawCard()
                    player2.drawCard()
                playerMove.pop()
                playerMove.pop()

scoreCards = {"1" : 11,  "3" : 10,   "8" : 2, "9" : 3, "K" : 4}
playerMove = []
player = 1
rounds = 0
deckCards = deck_make()

print (WELCOME)

while (True):
    try:
        player1_name = input (str("Player 1, please insert your name: "))
        if player1_name.isalpha() == True:
            firstHand = [deckCards.pop(), deckCards.pop(), deckCards.pop()]
            player1 = Player (firstHand, player1_name)
            break
        else:
            print ("Please use only alphabetic letters for your name.")
    except EOFError:#Want to exit only with ctrl+c command!
        print ("Sorry, 'ctrl+d' command not accepted. To exit the game digit 'ctrl+c' command.")

    except KeyboardInterrupt:
        print ("Program interrupted")
        exit(0)
while (True):
    try:
        player2_name = input (str("Player 2, please insert your name: "))
        if player2_name.isalpha() == True:
            secondHand = [deckCards.pop(), deckCards.pop(), deckCards.pop()]
            player2 = Player (secondHand, player2_name)
            break
        else:
            print ("Please use only alphabetic letters for your name.")
    except EOFError:#Want to exit only with ctrl+c command!
        print ("Sorry, 'ctrl+d' command not accepted. To exit the game digit 'ctrl+c' command.")

    except KeyboardInterrupt:
        print ("Program interrupted")
        exit(0)

Briscola = [deckCards.pop()]
Head_Briscola = []
Head_Briscola.append(Briscola[0])
print(chr(27) + "[2J")

while (rounds < 40):
    if player == 1:
        try:
            while (True):
                Field ()
                print (player1)
                action = input ("Which card do you want to play? Type 1, 2 or 3: ")
                if action.isdigit() == True:
                    if int(action) > len(player1.hand) or int(action) < 1:
                        print ("Sorry, you can choose only thrue cards in your hand.")
                        continue
                    else:
                        break
                elif action == "--help":
                    guide_display()
                    continue
            game = player1.playingCard(action)
            playerMove.append(game)
            player1.hand.remove (game)
            roundCheck()
            sleep (2)
            print(chr(27) + "[2J")
        except EOFError:#Want to exit only with ctrl+c command!
            print ("Sorry, 'ctrl+d' command not accepted. To exit the game digit 'ctrl+c' command.")

        except KeyboardInterrupt:
            print ("Program interrupted")
            exit(0)
    else:
        try:
            while (True):
                Field ()
                print (player2)
                action = input ("Which card do you want to play? Type 1, 2 or 3: ")
                if action.isdigit() == True:
                    if int(action) > len(player2.hand) or int(action) < 1:
                        print ("Sorry, you can choose only thrue cards in your hand.")
                        continue
                    else:
                        break
                elif action == "--help":
                    guide_display()
                    continue
            game = player2.playingCard(action)
            playerMove.append(game)
            player2.hand.remove (game)
            roundCheck()
            sleep (2)
            print(chr(27) + "[2J")
        except EOFError:#Want to exit only with ctrl+c command!
            print ("Sorry, 'ctrl+d' command not accepted. To exit the game digit 'ctrl+c' command.")
        except KeyboardInterrupt:
            print ("Program interrupted")
            exit(0)
    rounds += 1
player1.calc_score()
player2.calc_score()
player_win (player1.score, player2.score)
