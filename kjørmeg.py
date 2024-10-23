import os
import sys
import subprocess
import importlib.util


def install_things(venv_name="venv"):
    package_name = 'tkinter'

    tkinter_is_installed = True

    spec = importlib.util.find_spec(package_name)
    if spec is None:
        print(package_name +" is not installed")
        tkinter_is_installed = False

    if tkinter_is_installed == True: 
        runTkinter()

    else:
        subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-tk'])
        runTkinter()
    
def runTkinter():
    subprocess.run(['python', 'main.py'])

install_things()
