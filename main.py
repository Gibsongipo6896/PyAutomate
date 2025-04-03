import subprocess
import pyautogui as bot
import time
import threading

def start_NP():
    subprocess.run("notepad.exe")
    
def mesej():
    time.sleep(1)
    bot.hotkey("win","up")
    bot.write("Hello, this is a sample automation with human-like process\nFeel free to fork or comit to this project",interval=0.1)
    bot.write("\nok we ain't saving this file ",interval=0.1)
    time.sleep(1)
    bot.hotkey("ctrl","a")
    bot.press("del")
    
    bot.write("\nThere is an automation project that searches for tech news , you don't need to scroll or do anything.\nThough I'm still workin on it (: just follow me on GitHub for new cool projects",interval=0.1)
    bot.write("\nYou might want to explore more project on Gibson's git :)",interval=0.1)
    time.sleep(1)
    bot.write("\n\nBye !",interval=0.1)
    time.sleep(1)
    bot.hotkey("alt","f4")
    bot.press("right")
    bot.press("return")

a = threading.Thread(target=start_NP)
b = threading.Thread(target=mesej)

a.start()
b.start()