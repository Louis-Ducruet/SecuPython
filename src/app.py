import os
import time


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
    if time.time() - 86400 < int(timer):
        return False
    else:
        return True
