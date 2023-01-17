import os, platform
 
try:
 
        import requests
        os.system("git pull")
        os.system("termux-setup-storage")
        print('\x1b[38;5;46m checking new update CRAZY-GREEN')
        os.system("xdg-open https://www.facebook.com/groups/fb.king.cyber/?ref=share")
except:
        os.system('pip2 install requests')
import requests
bit = platform.architecture()[0]
if bit == "64bit":
        from crazy_64_green import menu
        menu()
elif bit == "32bit":
        from crazy_32_green import menu
        menu()
        
