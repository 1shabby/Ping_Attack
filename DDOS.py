import time
import socket
import random
import sys
import threading
import webbrowser
import os
import multiprocessing
from itertools import product


FLAG = 1


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))  # Green Text
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))  # Yellow Text
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))  # Red Text


def printHeader():
    prRed("DDDDDDDDDDDDD       DDDDDDDDDDDDD              OOOOOOOOO         SSSSSSSSSSSSSSS \n"
          " D::::::::::::DDD    D::::::::::::DDD         OO:::::::::OO     SS:::::::::::::::S\n"
          " D:::::::::::::::DD  D:::::::::::::::DD     OO:::::::::::::OO  S:::::SSSSSS::::::S\n"
          " DDD:::::DDDDD:::::D DDD:::::DDDDD:::::D   O:::::::OOO:::::::O S:::::S     SSSSSSS\n"
          "   D:::::D    D:::::D  D:::::D    D:::::D  O::::::O   O::::::O S:::::S            \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O S:::::S            \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O  S::::SSSS         \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O   SS::::::SSSSS    \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O     SSS::::::::SS  \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O        SSSSSS::::S \n"
          "   D:::::D     D:::::D D:::::D     D:::::D O:::::O     O:::::O             S:::::S\n"
          "   D:::::D    D:::::D  D:::::D    D:::::D  O::::::O   O::::::O             S:::::S\n"
          " DDD:::::DDDDD:::::D DDD:::::DDDDD:::::D   O:::::::OOO:::::::O SSSSSSS     S:::::S\n"
          " D:::::::::::::::DD  D:::::::::::::::DD     OO:::::::::::::OO  S::::::SSSSSS:::::S\n"
          " D::::::::::::DDD    D::::::::::::DDD         OO:::::::::OO    S:::::::::::::::SS \n"
          " DDDDDDDDDDDDD       DDDDDDDDDDDDD              OOOOOOOOO       SSSSSSSSSSSSSSS   \n")

    _start = input("Press enter to continue...\n")


def printInfo():
    prYellow("####################################################################\n"
             " #            THIS IS FOR EDUCATIONAL PURPOSES ONLY!                #\n"
             " ####################################################################\n"
             " # This piece of software is designed to perform a                  #\n"
             " # DOS (Denial Of Service) attack on a specified IP/ domain         #\n"
             " # by attacking a specific port. This script is capable of taking   #\n"
             " # remote or local servers down with relative ease. This is your    #\n"
             " # warning that your decision to use this script is your own and if #\n"
             " # you find yourself in trouble for using this script to take down  #\n"
             " # a remote server you are at fault.                                #\n"
             " ####################################################################\n")


def printOptions():
    prYellow("#######################################################################\n"
             " # HELP : Help                                                         #\n"
             " #  D   : Disclaimer for the software                                  #\n"
             " #  IP  : Designate the target IP address / Domain name for the attack #\n"
             " # PORT : Designate the target port for the attack (Default 80)        #\n"
             " # NUM  : Designate the number of threads to run the attack on         #\n"
             " # TIME : Designate the duration of the attack (in sec) on each thread #\n"
             " # ATCK : Run the attack on the designated IP and Port                 #\n"
             " # QUIT : Quit the program                                             #\n"
             " #######################################################################\n")


def printHelpMenu():
    prYellow("####################################################################\n"
             " #                             HELP MENU                            #\n"
             " ####################################################################\n"
             " # PORT : Port list containing services                             #\n"
             " #  IP  : IPs and Domains for testing the app                       #\n"
             " # ERR  : Contains info about expereincing crashes while running    #\n"
             " # QUIT : Return to the main menu                                   #\n"
             " ####################################################################\n")


def printPortUsage():
    prYellow("#########################################################################\n"
             " #                       PORT SERVICES CHEAT SHEET                       #\n"
             " #########################################################################\n"
             " # PORT(s) #               Service                 #  Transport Protocol #\n"
             " # 20, 21  #  File Transfer Protocol (FTP)         #         TCP         #\n"
             " # 22      #  Secure Shell (SSH)                   #     TCP and UDP     #\n"
             " # 23      # Telnet                                #         TCP         #\n"
             " # 25      # Simple Mail Transfer Protocol (SMTP)  #         TCP         #\n"
             " # 50, 51  # IPSec				  #         NA          #\n"
             " # 53      # Domain Name System (DNS)              #     TCP and UDP     #\n"
             " # 80      # HyperText Transfer Protocol (HTTP)    #         TCP         #\n"
             " # 443     # HTTP with Secure Sockets Layer (SSL)  #     TCP and UDP     #\n"
             " #########################################################################\n")


