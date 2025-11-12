from mamba_meta.debug.decorators import Protector
from django.core.management import ManagementUtility
from multiprocessing import Process
import time
import os
import sys

from dotenv import load_dotenv
load_dotenv()

class Django_Process(Process):
    def __init__(self, *args, ch_cwd=None, host='127.0.0.1', port=8000, **kwargs):
        self.cwd = ch_cwd
        self.host = host
        self.port = port
        super().__init__(*args,**kwargs)

    def run(self):
        if self.cwd:
            os.chdir(self.cwd)

        #                             spoof     ,*runserver*, host         +port,            disable hot-reload
        utility = ManagementUtility(['manage.py','runserver', self.host+":"+str(self.port), '--noreload'])
        utility.execute()

def main(**kwargs):
    Django = Django_Process(ch_cwd='django_mamba')
    Django.start()
    while Django.is_alive:
        time.sleep(10)

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE']='django_mamba.settings'
    sys.path.append(os.getcwd()+os.path.sep+'django_mamba')
    sys.path.append(os.getcwd()+os.path.sep+'packages')
    print(sys.path)
    Protector(main)()
