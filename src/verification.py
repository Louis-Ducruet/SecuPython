import time
import json
import src.authentification as authentification


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
    return True


def userIntegrite(terminal, editeur, chiffSys):
    try:
        user = json.loads(authentification.userFichier(editeur, chiffSys))
        # Vérification que tous les champs existent avec vérification du typage
        temp1, temp2 = str(user['default-email']), str(user['smtp']['server'])
        temp1, temp2 = int(user['smtp']['port']), str(user['smtp']['login'])
        temp1 = str(user['smtp']['password'])
        for temp in user['users']:
            a, b = str(temp['login']), str(temp['password'])
    except:
        print(terminal.alerte("Le fichier user.json a été corrompu !"))
        return False
    return True
