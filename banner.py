
import pyfiglet
import random
import time
import sys

colors = ['[31m', '[39m']
banner = pyfiglet.figlet_format('Adeesha', font='cyberlarge')
for char in banner:
    color = random.choice(colors)
    sys.stdout.write(color + char + "[0m")
    sys.stdout.flush()
    time.sleep(0.02)
print()
