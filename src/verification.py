import time


def verificationDepart(app, chiffSys, editeur, terminal):
    # Vérification si les données utilisateurs existe
    if not editeur.fichierExiste("user.json", True):
        print(terminal.alerte("Le fichier user.json n'existe pas !"))
        return False
    # Vérification si les dossiers input et output existe
    if not editeur.dossierExiste():
        print(terminal.alerte("Le ou les dossier(s) {} {} n'existe(nt) pas".format(editeur.input, editeur.output)))
        return False
    # Vérification s'il y a eu une tentative de hack
    if not editeur.fichierExiste("time.txt", True):
        print(terminal.alerte("Le fichier time.txt n'existe pas !"))
        time.sleep(0.5)
        editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
        print(terminal.attention("Création du fichier, par sécurité l'app est bloquée pour 24h."))
        return False
    if not app.secuTime(editeur, chiffSys, terminal):
        print(terminal.alerte("Suite à une tentative de hack l'app est bloquée pendant 24h !"))
        return False
