"""
     
    Creating a backup configuration of a Cisco switch or router by using 
    Paramiko module  
    Device's IP, username and password are arguments

 """


import paramiko
import time
import sys


IP = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IP, username=username, password=password, allow_agent=False, look_for_keys=False)

ssh_console = ssh.invoke_shell()

ssh_console.send("\n")
ssh_console.send("terminal length 0\n")
time.sleep(2)

ssh_console.send("\n")
ssh_console.send("show run\n")
time.sleep(5)

output = ssh_console.recv(70000)
print output

ssh.close()

