from Port_Scanner import nmap
import os
from svr import server
os.system("cls")

while True:
    command = input("\u001b[31;1mroot@kali\u001b[37m:~# ")
    if command == "nmap":
        nmap()
    elif command == "cls":
        os.system("cls")
    elif command == "about":
        print("Made by MarTCM")
    elif command == "help":
        print(

"""cls              clears the screen
nmap             launches nmap
msfconsole       launches MarTCM's Metasploit
about            prints the name of the creator of this terminal
help             shows all available commands"""
)
    elif command == "msfconsole":
        print("	     /	           \ ")
        print("	    ((__---,,,---__)) ")
        print("		(_) 0 0 (_)_____________ ")
        print("		   \ _ /		|\      ")
        print("		    0_0 \    M  S  F	| \ ")
        print("			 \   _________  |  * ")
        print("			  |||	    ww||| ")
        print("			  |||	      ||| ")
        msf = input("\u001b[33mmsfconsole>\u001b[37m")
        if msf == "use exploit/windows":
            exploit = input("\u001b[33mexploit/windows>\u001b[37m")
            if exploit == "exploit":
                server()









