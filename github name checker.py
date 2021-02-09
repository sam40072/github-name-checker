import requests
import time

baselink = 'https://github.com/'
def checkname(name):
    sendrequest = requests.get(baselink + name)
    if (sendrequest.status_code == 200): # 200 means that the page was found which means name is taken
        print(f'\033[91mname {name} is not available')
    elif (sendrequest.status_code == 404):# page not found which means name is not taken
        print(f'\033[92mname {name} is available')
    else:
        print(sendrequest.status_code)

def checknamefromlist(file_location):
    try:
        openfile = open(file_location, 'r')
        lines = openfile.readlines()
        for line in lines:
            checkname(line.strip())
            time.sleep(0.55)
    except:
        print('something went wrong')

def main():
    running = True
    while (running == True):
        print('1) Check name\n2) Check names from a list\n3) quit')
        choice = input(">")
        if (choice == '1'):
            name = input("enter name > ")
            print('\n')
            checkname(name)
            print('\n')
        if (choice == '2'):
            print('\n')
            file_location = input("location of the file > ")
            checknamefromlist(file_location)
            print('\n')
        if (choice == '3'):
            running = False


main()