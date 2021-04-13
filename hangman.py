import sys
word_List = ["access", "hactivist" , "framework", "hacker", "cryptography", "farmer", "fundamental", "government", "helicopter", "identification", "intellectual", "journalist", "legislation", "management", "network", "parking", "radio", "scenario", "telescope", "universal" , "vehicle", "warning", "youth", "zone"]

STAGES = [
'''
   x----x
   |    O
   |   /|\\
   |   / \\
  ===
''','''
   x----x
   |    O
   |   /|\\
   |   /
  ===
''','''
   x----x
   |    O
   |   /|\\
   |
  ===
''','''
   x----x
   |    O
   |   /|
   |
  ===
''', '''
   x----x
   |    O
   |    |
   |
  ===
''', '''
   x----x
   |    O
   |
   |
  ===
''', '''
   x----x
   |
   |
   |
  ===
''']

field_array = []#Here the array to print the word's spaces

word_playing = []#Here we take the word chose and add in this array

word_wrong = []#here we take the wronged letters guessed

Game_Over = False#Variable to stop or continue the game loop
errors = 6

#Function to check for winner variable and stop the game if change in true
def Winner_check():
    global Game_Over
    splitted = []
    for x, y in enumerate (word_playing):
        for q, w in enumerate (y):
            splitted.append (w + " ")
    if field_array == splitted:
        Game_Over = True
    elif errors == 0:
        Game_Over = True
    else:
        Game_Over = False

#Function to print the word if not guessed at the end
def Secret_word ():
    for x, y in enumerate (word_playing):
        print (y)

def draw_Field (array):
    for x, y in enumerate (array):
        for q, w in enumerate (y):
            print (w, end= "")

#Here we modify the field based on guessing enters
def add_field (field):
        for x, elem in enumerate (word_playing):
            for y, char in enumerate (elem):
                  if char in letters:
                        for q, w in enumerate (field):
                            if "_ " in field [q]:
                                field[y] = w.replace ("_ ", char + " ")

def word_chosen (start):
    for num, word in enumerate (word_List):
        if num == start:
            word_playing.append (word)

#Check to see if the character is in the word or not and if it's not we add in wrong array and decrease errors number by 1
def checkGuess (letters):
    global errors
    for x, y in enumerate (word_playing):
        for z, c in enumerate (y):
            if letters == c:
                print ("Good guess!!")
                break
        else:
            if letters not in word_wrong:
                errors -= 1
                word_wrong.append (letters)
                print ("Sorry,", letters, " not in the word.")


def words_playedShow (letters):
    if len(word_wrong) != 0:
        print ("That's characters had been chosen:")
        print (word_wrong)


print ("Let's play to Hangman!")
print ("To exit the game digit 'ctrl+c' command.")

#We show a list of word and corrisponding numbers to choosing
for num, word in enumerate (word_List):
    print (num, word)

while (True):
    try:
        start = int(input ("\nPlayer 1 \nplease insert the number corrisponding the word you want: "))
        if start < 0 or start >= len(word_List):
            print ("Please only number thrue 0 and ", len(word_List) - 1)
            continue
        else:
            break

    except KeyboardInterrupt:#To not disclusure some information about errors and code we want to manage interrupt error as well.
        print ("Program interrupted")
        sys.exit(0)

    except:
        print ("Sorry, choose only with numbers printed in screen.")


word_chosen(start)
for x, y in enumerate (word_playing):
    for q, w in enumerate (y):
        field_array.append ("_ ")


print(chr(27) + "[2J")
print ("Player 2 it's your turn!", "\n")

while (Game_Over == False):
    try:
        if len (word_wrong) != 0:#We want to print characters wrong only we have.
            print ("\n", "The wrong characters until now are:\n", word_wrong)

        print (STAGES[errors])#Here we show the hangman based on number in errors variable
        draw_Field (field_array)
        print ("\n")

        letters = input ("Please insert your guessing letter: ")
        if len(letters) > 1:#We want to limit the number of digits only to one character per time.
            print ("Sorry only one digit a time. Try again.")
            continue
        else:
            if letters.isalpha() == True:#We don't trust on user input. We want to handle if the user use int, float, symbols or space.
                checkGuess (letters)    #but we leave the choice to interrupt the program with ctrl + c.
                add_field (field_array)
                Winner_check ()
            else:
                print ("Sorry, only alphabetic characters. Try again.")

    except EOFError:#Want to exit only with ctrl+c command!
        print ("Sorry, 'ctrl+d' command not accepted. To exit the game digit 'ctrl+c' command.")

    except KeyboardInterrupt:
        print ("Program interrupted")
        sys.exit(0)

#Result of end of game. If player win or lose
if errors == 0:
    print ("\n", STAGES[errors])
    print ("\n", "GAME OVER \n Sorry you lose.", "\n")
    print ("The secret word was: ", end="")
    Secret_word ()
else:
    print ("Congratulation you win!!!!")
