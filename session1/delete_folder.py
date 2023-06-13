import os

import shutil

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Demo Ordner")

print(os.getcwd())

#os.rmdir(os.getcwd() + "/musik")

#os.chdir(os.getcwd() + "/musik")

#print(os.getcwd())

#for f in os.listdir():
    #os.remove(f)

#os.rmdir(os.getcwd())

shutil.rmtree(os.getcwd() + "/musik copy")