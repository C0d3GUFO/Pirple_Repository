#Function to draw the field
def connectField (field):
    for row in range (11):
        if row%2 == 0:
            trueRow = int(row / 2)
            for column in range (13):
                if column%2 == 0:
                    trueCol = int(column / 2)
                    if column != 12:
                        print (field [trueCol] [trueRow], end = "")
                    else:
                        print (field [trueCol] [trueRow])
                else:
                    print ("|", end ="")
        else:
            print ("-------------")
# Function to check if in the filed there is X move and than add in the X array
def check_ColumnX ():
    for i, x in enumerate (theField):
        for g, y in enumerate (x):
            if y == "X":
                if i == 0:
                    if g not in col_0:
                        col_0.append(g)
                elif i == 1:
                    if g not in col_1:
                        col_1.append(g)
                elif i == 2:
                    if g not in col_2:
                        col_2.append(g)
                elif i == 3:
                    if g not in col_3:
                        col_3.append(g)
                elif i == 4:
                    if g not in col_4:
                        col_4.append(g)
                elif i == 5:
                    if g not in col_5:
                        col_5.append(g)
                elif i == 6:
                    if g not in col_6:
                        col_6.append(g)

# Function to check if in the filed there is O move and than add in the X array
def check_ColumnO ():
    for i, x in enumerate (theField):
        for g, y in enumerate (x):
            if y == "O":
                if i == 0:
                    if g not in col_0Y:
                        col_0Y.append(g)
                elif i == 1:
                    if g not in col_1Y:
                        col_1Y.append(g)
                elif i == 2:
                    if g not in col_2Y:
                        col_2Y.append(g)
                elif i == 3:
                    if g not in col_3Y:
                        col_3Y.append(g)
                elif i == 4:
                    if g not in col_4Y:
                        col_4Y.append(g)
                elif i == 5:
                    if g not in col_5Y:
                        col_5Y.append(g)
                elif i == 6:
                    if g not in col_6Y:
                        col_6Y.append(g)

#Function for check vertical wins
def check (x):
    global winner  #Access to the global variable instead a local one.
    range_listA = list (range(min(x), min(x)+4))
    range_listB = list (range(min(x)+2, min(x)+6))
    checkA = set (x) & set (range_listA)
    checkB = set (x) & set (range_listB)
    list_tempA = []
    list_tempB = []
    for y in checkA:
        list_tempA.append (y)
    for y in checkB:
        list_tempB.append (y)
    if list_tempA == range_listA:
        winner = True #Change the global variable to stop the while loop
    elif list_tempB == range_listB:
        winner = True

#Function for check orizzontal X wins
def check_Orizz ():
    global winner
    for x in range (7):
        if x in col_0 and x in col_1 and x in col_2 and x in col_3:
            winner = True
        elif x in col_1 and x in col_2 and x in col_3 and x in col_4:
            winner = True
        elif x in col_2 and x in col_3 and x in col_4 and x in col_5:
            winner = True
        elif x in col_3 and x in col_4 and x in col_5 and x in col_6:
            winner = True

#Function for check orizzontal O wins
def check_OrizzO ():
    global winner
    for x in range (7):
        if x in col_0Y and x in col_1Y and x in col_2Y and x in col_3Y:
            winner = True
        elif x in col_1Y and x in col_2Y and x in col_3Y and x in col_4Y:
            winner = True
        elif x in col_2Y and x in col_3Y and x in col_4Y and x in col_5Y:
            winner = True
        elif x in col_3Y and x in col_4Y and x in col_5Y and x in col_6Y:
            winner = True

#2 Functions for distrubute check vertical wins for both X and O
def moveNum (y):
    if y == 1:
        check(col_0)
    elif y == 2:
        check(col_1)
    elif y == 3:
        check(col_2)
    elif y == 4:
        check(col_3)
    elif y == 5:
        check(col_4)
    elif y == 6:
        check(col_5)
    elif y == 7:
        check(col_6)

