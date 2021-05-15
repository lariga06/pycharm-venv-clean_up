import os
import shutil

BASE = "../backup/"

os.chdir(BASE)  # change directory
main_dir = os.getcwd()  # define main directory path
folders = os.listdir(BASE)  # list dirs and files

for folder in folders:
    os.chdir(f"./{folder}")
    print(os.getcwd())

    if "venv" in os.listdir():
        venv_del = f"{os.getcwd()}\\venv"
        shutil.rmtree(venv_del)  # delete folder
    if ".idea" in os.listdir():
        idea_del = f"{os.getcwd()}\\.idea"
        print(idea_del)
        shutil.rmtree(idea_del)
    os.chdir(main_dir)  # GO BACK to previous folder
print("JOB DONE")
