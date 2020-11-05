###########################################
# Code for implementing color schemes
###########################################

class colors: 
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

###################################
######### Welcome screen
##################################


import os
rows, columns = os.popen('stty size', 'r').read().split()
width = int(columns)

os.system('clear')

hashLine = '#'
print(colors.fg.pink,end="")
print(hashLine.center(width,'#'),colors.reset)
print('\n\n\n\n\n\n')

print(colors.fg.red, colors.bold,'\t\t\t\t\t\t\t\t\t\tA',end="")
print(colors.reset,end="")
print("rth\n\n")
print("\t\t\t\t\t\t\t\t\t     Team Task\n\n")
print(colors.fg.lightcyan,"\t\t\t\t\t\t   'Menu based Python program integrating all learnt technologies'",colors.reset)
print("\n\n")

welcomeLine = 'Welcome!!'
print(welcomeLine.center(width))

print(colors.fg.lightgrey,end="")
continueLine = "Press enter to Continue..."
print(continueLine.center(width),colors.reset)

print('\n\n\n\n\n\n')
print(colors.fg.pink,end="")
print(hashLine.center(width,'#'),colors.reset)
input()

####################################
############Displaying Menu
###################################

os.system('clear')
hashLine = '#'
print(colors.fg.pink,end="")
print(hashLine.center(width,'#'),colors.reset)
print("\n")
printMenu = "Menu Items :"
print(printMenu.center(width))

print(colors.fg.yellow)
print("Press 1: To see date")
print(colors.fg.purple)
print("Press 2: To see calendar")
print(colors.fg.yellow)
print("Press 3: To set-up Hadoop Cluster")
print(colors.fg.purple)
print("Press 4: To create new AWS EC-2 instance")
print(colors.fg.yellow)
print("Press 5: To delete AWS EC-2 instance")
print(colors.fg.purple)
print("Press 6: To create new AWS S3 bucket")
print(colors.fg.yellow)
print("Press 7: To delete AWS S3 bucket")
print(colors.fg.purple)
print(colors.reset)

choice = input("Enter your choice: ")

if choice == '1' :
    os.system('clear')
    os.system('date')
elif choice == '2' :
    os.system('clear')
    os.system('cal')
elif choice == '3' :
    os.system('clear')
    print("Press A: To continue for Local Cluster")
    print("Press B: To continue for Cloud Cluster")
    choice2 = input("Enter your choice: ")
    if choice2 == 'A' :
        os.system('clear')
        print("#####Working in Local Cluster#####\n\n")
        # Code
    elif choice2 == 'B':
        os.system('clear')
        print("#####Working in Remote Cluster#####\n\n")
        # Code
    else : 
        print(colors.fg.red,"Wrong Input! Pls try again.",colors.reset)
elif choice == '4' :
    os.system('clear')
    print("Creating new AWS EC-2 instance\n\n\n")
    ##################
    ########## code
    ##################
elif choice == '5' :
    os.system('clear')
    print("Deleting AWS EC-2 instance\n\n\n")
    ##################
    ########## code
    ##################
elif choice == '6' :
    os.system('clear')
    print("Creating new AWS S3 bucket\n\n\n")
    ##################
    ########## code
    ##################
elif choice == '7':
    os.system('clear')
    print("Deleting AWS S3 bucket\n\n\n")
    ##################
    ########## code
    ##################
