                    _____                _                
                   |  __ \              | |               
                   | |__) |___  __ _  __| |_ __ ___   ___ 
                   |  _  // _ \/ _` |/ _` | '_ ` _ \ / _ \
                   | | \ \  __/ (_| | (_| | | | | | |  __/
                   |_|  \_\___|\__,_|\__,_|_| |_| |_|\___|

By: Greg Schabert

Installation:
===========================================================================
First of all ensure that you have a python interpreter installed so you can
run the scripts making up the program. Once you have a python interpreter
installed on your machine, you simply need to ensure that both DDOS.py and
server.py are in the same folder as each other. Once they are in the same
folder and the interpreter is installed simply run DDOS.py and the program 
will prompt you with some input for running parameters.

Running:
===========================================================================
To run the attack for testing ensure that server.py is in the folder and 
run the DOS.py script contained in the folder. Once you launch the program
a local server instance will be launched in another window. If you intend
on testing the attack on a remote server, you can feel free to close the 
server that opened. Otherwise keep the server open if you intend on testing
on your loopback. After the server instance starts you will be prompted 
with a disclaimer for the attack. Once you hit enter you will be prompted
to select either TEST mode or ATTACK mode. 

TEST mode is the mode that should be used if you intend on not attacking a
remote server. This mode prevents the user from changing the IP target 
so as to prevent accidentally sending an attack where you didn't intend.

ATTACK mode is the mode that should be used if you intend on testing on a 
remote server that you own, or if you intend on using it on any other
remote server. As the disclaimer mentions, I am not responsible for your
actions if you use my program to attack a server and get into trouble. You
are responsible for your own actions and use ATTACK mode at your own risk.
If you are intending on using the program to test on a remote server that 
you own, if you would like to use TEST mode you simply need to make an edit
to line 322 in DDOS.py changing the value to whatever your IP/ domain name
is.

Once a mode has been selected you will be prompted with the commands for
the program. They are as follows:

Help: Provides help for various different topics. 
D: shows the disclaimer for the program again
IP: Changes the IP address *not availible in Test mode*
port: Changes the port
Num: Changes the number of connections
Time: changes the amount of time that the attack runs on each process
Atck/ Attack: Sends an attack with the given parameters
Quit: Quits the program

When using the attack function if you would like to completely take down
the server it is recommended that you change the NUM and Time to be very
large integers. With testing I have been able to run my CPU, Memory, and 
disk to 100% with about 1,000,000 connections for 120 seconds, but for the
best results I recommend having a large number of connections for a good
duration to ensure the computer is left with no resources.