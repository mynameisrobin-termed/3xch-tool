from pystyle import Write, Colors
from colorama import Fore, init
import requests
import time
import os
import subprocess
import sys
import tempfile
import shutil
import random

sys.dont_write_bytecode = True

init()

commands = {
    "1": "massban",
    "2": "masschannel",
    "3": "massdelch",
    "4": "webhook",
    "5": "dwebhook",
    "6": "nuker",
    "7": "tspam",
    "8": "givadmin",
    "9": "massrole",
    "10": "dallmessage",
    "11": "massleave",
    "update": "update",
    "exit": sys.exit,
    "mass ban": "massban",
    "mass create channels": "masschannel",
    "delete all channels": "massdelch"
}


def banner():
    banner_text = """

▓█████ ▒██   ██▒ ▄████▄   ██░ ██ 
▓█   ▀ ▒▒ █ █ ▒░▒██▀ ▀█  ▓██░ ██▒
▒███   ░░  █   ░▒▓█    ▄ ▒██▀▀██░
▒▓█  ▄  ░ █ █ ▒ ▒▓▓▄ ▄██▒░▓█ ░██ 
░▒████▒▒██▒ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
░░ ▒░ ░▒▒ ░ ░▓ ░░ ░▒ ▒  ░ ▒ ░░▒░▒
 ░ ░  ░░░   ░▒ ░  ░  ▒    ▒ ░▒░ ░

"""
    print(Fore.RED + banner_text)


def update():
    temp_dir = tempfile.mkdtemp()
    shutil.copy("commands/update.py", temp_dir)
    print(temp_dir)
    subprocess.run(f"start cmd /k python {temp_dir}/update.py", shell=True)
    sys.exit(0)


def main():
    response = requests.get(
        "https://raw.githubusercontent.com/dropalways/netcry-nuker/main/version.txt")  # get latest version
    with open("version.txt", "r") as file:
        localversion = file.readline().strip()  # save local version as variable
    if localversion < response.text:  # compare local version to latest version
        rng = random.randint(1, 10)
        if rng == 7:  # 1/10 chance of displaying this message
            result = easygui.buttonbox(
                f"Current version({localversion}) isn't up to date with the latest release({response.text}). Do you want to install the latest version?",
                title="Netcry", choices=["OK", "No"])
            # root = tk.Tk()
            # root.title("Netcry")
            # root.geometry("0x0")
            # root.iconify()
            # update_question = messagebox.askyesno("Netcry", f"Current version({localversion}) isn't up to date with latest release({response.text}) Do you want to install the latest version?", icon='warning')
            # if update_question:
            #     update()
            #     root.destroy()
            # else:
            #     root.destroy()
            # root.mainloop()
            if result == "OK":
                update()
            else:
                pass
    os.system('clear' if os.name != 'nt' else 'cls')
    os.system(f"title Netcry")
    with open("token.txt", "r") as file:
        token = file.readline().strip()
    if token == "":
        print("Empty token")
        sys.exit(1)
    elif token == "single token here":
        print("You havent edited the file 'token.txt'.")
        sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}
    response = requests.get(
        "https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        data = response.json()
        user_id = data['id']
        invite_link = f"https://discord.com/api/oauth2/authorize?client_id={user_id}&permissions=8&scope=bot"
        options = f"""{Fore.LIGHTMAGENTA_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {Colors.gray}discord: 3xch{Fore.LIGHTMAGENTA_EX}  ┃       {Colors.gray}https://guns.lol/3xch{Fore.LIGHTMAGENTA_EX}        ┃  {Colors.gray}https://github.com/mynameisrobin_termed{Fore.LIGHTMAGENTA_EX}  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [{Colors.gray}1{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass ban{Fore.LIGHTMAGENTA_EX}                   ┃  [{Colors.gray}10{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass purge messages{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}19{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}2{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create channels{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}11{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass leave servers{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}20{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}3{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Delete all channels{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}12{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}21{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}4{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}13{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}22{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}5{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook deleter{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}14{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}23{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}6{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Nuker bot{Fore.LIGHTMAGENTA_EX}                  ┃  [{Colors.gray}15{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}24{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}7{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Channel spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}16{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}25{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}8{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Give admin to a user{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}17{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}26{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}9{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create roles{Fore.LIGHTMAGENTA_EX}          ┃  [{Colors.gray}18{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}27{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃    {Colors.gray}{invite_link}{Fore.LIGHTMAGENTA_EX}   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""  # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻
        os.system('clear' if os.name != 'nt' else 'cls')
        banner()
        print(Fore.LIGHTMAGENTA_EX + options)
    else:
        options2 = f"""{Fore.LIGHTMAGENTA_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {Colors.gray}discord: 3xch{Fore.LIGHTMAGENTA_EX}  ┃       {Colors.gray}https://guns.lol/3xch{Fore.LIGHTMAGENTA_EX}        ┃  {Colors.gray}https://github.com/mynameisrobin_termed{Fore.LIGHTMAGENTA_EX}  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [{Colors.gray}1{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass ban{Fore.LIGHTMAGENTA_EX}                   ┃  [{Colors.gray}10{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass purge messages{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}19{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}2{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create channels{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}11{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass leave servers{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}20{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}3{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Delete all channels{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}12{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}21{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}4{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}13{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}22{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}5{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook deleter{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}14{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}23{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}6{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Nuker bot{Fore.LIGHTMAGENTA_EX}                  ┃  [{Colors.gray}15{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}24{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}7{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Channel spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}16{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}25{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}8{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Give admin to a user{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}17{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}26{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}9{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create roles{Fore.LIGHTMAGENTA_EX}          ┃  [{Colors.gray}18{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}27{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
        banner()
        print(options2)

    while True:
        try:
            user_input = Write.Input(f"\n\nChoice""@3xch━>>> ", Colors.gray, interval=0.03)

        except KeyboardInterrupt:
            sys.exit()

        user_input = user_input.lower()

        if user_input in commands:
            if user_input == "exit":
                commands[user_input]()
            elif user_input == "update":
                update()
            else:
                try:
                    os.system('clear' if os.name != 'nt' else 'cls')
                    subprocess.run(["python", str(f"commands/{commands.get(user_input)}.py")])
                    time.sleep(0.7)
                    main()
                except KeyboardInterrupt:
                    sys.exit()
        elif user_input == "":
            print("Error: Enter something")
            time.sleep(0.7)
            main()
        elif user_input == "reload":
            main()
        else:
            print(Fore.RED + "Error 404: Command not found")
            time.sleep(0.7)
            main()


if __name__ == "__main__":
    main()
