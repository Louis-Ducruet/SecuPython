import os
import time


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


def attendre(terminal):
    input(f"Presser {terminal.bNoir}{terminal.fJaune}ENTRER{terminal.annule} pour continuer.")


def secuTime(editeur, chiffSys, terminal):
    timer = editeur.contenuFichier("time.txt", True)
    timer = chiffSys.chiffrement(timer, False)
    try:
        int(timer)
    except:
        print(f"{terminal.bRouge}Erreur : Le fichier time.txt est corrompu. Restauration du fichier !{terminal.annule}\n")
        editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
        return False
    if time.time() - 86400 < int(timer):
        return False
    else:
        return True
