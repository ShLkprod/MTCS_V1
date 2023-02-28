import subprocess, platform
def main_menu():
    print('''\033[32m
 ███╗   ███╗████████╗ ██████╗███████╗
 ████╗ ████║╚══██╔══╝██╔════╝██╔════╝
 ██╔████╔██║   ██║   ██║     ███████╗
 ██║╚██╔╝██║   ██║   ██║     ╚════██║
 ██║ ╚═╝ ██║   ██║   ╚██████╗███████║
 ╚═╝     ╚═╝   ╚═╝    ╚═════╝╚══════╝\033[0m
*-----------\033[31mCoded by ShLk\033[0m------------*''')
    print("\nGithub: \033[33mhttps://github.com/ShLkprod/MTCS_V1\033[0m")
    print("Telegram: \033[33m@Laineekz\033[0m and \033[33m@SharpCD\n")
    input("\033[32mPress Enter to continue...\033[0m")
def clear_screen():
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:  # Linux and Mac
        print("\033c\033[3J")


if __name__ == '__main__':
    main_menu()
