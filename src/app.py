import os
import time

currentUser = None


def efface(terminal):
    # pour windows
    if os.name == 'nt':
        os.system('cls')
    # pour mac et linux
    else:
        os.system('clear')
    print(terminal.logo())


def attendre(terminal, message):
    input(terminal.attendre(message))


def secuTime(editeur, chiffSys, terminal):
    timer = editeur.contenuFichier("time.txt", True)
    timer = chiffSys.chiffrement(timer, False)
    try:
        int(timer)
    except:
        print(terminal.alerte("Le fichier time.txt a été corrompu !"))
        print(terminal.attention("Restauration du fichier, par sécurité l'app est bloquée pour 24h."))
        editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
        return False
    # FIXME Remouve - 86400 after dev test
    if time.time() - 86400 < int(timer):
        return False
    else:
        return True


def afficheMenu(terminal):
    print(terminal.info("Menu SecuPython"))
    print(terminal.menu(1, "chiffrer (.txt)"))
    print(terminal.menu(2, "déchiffrer (.txt)"))
    print(terminal.menu(3, "chiffrer (.jpg, .png)"))
    print(terminal.menu(4, "déchiffrer (.jpg, .png)"))
    print(terminal.menu(5, "les paramètres"))
    print(terminal.menu(6, "se déconnecter"))
    print("")
