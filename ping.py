import socket 
import sys
import os
os.system("clear")
print("#"* 40)
hostname=input("Entre Your Dns Or Target"  " :").strip()

ip= socket.gethostbyname(hostname)

print("$"*40)
print(f"Host Name Is : {hostname}")
print("$"*40)
print(f"Target Ip Is : {ip} ")

print("#"*40)
print("         ""@@@@ thank you @@@@")
print("         ""$$$$ rach chim $$$$")