def moveNumO (y):
    if y == 1:
        check(col_0Y)
    elif y == 2:
        check(col_1Y)
    elif y == 3:
        check(col_2Y)
    elif y == 4:
        check(col_3Y)
    elif y == 5:
        check(col_4Y)
    elif y == 6:
        check(col_5Y)
    elif y == 7:
        check(col_6Y)

#And than check straight for diagonals both X and O
def check_DiagStraightX ():
    global winner
    if 5 in col_0:
        if 4 in col_1 and 3 in col_2 and 2 in col_3:
            winner = True
    elif 4 in col_0:
        if 3 in col_1 and 2 in col_2 and 1 in col_3:
            winner = True
    elif 3 in col_0:
        if 2 in col_1 and 1 in col_2 and 0 in col_3:
            winner = True
    elif 5 in col_1:
        if 4 in col_2 and 3 in col_3 and 2 in col_4:
            winner = True
    elif 4 in col_1:
        if 3 in col_2 and 2 in col_3 and 1 in col_4:
            winner = True
    elif 3 in col_1:
        if 2 in col_2 and 1 in col_3 and 0 in col_4:
            winner = True
    elif 5 in col_2:
        if 4 in col_3 and 3 in col_4 and 2 in col_5:
            winner = True
    elif 4 in col_2:
        if 3 in col_3 and 2 in col_4 and 1 in col_5:
            winner = True
    elif 3 in col_2:
        if 2 in col_3 and 1 in col_4 and 0 in col_5:
            winner = True
    elif 5 in col_3:
        if 4 in col_4 and 3 in col_5 and 2 in col_6:
            winner = True
    elif 4 in col_3:
        if 3 in col_4 and 2 in col_5 and 1 in col_6:
            winner = True
    elif 3 in col_3:
        if 2 in col_4 and 1 in col_5 and 0 in col_6:
            winner = True

def check_DiagReverseX ():
    global winner
    if 5 in col_6:
        if 4 in col_5 and 3 in col_4 and 2 in col_3:
            winner = True
    elif 4 in col_6:
        if 3 in col_5 and 2 in col_4 and 1 in col_3:
            winner = True
    elif 3 in col_6:
        if 2 in col_5 and 1 in col_4 and 0 in col_3:
            winner = True
    elif 5 in col_5:
        if 4 in col_4 and 3 in col_3 and 2 in col_2:
            winner = True
    elif 4 in col_5:
        if 3 in col_4 and 2 in col_3 and 1 in col_2:
            winner = True
    elif 3 in col_5:
        if 2 in col_4 and 1 in col_3 and 0 in col_2:
            winner = True
    elif 5 in col_4:
        if 4 in col_3 and 3 in col_2 and 2 in col_1:
            winner = True
    elif 4 in col_4:
        if 3 in col_3 and 2 in col_2 and 1 in col_1:
            winner = True
    elif 3 in col_4:
        if 2 in col_3 and 1 in col_2 and 0 in col_1:
            winner = True
    elif 5 in col_3:
        if 4 in col_2 and 3 in col_1 and 2 in col_0:
            winner = True
    elif 4 in col_3:
        if 3 in col_2 and 2 in col_1 and 2 in col_0:
            winner = True
    elif 3 in col_3:
        if 2 in col_2 and 1 in col_1 and 0 in col_0:
            winner = True

