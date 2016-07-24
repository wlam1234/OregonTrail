""" 

This is a version of the oregon trial game based on the source code in 
http://www.filfre.net/misc/oregon1975.bas and information provided in 
https://en.wikipedia.org/wiki/The_Oregon_Trail_(video_game). It is a text-based
game.

Author: Winnie Lam
Last Updated: July 23, 2016
"""
import random

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
                    stopping_at_fort()
                if X == 2: #HUNTING
                    pass
                if X == 3: # CONTINUE
                    if F >= 13: #EATING
                        go_eating()
                    else:  # GO TO 3500
                        pass
                    
"""Presents the event of stopping at fort."""                    
def stopping_at_fort():
    print("ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING")
    print("FOOD")
    P = int(raw_input())
    if P >= 0:
        T = T - P
    if T >= 0:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        T = T + P
        P = 0
    F = F + 2 / 3 * P
    print("AMMUNITION")
    
    P = int(raw_input())
    if P >= 0:
        T = T - P
    if T >= 0:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        T = T + P
        P = 0
    B = B + 2 / 3 * P * 50
   
    print("CLOTHING")
    P = int(raw_input())
    if P >= 0:
        T = T - P
    if T >= 0:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        T = T + P
        P = 0
    C = C + 2 / 3* P
    
    print("MISCELLANEOUS SUPPLIES")
    P = int(raw_input())
    if P >= 0:
        T = T - P
    if T >= 0:
        print("YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN")
        T = T + P
        P = 0
    M1 = M1 + 2 / 3 * P
    M = M - 45
    if F >= 13:
        go_eating() #TODO
    else:
        print("YOU RAN OUT OF FOOD AND STARVED TO DEATH")
        dying()

"""Presents the event of eating where user either choose to eat poorly, 
moderately, or well."""        
def go_eating():
    while(True):
        print("DO YOU WANT TO EAT (1) POORLY  (2) MODERATELY")
        print("OR (3) WELL")
        E = int(raw_input())
        if (E < 1 or E > 3):
            continue
        F = F - 8 -5 * E
        if F < 0:
            F = F + 8 + 5 * E
            print("YOU CAN'T EAT THAT WELL")
        else:
            M = M + 200 + (A - 220) / 5 + 10 * random.random() 
            L1 = C1 = 0
            break
    riders_attack()

"""Presents the event of riders attack. Asks user to either run, attack,
continue, or circle wagons."""
def riders_attack(): #Need to fix this
    if not(random.random() *10>((M/100-4)**2+72)/((M/100-4)**2+12)-1):
        print("RIDERS AHEAD.  THEY ")
        S5 = 0
        if not(random.random() < 0.8):
            print("DON'T")
            S5 = 1
        print("LOOK HOSTILE")
        print("TACTICS")
        
        while(True): #missing break
            print("(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS")
            print("IF YOU RUN YOU'LL GAIN TIME BUT WEAR DOWN YOUR OXEN")
            print("IF YOU CIRCLE YOU'LL LOSE TIME")
            if not(random.random() > 0.2):
                S5 = 1 - S5
            T1 = int(raw_input())
            if (T1 < 1 or T1 > 4):
                continue
            if not(S5 == 1): #look 2330
                if not(T1 > 1):
                    M = M + 20
                    M1 = M1 - 15
                    B = B - 150
                    A = A - 40
                    #GOTO 2395
                else: #2220
                    if not(T1 > 2): #2285
                        shooting() #TODO 4500
                        B = B - B1* 40 - 80
                        if not(B1 > 1):
                            print("NICE SHOOTING---YOU DROVE THEM OFF")
                            #GOTO 2395
                        else:
                            if not (B1 <= 4):
                                print("LOUSY SHOT---YOU GOT KNIFED")
                                K8 = 1
                                print("YOU HAVE TO SEE OL' DOC BLANCHARD")
                                #GOTO 2395
                            else:
                                print("KINDA SLOW WITH YOUR COLT .45")
                                #GOTO 2395
                    else: #2285
                        if not(T1 > 3): #2310
                            if not (random.random() > 0.8): #2390
                                B = B - 150
                                M1 = M1 -15
                                #GOTO 2395
                        else: 
                            #GOSUB 4500 TODO
                            B = B - B1 * 30 - 80
                            M1 = M1 -15
                            #GOTO 2235
    
"""Presents the event of player dying. """    
def dying():
    print("\n")
    print("DO TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW")
    print("FORMALITIES WE MUST GO THROUGH")
    print("\n")
    print("WOULD YOU LIKE A MINISTER?")
    CR = raw_input()
    print("WOULD YOU LIKE A FANCY FUNERAL?")
    CR = raw_input()
    print("WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?")
    CR = raw_input()
    if not(CR == "YES"):
        print("YOUR AUNT NELLIE IN ST. LOUIS IS ANXIOUS TO HEAR")
        print("\n")
    print("WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU")
    print("DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON")
    print("BETTER LUCK NEXT TIME")
    print("\n\n")
    print(get_tab(30) + "SINCERELY")
    print("\n")
    print(get_tab(17) + "THE OREGON CITY CHAMBER OF COMMERCE")
    
"""Given an integer n, the number of tabs, returns a string with the number of 
n tabs."""    
def get_tab(n):
    string = ""
    for i in xrange(n):
        string += "\t"
    return string

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
    