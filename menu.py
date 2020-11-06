#####################################################
# Code for implementing color schemes
#####################################################

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



####################################################
#########functions
####################################################
def menu() :
    os.system('clear')
    hash()
    print("\n")
    printMenu = "Menu Items :"
    print(printMenu.center(width))

    print(colors.fg.yellow)
    print("Press 1: To see date")
    print(colors.fg.purple)
    print("Press 2: To see calendar")
    print(colors.fg.yellow)
    print("Press 3: To go to Hadoop menu")
    print(colors.fg.purple)
    print("Press 4: To go to AWS menu")
    print(colors.fg.yellow)
    print("Press 5: To go to Docker menu")
    print(colors.fg.purple)
    print("Press 6: To go to Machine Learning menu")
    print(colors.fg.yellow)
    print("Press Q: To Quit")
    print(colors.reset)

    choice = input("Enter your choice: ")

    if choice == '1' :
        date()
    elif choice == '2' :
        cal()
    elif choice == '3' :
        hadoop()
    elif choice == '4' :
        aws()
    elif choice == '5' :
        docker()
    elif choice == '6' :
        ML()
    elif choice == 'Q' :
        exit()
    else :
        print(colors.fg.red,"Error: Wrong input!",colors.reset)

def hash() :
    hashLine = '#'
    print(colors.fg.pink,end="")
    print(hashLine.center(width,'#'),colors.reset)


def date() :
    os.system('clear')
    os.system('date')


def cal() :
    os.system('clear')
    os.system('cal')
    

def ML() :
    ####################
    ##Complete this function
    #####################
    os.system('clear')
    hash()
    greet = "Welcome to Machine Learning assistant!"
    print(colors.fg.green)
    print(greet.center(width))
    print(colors.reset)

def docker() :
    os.system('clear')
    hash()
    greet = "Welcome to Docker assistant!"
    print(colors.fg.green)
    print(greet.center(width))
    print(colors.reset)
    print("Press 1: To start docker engine\n")
    print("Press 2: To stop docker engine\n")
    print("Press 3: To list docker info\n")
    print("Press 4: To list all docker os\n")
    print("Press 5: To launch docker OS\n")
    print("Press 6: To start docker OS\n")
    print("Press 7: To attach screen to docker OS\n")
    print("Press 8: To delete docker OS\n")
    print("Press 9: To delete All docker OS\n")
    print("Press 10: To download docker image\n")
    print("Press 11: To remove docker image\n")
    print("Press M: To go back to Main Menu\n")
    print("Press Q: To quit\n")
    choiceDocker = input('\nEnter your choice : ')

    if choiceDocker == '1' :
        os.system('systemctl start docker')
    elif choiceDocker == '2' :
        os.system('systemctl stop docker')
    elif choiceDocker == '3' :
        os.system('docker info')
    elif choiceDocker == '4' :
        os.system('docker ps -a')
    elif choiceDocker == '5' :
        osName = input("Enter image os : ")
        osVersion = input("Enter OS version : ")
        launchInfo = 'docker run -it ' + osName + ':' + osVersion
        os.system(launchInfo)
    elif choiceDocker == '6' :
        osName = input("Enter os name: ")
        startInfo = 'docker start ' + osName
        os.system(startInfo)
    elif choiceDocker == '7' :
        osName = input("Enter os name: ")
        attachInfo = 'docker attach ' + osName
        os.system(attachInfo)
    elif choiceDocker == '8' :
        osName = input("Enter os name: ")
        deleteInfo = 'docker rm -f ' + osName
        os.system(deleteInfo)
    elif choiceDocker == '9' :
        os.system('docker rm `docker ps -a -q`')
    elif choiceDocker == '10' :
        osName = input("Enter image os : ")
        osVersion = input("Enter OS version : ")
        pullInfo = 'docker pull ' + osName + ':' + osVersion
        os.system(pullInfo)
    elif choiceDocker == '11' :
        osName = input("Enter image os : ")
        osVersion = input("Enter OS version : ")
        removeInfo = 'docker rmi -f ' + osName + ':' + osVersion
        os.system(removeInfo)
    elif choiceDocker == 'M' :
        menu()
    elif choiceDocker == 'Q' :
        exit()
    else :
        print(colors.fg.red,"Error: Wrong Input!",colors.reset)


def hadoop() :
    ####################
    ##Complete this function
    #####################
    os.system('clear')
    hash()
    greet = "Welcome to Hadoop assistant!"
    print(colors.fg.green)
    print(greet.center(width))
    print(colors.reset)

    print("Press A: To continue for Local Cluster")
    print("Press B: To continue for Cloud Cluster")
    choiceHadoop = input("Enter your choice: ")
    if choiceHadoop == 'A' :
        os.system('clear')
        print("#####Working in Local Cluster#####\n\n")
        # Code
    elif choiceHadoop == 'B':
        os.system('clear')
        print("#####Working in Remote Cluster#####\n\n")
        # Code
    else : 
        print(colors.fg.red,"Wrong Input! Pls try again.",colors.reset)


def aws() :
    ####################
    ##Complete this function
    #####################
    os.system('clear')
    hash()
    greet = "Welcome to AWS assistant!"
    print(colors.fg.green)
    print(greet.center(width))
    print(colors.reset)

    print("Press 1: For creating new AWS EC-2 instance\n\n\n")
    print("Press 2: For deleting AWS EC-2 instance\n\n\n")
    print("Press 3: For creating new AWS S3 bucket\n\n\n")
    print("Press 4: deleting AWS S3 bucket\n\n\n")
    choiceAws = input('Enter your choice : ')
    if choiceAws == '1' :
        os.system('clear')

####################################################
######### Welcome screen
####################################################

import os
rows, columns = os.popen('stty size', 'r').read().split()
width = int(columns)

os.system('clear')

hash()
print('\n\n\n\n\n\n\n\n\n\n\n\n')

print(colors.fg.red, colors.bold,'\t\t\t\t\t\t\t\t\t\tA',end="")
print(colors.reset,end="")
print("rth\n\n")
print("\t\t\t\t\t\t\t\t\t     Team Task\n\n")
print(colors.fg.lightcyan,"\t\t\t\t\t\t   'Menu based Python program integrating all learnt technologies'",colors.reset)
print("\n\n")

welcomeLine = 'Welcome!!'
print(welcomeLine.center(width))

print(colors.fg.darkgrey,end="\n")
continueLine = "Press enter to Continue..."
print(continueLine.center(width),colors.reset)

print('\n\n\n\n\n\n\n\n\n\n\n\n\n')
hash()
input()

#################################
##########Displaying Menu
#################################

menu()
