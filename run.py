from rich.console import Console
from rich.markdown import Markdown
from questionary import Style
from prompt_toolkit.formatted_text import HTML
import os
import time
import questionary
import requests


#style
qu_style = Style([
    ('highlighted', 'bg:#0000ff'),
])

#defines
console = Console()

#About
md = """
# Next-B

## Tool about
- made by ATDevLk
- release 2026
- Code by python 100%

## Social media
- **Github** - https://github.com/atdevlk
- **Linkdin** - https://www.linkedin.com/in/at-devlk-65474b435


"""
def about():
    console.print(Markdown(md))


#banner
banner = f"""
\033[38;2;0;0;215m                        888        888
                        888        888
                        888        888
88888b.  .d88b. 888  888888888     88888b.
\033[38;2;0;0;135m888 "88bd8P  Y8b`Y8bd8P'888        888 "88b
888  88888888888  X88K  888  888888888  888
\033[38;2;0;0;95m888  888Y8b.    .d8""8b.Y88b.      888 d88P
888  888 "Y8888 888  888 "Y888     88888P"
"""

#prompt text
p_text = HTML("<a>──</a><c>[</c><b>Next-b</b><c>]</c><a>─</a>> ")

#figlet script
def figlet():
    os.system("clear")
    name = input("\033[34mWhat's your name ?\033[0m: ")
    #font
    font = questionary.select(
        "Select font",
        choices = ["cyberlarge", "cybermedium", "cybersmall", "slant"],
        style = qu_style
    ).ask()
    #figlet script
    figlet_script = f"""
import pyfiglet
import random
import time
import sys

colors = ['\033[31m', '\033[39m']
banner = pyfiglet.figlet_format('{name}', font='{font}')
for char in banner:
    color = random.choice(colors)
    sys.stdout.write(color + char + "\033[0m")
    sys.stdout.flush()
    time.sleep(0.02)
print()
"""
    
    #banner python file write
    with open("banner.py", "w") as f:
        f.write(figlet_script)
        f.close()
    #move path to bashrc
    path = os.getcwd() + "/banner.py"
    #write 
    loc = os.path.expanduser("~/.bashrc")
    try:
        with open(loc, "a") as f:
            f.write("clear\n")
            f.write("python " + path)
            
        os.system("source " + loc)
        print("\033[92m[✓] Done \033[0m")
    except:
        print("\033[91m[!] Not Found bashrc \033[0m")


#hacker
def hacker():
    name = input("\033[34mWhat's your name ?\033[0m: ")
    #hacker script
    hacker_script = f"""
import os
import sys
import time
    
os.system("clear")
banner = '''
\033[38;2;228;228;228m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿  @{name}
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
\033[38;2;188;188;188m⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
\033[38;2;128;128;128m⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print()
    """
    #banner python file write
    with open("banner.py", "w") as f:
        f.write(hacker_script)
        f.close()
    #move path to bashrc
    path = os.getcwd() + "/banner.py"
    #write 
    loc = os.path.expanduser("~/.bashrc")
    try:
        with open(loc, "a") as f:
            f.write("clear\n")
            f.write("python " + path)

        os.system("source " + loc)
        print("\033[92m[✓] Done \033[0m")
    except:
        print("\033[91m[!] Not Found bashrc \033[0m")


#animate_welcomme
def animate_welcome():
    #get name
    name = input("\033[34mWhat's your name ?\033[0m: ")
    #animate_welcomee script
    animate_wel = f"""
import os
import time
import sys

os.system('clear')
wel = 'welcome to Termux, {name}'
for char in wel:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
print()
time.sleep(0.2)
os.system('clear')
banner = '''
\033[38;2;95;215;0m########:'########:'########::  
... ##..:: ##.....:: ##.... ##:  
\033[38;2;135;255;135m::: ##:::: ##::::::: ##:::: ##:  
::: ##:::: ######::: ########::     \\033[91m@{name}\033[38;2;135;255;135m  
\033[38;2;135;255;215m::: ##:::: ##...:::: ##.. ##:::  
\033[38;2;175;255;255m::: ##:::: ##::::::: ##::. ##::  
::: ##:::: ########: ##:::. ##:MUX
'''
for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)
print()
"""
    #write python file
    with open("banner.py", "w") as f:
        f.write(animate_wel)
        f.close()

    
#update check 
def update_check():
    version = "1.0"
    repo = "atdevlk/next-b"
    url = f"https://api.github.com/repos/{repo}/releases/latest"

    with console.status("Scanning..") as status:
         try:
            res = requests.get(url, timeout=5) 
            res.raise_for_status()
            latest = res.json()["tag_name"].lstrip("v")

            if latest != version:
                console.print("[green]Update Avalible ✓ [/green]")
            else:
                console.print("[green]You are on latest version [/green]")
         except:
             console.print("[red]Update check error ! [/red]")

    
#print main banner
os.system("clear")
print(banner)
cmd = questionary.select(
    "Enter your choice",
     choices= ["Figlet", "Hacker", "Animate_welcome",
                "Update", "About", "Exit"],
     style = qu_style
).ask()

#listenig
while True:
    
    if cmd == "Figlet":
        figlet()
        break
        
    elif cmd == "Hacker":
        hacker()
        break

    elif cmd == "Animate_welcome":
        animate_welcome()
        break

    elif cmd == "About":
        about()
        break

    elif cmd == "Update":
        update_check()
        break
        
    elif cmd == "Exit":
        break
