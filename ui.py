import os
import random
import threading

R = "\033[91m"
G = "\033[92m"
C = "\033[96m"
Y = "\033[93m"
W = "\033[97m"
D = "\033[90m"
B = "\033[1m"
X = "\033[0m"


def clear():
    os.system("clear")


def banner():
    print(f"""{C}{B}
  ██╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗
  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
  ██║██████╔╝███████╗██║     ███████║██╔██╗ ██║
  ██║██╔═══╝ ╚════██║██║     ██╔══██║██║╚██╗██║
  ██║██║     ███████║╚██████╗██║  ██║██║ ╚████║
  ╚═╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
{X}{D}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}       TERMUX OLD ID TOOL
{D}  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}
""")


def menu():
    clear()
    banner()

    print(f"{G}[1]{W} CLONE OLD ID")
    print(f"{Y}[2]{W} STOP CLONE")
    print(f"{C}[3]{W} IDZ")
    print(f"{R}[4]{W} EXIT")

    print(f"\n{D}Workers: 7 | Mode: Direct don{X}")

    return input(f"\n{G}IPSCAN {W}» {X}").strip()


def message(text, color=G):
    print(f"{color}[IPSCAN] {text}{X}")


def pause():
    input(f"\n{D}Press ENTER to continue...{X}")


# LIVE VISUAL EFFECT

def run_visual_effect(stop_event):

    while not stop_event.is_set():

        number = random.randint(0, 9999)

        line = f"100000{number:04d}***58 = 12345678"

        print(
            f"\n{C}[LIVE] {line}{X}",
            flush=True
        )

        if stop_event.wait(30):
            break
