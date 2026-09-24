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

colors = ['\033[31m', '\033[39m']
banner = pyfiglet.figlet_format('{name}', font='{font}')
for char in banner.split('\\n'):
    color = random.choice(colors)
    print(color + char + '\033[0m')
    time.sleep(0.05)
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
print(banner)
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


#update check 
def update_check():
    version = "1.0"
    repo = "atdevlk/next-b"
    url = f"https://api.github.com/repo/{repo}/releases/latest"
    
    try:
        res = requests.get(url, timeout=5)
        latest = res.json()["h4"].lstrip("v")

        if latest != version:
            print("\033[92mUpdate Avalible ✓ \033[0m")
        else:
            print("\033[92mYou are on latest version \033[0m")
    except:
        print("\033[91mUpdate check error ! \033[0m")

    
#print main banner
os.system("clear")
print(banner)
cmd = questionary.select(
    "Enter your choice",
     choices= ["Figlet", "Hacker", "Update", "About", "Exit"],
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

    elif cmd == "About":
        about()
        break

    elif cmd == "Update":
        update_check()
        break
        
    elif cmd == "Exit":
        break
