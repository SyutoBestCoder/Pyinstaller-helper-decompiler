import os, shutil, time, subprocess
try:
  subprocess.check_output("pip show pyinstaller",shell=True,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError:
  os.system("pip install pyinstaller")
an = input("1. Decompile pyinstaller exe\n2. compile py to exe\n:")
if an == '1':
    print("drag your exe")
    pyPath = input()
    os.system(f'python pyinstxtractor.py "{pyPath}" ')
    print("Decompiled!")
else:
    print("Drag and drop your py file")
    pyPath = input()
    print("Drag and Drop your ico file")
    ico = input()
    os.system(f'pyinstaller "{pyPath}" --icon "{ico}" --onefile')
    time.sleep(0.2)
    os.remove("main.spec")
    shutil.rmtree("build")
    print("Succesfully created your exe!")