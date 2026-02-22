# Colourful Oghh Bot 
# Works best in terminal / command prompt (VS Code, PyCharm terminal, etc.)

# Color codes
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

print("\033[91m" + r"""
   /\                           
  /  \   __ _ _   _  __ _ _ __  
 / /\ \ / _` | | | |/ _` | '_ \ 
/ ____ \ (_| | |_| | (_| | | | |
_/    \_\\__,_|\__, |\__,_|_| |_|
                __/ |            
               |___/             
""" + "\033[0m")

while True:
    message = input(f"{GREEN}You       : {RESET}").lower().strip()

    if message in ["hii", "hi", "hello", "hey", "hiii"]:
        print(f"{MAGENTA}Bot       : {BOLD}oghh 🔥{RESET}")

    elif message in ["bye", "byee", "goodbye", "nikal", "band kar"]:
        print(f"{YELLOW}Bot       : {BOLD}Chal abhi ke liye oghh! 👋{RESET}")
        print(f"{CYAN}=== Bye Bhai! Come back soon ==={RESET}")
        break

    elif message == "":
        print(f"{BLUE}Bot       : Arre kuch to bol bhai... 😶{RESET}")

    else:
        print(f"{RED}Bot       : {message!r} ?  kya bol rha bhai? {RESET}")
