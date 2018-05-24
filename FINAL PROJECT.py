#Kiera McMurtrie
#4/20/2018
#Computer Programming

#NOTES
#os.system('cls' if os.name == 'nt' else 'clear')

#IMPORTS
import random
import os

#GLOBALS
ticket_num = random.randrange(1000, 999999)
balance = 768
price = 0
day = ''
day_read = ''
ticket_cost = 0
time = ''
movie = ''
order = 0
ap = ''
seatnums = 0

def main_menu():
    try:
        xx = input('''
__   __                      _                      _  ___  ___               _         _____  _                   _               
\ \ / /                     | |                    | | |  \/  |              (_)       |_   _|| |                 | |              
 \ V /   ___   _   _  _ __  | |  ___    ___   __ _ | | | .  . |  ___  __   __ _   ___    | |  | |__    ___   __ _ | |_   ___  _ __ 
  \ /   / _ \ | | | || '__| | | / _ \  / __| / _` || | | |\/| | / _ \ \ \ / /| | / _ \   | |  | '_ \  / _ \ / _` || __| / _ \| '__|
  | |  | (_) || |_| || |    | || (_) || (__ | (_| || | | |  | || (_) | \ V / | ||  __/   | |  | | | ||  __/| (_| || |_ |  __/| |   
  \_/   \___/  \__,_||_|    |_| \___/  \___| \__,_||_| \_|  |_/ \___/   \_/  |_| \___|   \_/  |_| |_| \___| \__,_| \__| \___||_|
______                   _____      _              _          _                _       
| ___ \                 |  ___|    | |            | |        | |              (_)      
| |_/ _ __ ___ ___ ___  | |__ _ __ | |_ ___ _ __  | |_ ___   | |__   ___  __ _ _ _ __  
|  __| '__/ _ / __/ __| |  __| '_ \| __/ _ | '__| | __/ _ \  | '_ \ / _ \/ _` | | '_ \ 
| |  | | |  __\__ \__ \ | |__| | | | ||  __| |    | || (_) | | |_) |  __| (_| | | | | |
\_|  |_|  \___|___|___/ \____|_| |_|\__\___|_|     \__\___/  |_.__/ \___|\__, |_|_| |_|
                                                                          __/ |        
                                                                         |___/
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        x = int(input('''                                                      
1. Showtimes
2. Refund ticket
3. Quit
'''))
        if x == 1:
            showtimes()
        elif x == 2:
            refund()
        elif x == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            y = input("Are you sure you'd like to quit?(y/n)\n")
            if y == 'y':
                quit()
            elif y == 'n':
                os.system('cls' if os.name == 'nt' else 'clear')
                main_menu()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Please answer (y/n)')
                main_menu()
        else:
            print('Not an option')
            main_menu()
            os.system('cls' if os.name == 'nt' else 'clear')
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Invalid input, please put in a number')
        main_menu()
        
#----------------SHOWTIMES----------------

def showtimes():
    os.system('cls' if os.name == 'nt' else 'clear')
    global day
    global day_read
    class DATES:
        def __init__(self):
            self.m = m
            self.t = t
            self.w = w
            self.th = th
            self.f = f
            self.sat = sat
            self.sun = sun
    m = open('MONDAY.txt', 'r')
    t = open('TUESDAY.txt', 'r')
    w = open('WEDNESDAY.txt', 'r')
    th = open('THURSDAY.txt', 'r')
    f = open('FRIDAY.txt', 'r')
    sat = open('SATURDAY.txt', 'r')
    sun = open('SUNDAY.txt', 'r')
    mm = m.read()
    tt = t.read()
    ww = w.read()
    thth = th.read()
    ff = f.read()
    satsat = sat.read()
    sunsun = sun.read()    

    m.close()
    t.close()
    w.close()
    th.close()
    f.close()
    sat.close()
    sun.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        x = int(input('''DAYS
1. MONDAY
2. TUESDAY
3. WEDNESDAY
4. THURSDAY
5. FRIDAY
6. SATURDAY
7. SUNDAY
8. Main Menu
'''))
        if x == 1:
            print(mm[:300])
            day = 'MONDAY.txt'
            day_read = 'Monday'
            menu2()
        elif x == 2:
            print(tt[:300])
            day = 'TUESDAY.txt'
            day_read = 'Tuesday'
            menu2()
        elif x == 3:
            print(ww[:300])
            day = 'WEDNESDAY.txt'
            day_read = 'Wednesday'
            menu2()
        elif x == 4:
            print(thth[:300])
            day = 'THURSDAY.txt'
            day_read = 'Thursday'
            menu2()
        elif x == 5:
            print(ff[:300])
            day = 'FRIDAY.txt'
            day_read = 'Friday'
            menu2()
        elif x == 6:
            print(satsat[:400])
            day = 'SATURDAY.txt'
            day_read = 'Saturday'
            menu3()
        elif x == 7:
            print(sunsun[:400])
            day = 'SUNDAY.txt'
            day_read = 'Sunday'
            menu3()
        elif x == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()

    except ValueError:
        print('Invalid input, please put in a number')
        os.system('cls' if os.name == 'nt' else 'clear')
        showtimes()
        
#----------------MOVIES----------------

def menu2():
    try:
        x = int(input('''
1. Blue Panther
2. A Loud Area
3. Chicken Blockers
4. Not Ready Player Two
5. I Feel Ugly
6. Menu
'''))
        global seatnums
        global movie
        if x == 1:
            movie = 'Blue Panther'
            seatnums = 14
            ticket_pay1()
        elif x == 2:
            movie = 'A Loud Area'
            seatnums = 9
            ticket_pay1()
        elif x == 3:
            movie = 'Chicken Blockers'
            seatnums = 13
            ticket_pay1()
        elif x == 4:
            movie = 'Not Ready Player Two'
            seatnums = 16
            ticket_pay1()
        elif x == 5:
            movie = 'I Feel Ugly'
            seatnums = 28
            ticket_pay1()
        elif x == 6:
            main_menu()
        else:
            print('Not an option')
    except ValueError:
        print('Invalid input, please put in a number')
    print(movie)

def menu3():
    try:
        x = int(input('''
1. Blue Panther
2. A Loud Area
3. Chicken Blockers
4. Not Ready Player Two
5. I Feel Ugly
6. Avengers: Finite War
7. Menu
'''))
        global seatnums
        global movie
        if x == 1:
            movie = 'Blue Panther'
            seatnums = 14
            ticket_pay1()
        elif x == 2:
            movie = 'A Loud Area'
            seatnums = 9
            ticket_pay1()
        elif x == 3:
            movie = 'Chicken Blockers'
            seatnums = 13
            ticket_pay1()
        elif x == 4:
            movie = 'Not Ready Player Two'
            seatnums = 16
            ticket_pay1()
        elif x == 5:
            movie = 'I Feel Ugly'
            seatnums = 28
            ticket_pay1()
        elif x == 6:
            movie = 'Avengers: Finite War'
            seatnums = 4
            ticket_pay1()
        elif x == 7:
            main_menu()
        else:
            print('Not an option')

    except ValueError:
        print('Invalid input, please put in a number')
        
#----------------TICKET PAYS----------------

def ticket_pay1():
    global day
    global ticket_cost
    global time
    global movie
    global ap
    if day == 'SATURDAY.txt' or day == 'SUNDAY.txt':
        ticket_cost = 12
    else:
        ticket_cost = 8
    print('Tickets are: $'  +str(ticket_cost))
    while True:
        x = open(day, 'r')
        xx = x.read()
        ap = input('AM or PM: ').lower()
        if ap == 'am' or ap == 'pm':
            ticket_pay1o1()
        else:
            print("Must be 'AM' or 'PM'")
            continue
        time = input('Movie time: ')
        order = int(time+ap)
        print(order)
        if ':' not in time:
            print("Please separate the numbers with a ':'")
            continue
        elif order in xx:
            ticket_pay2()   
        else:
            print('That time is not available')
            continue
        x.close()

def ticket_pay1o1():
    global time
    global movie
    global ap
    time = input('Movie time: ')
    order = (time+ap)
    x = open(day, 'r')
    xx = x.read()
    if order in xx:
        ticket_pay2()
    elif ':' not in time:
        print("Please separate the numbers with a ':'")
        ticket_pay1()
    elif order not in xx:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('That time is not available, pick a different time\n')
        print(xx)
        ticket_pay1()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('That time is not available, pick a different time\n')
        print(xx)
        ticket_pay1()
    
def ticket_pay2():
    #Love all these globals <3
    global ticket_cost
    global ticket_num
    global day
    global day_read
    global time
    global movie
    global balance
    global price
    global seatnums
    try:
        amnt = int(input('Amount of tickets: '))
        if seatnums >= amnt:
            seatnums = seatnums-amnt
        else:
            print('There are not that many seats available. There are ' +str(seatnums)+ ' available')
            ticket_pay2()
    except ValueError:
        print('Please input a number')
        ticket_pay2()
    price = amnt*ticket_cost
    if price > balance:
        print("""Your bank has rejected you
Account Balance: """ +str(balance)+ """
Purchase Cost: """ +str(price))
    else:
        print("You are purchasing "+str(amnt)+" tickets for '" +str(movie)+ "' at "+str(time)+ ", "+str(day_read)+' for $' +str(price))
        try:
            pp = int(input('''1. Confirm
2. Make Changes
'''))
        except ValueError:
            print("""Please pick '1' or '2'
""")
            print(pp)
        if pp == 1:
            print('Confirmed! Your purchase numer is '+str(ticket_num))
            balance = balance-(amnt*ticket_cost)
            print('Your account balance is now '+str(balance)+'!')
            mm = input('Would you like to return to the main menu?(y/n) ').lower()
            if mm == 'y':
                with open("TICKET_NUM.txt", "a") as myfile:
                    myfile.write(str(ticket_num)+'''
''')
                main_menu()
            elif mm == 'n':
                with open("TICKET_NUM.txt", "a") as myfile:
                    myfile.write(str(ticket_num)+'''
''')    
                quit()
            else:
                print("Please choose 'y' or 'n'")
        if pp == 2:
            ticket_pay1()
               
#----------------TICKET REFUND----------------
def refund():
    try:
        order = int(input("Please input the order number you'd like to refund: "))
        order = str(order)
        num = open('TICKET_NUM.txt', 'r')
        numnum = num.read()
        op = []
        if order in numnum:
            cancel = input("Are you sure you want to cancel your tickets?(y/n) ")
            if cancel == 'y':
                print('Your tickets have been canceled!!')
                balance = balance+price
                for line in num:
                    xx = line.split()
                    if order!=xx[0]:
                        op.append(line)
                y = open('TICKET_NUM.txt', 'w')
                for num in op:
                    y.write(num)
                y.close()
                num.close()
                menu = input('Would you like to return to the menu?(y/n) ')
                while True:
                    if menu == 'y':
                        main_menu()
                        break
                    elif menu == 'n':
                        quit()
                    else:
                        print("Please answer 'y' or 'n'")
                        continue
            elif cancel == 'n':
                main_menu()
            else:
                print("Please answer 'y' or 'n'")
                refund()
        
    except ValueError:
        print('Please input a ticket number')
        refund()


        


main_menu()