def check_DiagStraightO ():
    global winner
    if 5 in col_0Y:
        if 4 in col_1Y and 3 in col_2Y and 2 in col_3Y:
            winner = True
    elif 4 in col_0Y:
        if 3 in col_1Y and 2 in col_2Y and 1 in col_3Y:
            winner = True
    elif 3 in col_0Y:
        if 2 in col_1Y and 1 in col_2Y and 0 in col_3Y:
            winner = True
    elif 5 in col_1Y:
        if 4 in col_2Y and 3 in col_3Y and 2 in col_4Y:
            winner = True
    elif 4 in col_1Y:
        if 3 in col_2Y and 2 in col_3Y and 1 in col_4Y:
            winner = True
    elif 3 in col_1Y:
        if 2 in col_2Y and 1 in col_3Y and 0 in col_4Y:
            winner = True
    elif 5 in col_2Y:
        if 4 in col_3Y and 3 in col_4Y and 2 in col_5Y:
            winner = True
    elif 4 in col_2Y:
        if 3 in col_3Y and 2 in col_4Y and 1 in col_5Y:
            winner = True
    elif 3 in col_2Y:
        if 2 in col_3Y and 1 in col_4Y and 0 in col_5Y:
            winner = True
    elif 5 in col_3Y:
        if 4 in col_4Y and 3 in col_5Y and 2 in col_6Y:
            winner = True
    elif 4 in col_3Y:
        if 3 in col_4Y and 2 in col_5Y and 1 in col_6Y:
            winner = True
    elif 3 in col_3Y:
        if 2 in col_4Y and 1 in col_5Y and 0 in col_6Y:
            winner = True

def check_DiagReverseO ():
    global winner
    if 5 in col_6Y:
        if 4 in col_5Y and 3 in col_4Y and 2 in col_3Y:
            winner = True
    elif 4 in col_6Y:
        if 3 in col_5Y and 2 in col_4Y and 1 in col_3Y:
            winner = True
    elif 3 in col_6Y:
        if 2 in col_5Y and 1 in col_4Y and 0 in col_3Y:
            winner = True
    elif 5 in col_5Y:
        if 4 in col_4Y and 3 in col_3Y and 2 in col_2Y:
            winner = True
    elif 4 in col_5Y:
        if 3 in col_4Y and 2 in col_3Y and 1 in col_2Y:
            winner = True
    elif 3 in col_5Y:
        if 2 in col_4Y and 1 in col_3Y and 0 in col_2Y:
            winner = True
    elif 5 in col_4Y:
        if 4 in col_3Y and 3 in col_2Y and 2 in col_1Y:
            winner = True
    elif 4 in col_4Y:
        if 3 in col_3Y and 2 in col_2Y and 1 in col_1Y:
            winner = True
    elif 3 in col_4Y:
        if 2 in col_3Y and 1 in col_2Y and 0 in col_1Y:
            winner = True
    elif 5 in col_3Y:
        if 4 in col_2Y and 3 in col_1Y and 2 in col_0Y:
            winner = True
    elif 4 in col_3Y:
        if 3 in col_2Y and 2 in col_1Y and 1 in col_0Y:
            winner = True
    elif 3 in col_3Y:
        if 2 in col_2Y and 1 in col_1Y and 0 in col_0Y:
            winner = True

player = 1
winner = False
theField = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]

col_0 = []
col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_6 = []
col_0Y = []
col_1Y = []
col_2Y = []
col_3Y = []
col_4Y = []
col_5Y = []
col_6Y = []

connectField (theField)

while (winner == False):
    print ("Player turn: ", player)
    move = int (input ("Choose the column of your move (numebers 1-7): "))
    if move >= 1 and move <= 7:
        if player == 1:
            for i, x in enumerate (theField):
                if i == move - 1:
                    for j, a in reversed (list(enumerate(x))):
                        if " " in a:
                            theField [i] [j] = a.replace (" ", "X")
                            break
            check_ColumnX ()
            moveNum (move)
            check_Orizz ()
            check_DiagStraightX ()
            check_DiagReverseX ()
            if winner == True:
                print ("Congratulation!!!", player, "wins!!!!") #When while loop stopped print the winner
            player = 2

        else:
            for i, x in enumerate (theField):
                if i == move - 1:
                    for j, a in reversed (list (enumerate(x))):
                        if " " in a:
                            theField [i] [j] = a.replace (" ", "O")
                            break
            check_ColumnO ()
            moveNumO (move)
            check_OrizzO ()
            check_DiagStraightO ()
            check_DiagReverseO ()
            if winner == True:
                print ("Congratulation!!!", player, "wins!!!!")
            player = 1

        connectField (theField)
    else:
        print ("Please insert only numbers 1 - 7.")
