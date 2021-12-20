import src.classe.affichage as affichage
import src.classe.fichier as fichier
import src.classe.securite as securite
import json
import time


def verification(dossier: fichier.Fichier, terminal: affichage.Affichage, chiffSys: securite.Securite):
    if not dossier.dossierExist():
        print(terminal.alerte("Le ou les dossier(s) {} {} n'existe(nt) pas".format(dossier.entree, dossier.entree)))
        return False
    if not dossier.fichierExiste("user.json", True):
        print(terminal.alerte("Le fichier user.json n'existe pas !"))
        return False
    if not dossier.fichierExiste("time.txt", True):
        print(terminal.alerte("Le fichier time.txt n'existe pas !"))
        time.sleep(0.5)
        dossier.ecrireHeure(chiffSys)
        print(terminal.attention("Création du fichier, par sécurité l'app est bloquée pour 24h."))
        return False
    if not secuTime(dossier, chiffSys, terminal):
        print(terminal.alerte("Suite à une tentative de hack l'app est bloquée pendant 24h !"))
        return False
    if not userIntegrite(terminal, dossier, chiffSys):
        return False
    return True


def secuTime(fichier: fichier.Fichier, chiffSys: securite.Securite, affichage: affichage.Affichage):
    timer = fichier.contenuFichier("time.txt", True)
    timer = chiffSys.chiffrementTxt(timer, False)
    try:
        int(timer)
    except:
        print(affichage.alerte("Le fichier time.txt a été corrompu !"))
        print(affichage.attention("Restauration du fichier, par sécurité l'app est bloquée pour 24h."))
        fichier.ecrireHeure(chiffSys)
        return False
    # FIXME après le dev supprimer le - 86400 final.
    if time.time() - 86400 < int(timer) - 86400:
        return False
    else:
        return True


def userIntegrite(affichage: affichage.Affichage, fichier: fichier.Fichier, chiffSys: securite.Securite):
    try:
        contenu = fichier.contenuFichier("user.json", True)
        contenu = chiffSys.chiffrementTxt(contenu, False)
        user = json.loads(contenu)
        # Vérification que tous les champs existent avec vérification du typage
        temp1, temp2 = str(user['default-email']), str(user['smtp']['server'])
        temp1, temp2 = int(user['smtp']['port']), str(user['smtp']['login'])
        temp1 = str(user['smtp']['password'])
        for temp in user['users']:
            a, b = str(temp['login']), str(temp['password'])
    except:
        print(affichage.alerte("Le fichier user.json a été corrompu !"))
        return False
    return True