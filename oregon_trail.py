""" 

This is a version of the oregon trial game based on the source code in 
http://www.filfre.net/misc/oregon1975.bas and information provided in 
https://en.wikipedia.org/wiki/The_Oregon_Trail_(video_game). It is a text-based
game.

Author: Winnie Lam
Last Updated: July 23, 2016
"""

#global variabbles
A = 0 #amount spent on animals
B = 0 #amount spent on ammunition
B1 = 0 #actual response time for inputing 'BANG'
B2 = 0 #maximum response time for inputing 'BANG'
C = 0 #amount spent on clothing
C1 = 0 #flag for insufficent clothing in cold weather
CR = 0 #yes/No response to questions  (C$) in source code
D1 = 0 #counter in generative events
D3 = 0 #turn number for seeing date
D4 = 0 #current date
E = 0 #choice of eating
F = 0 #amount spend on food
F1 = 0 #flag for clearing south pass
F2 = 0 #flag for clearing blue mountains
F9 = 0 #fraction of 2 weeks traveled on final turn
K8 = 0 # flag for injury
L1 = 0 #flag for blizzard
M = 0 #total mileage whole trip
M1 = 0 #amount spent on miscellaneous supplies
M2 = 0 # total mileage up through previous turn
M9 = 0 #Flag for clearing south pass in setting mileage
P = 0 #Amount spent on items at fort
R1 = 0 #Random numbers in choosing events
S4 = 0 #Flag for illness
S5 = 0 #hostility of riders' factor
T = 0 # cash left over after inital purchases
T1 = 0 # choice of tactices when attacked
X = 0 # choice of action for each turn
X1 = 0 #flag for fort option


"""Prints instructions of the game from a file called 'instructions'. """
def print_instructions():
    instructions_file = open('instructions','r')
    for line in instructions_file:
        print (line)

    instructions_file.close()
    
"""Initialize variables after instructions query is sent."""
def initial_variables():
    X1 = -1
    K8 = S4 = F1 = F2 = M = M9 = D3 = 0
    
"""Asks user for initial purchases and deals with given information 
accordingly. query is a String containing the question, var is the variable 
affected and query_num is an integer indicating which query is being asked."""    
def ask_user(query, var, query_num):
    while(True):
        print(query)
        var = int(raw_input())
        if check_condition(var, query_num):
            break
       
"""Deals with user's input for initial purchases. Returns true is user makes a
sutiable answer, otherwise prints a message and returns false. 
var is the variable affected  and query_num is an integer indicating which 
query is being asked."""   
def check_condition(var, query_num):
    if query_num == 0: #A
        if var >= 200:
            print("NOT ENOUGH")
        elif 200< var <= 300:
            print("TOO MUCH")
        else:
            return True
    elif query_num == 1: #F
        if var < 0:
            print("IMPOSSIBLE")
        else:
            return True  
    elif query_num == 2: #B
        if var < 0:
            print("IMPOSSIBLE")
        else:
            return True 
    elif query_num == 3:#C
        if var < 0:
            print("IMPOSSIBLE")
        else:
            return True 
    elif query_num == 4: #M1
        if var < 0:
            print("IMPOSSIBLE")
        else:  
            return True 
    else: 
        return False
    return False
    
"""Asks user for initial purchases."""
def ask_spendings():
    print ("\n\n")   
    ask_user("HOW MUCH DO YOU WANT TO SPEND ON YOUR TEAM", A, 0)
    ask_user("HOW MUCH DO YOU WANT TO SPEND ON YOUR FOOD", F, 1)
    ask_user("HOW MUCH DO YOU WANT TO SPEND ON YOUR AMMUNITION", B, 2)
    ask_user("HOW MUCH DO YOU WANT TO SPEND ON YOUR CLOTHING", C, 3)
    ask_user("HOW MUCH DO YOU WANT TO SPEND ON YOUR MISCELANEOUS SUPPLIES", \
             M1, 4)
    
def start_turn():
    #TODO
    if F < 0:
        F = 0
    if B < 0:
        B = 0
    if C < 0:
        C = 0
    if M1 < 0:
        M1 = 0
    if F < 12:
        print("YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!")
    
    #Ignored lines 1055 to 1080 as I am not sure what INT does
    M2 = M
    if not(S4 == 1) or not(K8 == 1):
        T = T - 20
        if T >= 0:  #look at 3520 later
            print ("DOCTOR'S BILL IS $20")
            K8 = S4 = 0
            if not (M9 == 1):
                print ("TOTAL MILEAGE IS "+ str(M))
            else:
                print ("TOTAL MILEAGE IS 950")
                M9 = 0
            
            print("FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH")
            print(str(F) + " " + str(B) + " " + str(C) + " "+ str(M1) + " " \
                  + str(T))
            
            if not(X1 == -1): #look at 1350 later
                X1 = X1 * -1
                print("DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT," + \
                      "OR (3) CONTINUE")
                X = int(raw_input())
                if X > 2 or X < 1:
                    X = 3
                if X == 1: #STOOPING AT FORT
                    pass
                if X == 2: #HUNTING
                    pass
                if X == 3: # CONTINUE
                    if F >= 13: #EATING
                        pass
                    else:  # GO TO 3500
                        pass
                    
                    
if __name__ == "__main__" :
    print ("DO YOU NEED INSTRUCTIONS(YES/NO)?")
    user_input = raw_input()
    if user_input == "NO":
        initial_variables()
    else: 
        print_instructions()
        initial_variables()
        
    while(True):    
        ask_spendings()
        T = 700 - A - F - B - C - M1
        if T < 0:
            print("YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.BUY AGAIN")
        else:
            break
    
    B = 50 * B
    print("AFTER ALL YOUR PURCHASES, YOU NOW HAVE " + str(T) + " DOLLARS LEFT")
    print ("\nMONDAY MARCH 29 1847\n")
    