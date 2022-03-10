from subprocess import check_output


class ADB:
    def StartServer(self):
        check_output(['adb', 'start-server'])

    def adb(self,c):
        check_output(c.split())