def printIPUsage():
    prYellow("#################################################\n"
             " #                    IP HELP                    #\n"
             " #################################################\n"
             " # For testing purposes, plese ensure that the   #\n"
             " # IP target is set to 127.0. 0.1 or localhost   #\n"
             " # to ensure that you are not attacking someone  #\n"
             " # on accident. If you would like to attack a    #\n"
             " # server that you own ensure that the IP is the #\n"
             " # same as printed when you run ipconfig on the  #\n"
             " # server. Also note that you can target a web   #\n"
             " # server by using the domain name as the target #\n"
             " # instead of an IPv4 address. Ex www.google.com #\n"
             " #################################################\n")


def printErrorHelp():
    prYellow("#################################################\n"
             " #                  ERROR HELP                   #\n"
             " #################################################\n"
             " # When running you may come across some errors  #\n"
             " # or crashes. I recommend looking up the error  #\n"
             " # Also please ensure that if you are trying to  #\n"
             " # to DDOS your loopback ip (127.0.0.1) that you #\n"
             " # have a server socket running and ensure that  #\n"
             " # the port and IP of the server and attack are  #\n"
             " # the same. To launch a server socket please    #\n"
             " # run the server.py file contained within the   #\n"
             " # folder that contained this file.              #\n"
             " #################################################\n")


def helpMenuHandling():  # Handles the helpmenu
    check = True
    while check:
        printHelpMenu()
        feedback = input("Please enter the topic you would like help with.\n")
        if feedback.upper() == "PORT":
            printPortUsage()
        elif feedback.upper() == "IP":
            printIPUsage()
        elif feedback.upper() == "ERR":
            printErrorHelp()
        elif feedback.upper() == "QUIT":
            check = False
            return
        feedback = input("Press enter to continue...")


def selectMode():  # Prompts the user to select which mode to run the app in
    check = True
    while check:
        feedback = input(
            "Would you like to run the app for testing or to perform an attack? (Test/ Attack)\n")
        if feedback.upper() == "TEST":
            prGreen("You are going to enter " + feedback +
                    " mode. This means that you will not be able to change\n"
                    "the IP address to ensure you do not send an attack on accident.\n"
                    "To change modes please quit and restart the app.\n")
            response = input(
                "Are you sure that you want to continue in TEST mode? (y/n)\n")
            if response.upper() == "Y" or response.upper() == "YES":
                check = False
        elif feedback.upper() == "ATTACK":
            prGreen("You are going to enter " + feedback +
                    " mode. This means that you will be able to modifiy the target IP address.\n"
                    "Please note that this WILL allow you to send attacks to servers. Please\n"
                    "review the warning before sending an attack and understand that I am NOT\n"
                    "responsible for your actions if you decide to send an attack and get into\n"
                    "trouble.\n")
            response = input(
                "Are you sure that you want to continue in ATTACK mode? (y/n)\n")
            if response.upper() == "Y" or response.upper() == "YES":
                check = False
        else:
            prRed("Please chose either TEST or ATTACK as the mode to run.")
    return feedback.upper()


def printStartup():  # Prints start up info and
    printHeader()
    printInfo()
    mode = selectMode()
    _confirm = input("Press enter to accept.")
    printOptions()
    return mode


# Prints the items you can change


def printTargets(mode, destination, portNum, thread_count, duration):
    if mode.upper() == "ATTACK":
        prRed("Mode: " + mode + " *CAUTION IP TARGETING IS ENABLED*\n")
    elif mode.upper() == "TEST":
        prGreen("Mode: " + mode + "\n")
    prGreen("Destination: " + destination + "\n")
    prGreen("Port: " + str(portNum) + "\n")
    prGreen("Number of Connections (Threads): " + str(thread_count) + "\n")
    prGreen("Duration of Attack (in seconds): " + str(duration) + "\n")


def IPTarCheck(mode, target):  # Checks to see which mode the app is ran in and gives proper response
    if mode == "ATTACK":
        target = setIPTar(target)
    else:
        prRed("This function is not availible in this mode.\n"
              " Please switch to ATTACk if you would like to\n"
              " change the IP.\n")
    return target


def setIPTar(destination):  # Sets the target IP / Domain
    check = True
    while check:
        destination = input("Please Designate the target IP or domain name.\n")
        prGreen("You entered " + destination + "\n")
        feedback = input(
            "Are you sure that you want to target this IP/ domain? (y/n)\n")
        if feedback.upper() == "Y" or feedback.upper() == "YES":
            check = False
            return destination


