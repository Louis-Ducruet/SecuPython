import os


def efface(terminal):
    # pour windows
    if os.name == 'nt':
        os.system('cls')
    # pour mac et linux
    else:
        os.system('clear')
    print(
        "\n\n"
        f"    {terminal.fBleu}███████╗███████╗ ██████╗██╗   ██╗{terminal.fJaune}██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗{terminal.annule}\n"
        f"    {terminal.fBleu}██╔════╝██╔════╝██╔════╝██║   ██║{terminal.fJaune}██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║{terminal.annule}\n"
        f"    {terminal.fBleu}███████╗█████╗  ██║     ██║   ██║{terminal.fJaune}██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║{terminal.annule}\n"
        f"    {terminal.fBleu}╚════██║██╔══╝  ██║     ██║   ██║{terminal.fJaune}██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║{terminal.annule}\n"
        f"    {terminal.fBleu}███████║███████╗╚██████╗╚██████╔╝{terminal.fJaune}██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║{terminal.annule}\n"
        f"    {terminal.fBleu}╚══════╝╚══════╝ ╚═════╝ ╚═════╝ {terminal.fJaune}╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{terminal.annule}\n"
    )
