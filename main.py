import subprocess, platform
def clear_screen():
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:  # Linux and Mac
        print("\033c\033[3J")
def main_menu():
    print('''\033[32m
    ███╗   ███╗████████╗ ██████╗███████╗
    ████╗ ████║╚══██╔══╝██╔════╝██╔════╝
    ██╔████╔██║   ██║   ██║     ███████╗
    ██║╚██╔╝██║   ██║   ██║     ╚════██║
    ██║ ╚═╝ ██║   ██║   ╚██████╗███████║
    ╚═╝     ╚═╝   ╚═╝    ╚═════╝╚══════╝\033[0m
    *-----------\033[31mCoded by ShLk\033[0m------------*''')
    print("\n    Github: \033[33mhttps://github.com/ShLkprod/MTCS_V1\033[0m")
    print("    Telegram: \033[33m@Laineekz\033[0m and \033[33m@SharpCD\n")
    input("    \033[32mPress Enter to continue...\033[0m")
    clear_screen()
    category_menu()
def category_menu():
    print('''\033[32m
     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
     ████╗ ████║██╔════╝████╗  ██║██║   ██║
     ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
     ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝\033[0m
    ╭━─━─━─━─━─━─━─━─━≪✠≫━─━─━─━─━─━─━─━─━╮
     \033[33mThank you for downloading our script, 
     select a category for further actions.\033[0m
    ╰━─━─━─━─━─━─━─━─━≪✠≫━─━─━─━─━─━─━─━─━╯
    ''')
    print("    [\033[35m1\033[0m] - \033[33mNetwork Analysis.\033[0m")
    print("    [\033[35m2\033[0m] - \033[33mOperating system.\033[0m")
    print("    [\033[31m0\033[0m] - \033[31mExit.")
    print("    \033[32mEnter the request number:")
    input_val = input()
    if input_val == "1":
        clear_screen()
        network_analysis()
    if input_val == "2":
        clear_screen()
        operating_system()
    if input_val == "0":
        exit()
def network_analysis():
    print('''\033[32m
    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝\033[0m
    ╭━─━─━─━─━─━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━─━─━─━─━─━─━─━─━─╮
    \033[33m         Choose a script, depending on your goal/task.\033[0m
    ╰━─━─━─━─━─━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━─━─━─━─━─━─━─━─━─╯
        ''')
    print("    [\033[35m1\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m2\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m3\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m4\033[0m] - \033[33m.\033[0m")
    print("    [\033[31m0\033[0m] - \033[31mBack to menu.")
    print("    \033[32mEnter the request number:")
    input_val = input()
    if input_val == "1":
        clear_screen()
    if input_val == "2":
        clear_screen()
    if input_val == "3":
        clear_screen()
    if input_val == "4":
        clear_screen()
    if input_val == "0":
        clear_screen()
        category_menu()
def operating_system():
    print('''\033[32m
    ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
    ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
    ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
    ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝\033[0m
    ╭━─━─━─━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━─━─━─━─━─━─━─╮
        \033[33mChoose a script, depending on your goal/task.\033[0m
    ╰━─━─━─━─━─━─━─━─━─━─━─━─≪✠≫━─━─━─━─━─━─━─━─━─━─━─━─╯
            ''')
    print("    [\033[35m1\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m2\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m3\033[0m] - \033[33m.\033[0m")
    print("    [\033[35m4\033[0m] - \033[33m.\033[0m")
    print("    [\033[31m0\033[0m] - \033[31mBack to menu.")
    print("    \033[32mEnter the request number:")
    input_val = input()
    if input_val == "1":
        clear_screen()
    if input_val == "2":
        clear_screen()
    if input_val == "3":
        clear_screen()
    if input_val == "4":
        clear_screen()
    if input_val == "0":
        clear_screen()
        category_menu()






if __name__ == '__main__':
    main_menu()