def setPortTar(portTar):
    check = True
    while check:
        portTar = input(
            "Please designate the target Port that you would like to connect to.\n"
            "Enter H if you are unsure of what port to connect to.\n")
        prGreen("you entered " + str(portTar) + "\n")
        if portTar.upper() == "H":
            printPortUsage()
        elif portTar.upper() != "H" or portTar() != " " or portTar() != "\n":
            feedback = input(
                "Are you sure that you want to target this Port? (y/n)\n")
            if feedback.upper() == "Y" or feedback.upper() == "YES":
                check = False
                return int(portTar)


def setThreadCount(thread_count):  # Sets the number of connections
    check = True
    while check:
        thread_count = input(
            "Please designate the number of threads that you would like to use.\n")
        if int(thread_count) < 1:
            prRed("The thread count can not be less than 1!\n")
        else:
            prGreen("You entered " + str(thread_count) +
                    " as the number of threads to run the attack on.\n")
            feedback = input("Are you sure that you want to run the attack on " +
                             str(thread_count) + " threads? (y/n)\n")
            if feedback.upper() == "Y" or feedback.upper() == "YES":
                check = False
                return int(thread_count)


def setDuration(duration):  # Sets how long an attack will last. Note this is for each connection so the overall time make take longer than this
    check = True
    while check:
        duration = input("Please designate the duration of the attack.\n")
        if int(duration) < 1:
            prRed("The duration count can not be less than 1!\n")
        else:
            prGreen("You entered " + str(duration) +
                    "as the duration of the attack.\n")
            feedback = input(
                "Are you sure that you want to set the duration to " + duration + " seconds? (y/n)\n")
            if feedback.upper() == "Y" or feedback.upper() == "YES":
                check = False
                return int(duration)


def attack(target, port, duration):
    prRed(f'Attacking for {duration}')
    for _sec in range(duration):
        prGreen(f'Attacked: {target}:{port}')
        time.sleep(0.5)  # Delay between attacks (in seconds)


def prepAttack(numThreads, target, port, duration):
    atk_list = list()

    for _i in range(numThreads):
        atk_list.append([target, port, duration])

    return atk_list


def startAttack(attackers, attack_list, target, port, duration):
    global POOL
    attack_list = prepAttack(attackers, target, port, duration)

    POOL = multiprocessing.Pool(processes=attackers)
    with POOL:
        results = POOL.starmap(attack, attack_list)

    prYellow(f'Result: {results}')


def startServer():
    os.system('start py server.py')


def launchWebConnection(target, port):
    webbrowser.open(target + '/' + str(port))


def get_input():
    global FLAG
    FLAG = 1
    global POOL
    while FLAG == 1:
        keystrk = input('Send "C" to stop attack \n')
        # thread doesn't continue until key is pressed
        print('You pressed: ', keystrk)
        if keystrk.upper() == 'C':
            FLAG = False
            print('FLAG is now:', FLAG)
            POOL.close()
            POOL.terminate()
            POOL.join()


def main():
    target = 'localhost'  # specified IP/ domain
    port = 80  # specified port
    num_connections = 100  # Set the number of threads to run on
    duration = 60  # seconds

    startServer()
    mode = printStartup()

    check = True
    while check:
        printTargets(mode, target, port, num_connections, duration)
        feedback = input("Please select a task to run.\n")
        if feedback.upper() == "HELP":
            helpMenuHandling()
        elif feedback.upper() == "D" or feedback.upper() == "DISCLAIMER":
            printInfo()
        elif feedback.upper() == "IP":
            target = IPTarCheck(mode, target)
        elif feedback.upper() == "PORT":
            port = setPortTar(port)
        elif feedback.upper() == "NUM":
            num_connections = setThreadCount(num_connections)
        elif feedback.upper() == "TIME":
            duration = setDuration(duration)
        elif feedback.upper() == "ATCK" or feedback.upper() == "ATTACK":
            launchWebConnection(target, port)
            processList = prepAttack(num_connections, target, port, duration)
            atk_thread = threading.Thread(target=startAttack, args=(
                num_connections, processList, target, port, duration))
            input_thread = threading.Thread(target=get_input)
            input_thread.start()
            atk_thread.start()
        elif feedback.upper() == "QUIT":
            exit()
        feedback = input("Press enter to continue...\n")
        printOptions()


if __name__ == '__main__':
    main()
