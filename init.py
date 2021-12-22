import time

import src.app as app
import src.classe.affichage as affichage
import src.classe.fichier as fichier
import src.classe.securite as securite

terminal = affichage.Affichage()
dossier = fichier.Fichier("input", "output")
chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])


def init():
    app.efface(terminal)
    print(terminal.info("Initialisation de l'application"))
    user = {
        "default-email": input(terminal.input("une", "adresse email", "de contact")),
        "smtp": {
            "server": input(terminal.input("le", "serveur SMTP", "d'envoie automatique email")),
            "port": int(input(terminal.input("le", "port", "du serveur SMTP"))),
            "login": input(terminal.input("le", "login", "du serveur SMTP")),
            "password": input(terminal.input("le", "mot de passe", "du serveur SMTP"))
        },
        "users": []
    }
    user['users'].append({
        "login": input(terminal.input("votre", "login", "de connexion à l'application")),
        "password": input(terminal.input("votre", "mot de passe", "de connexion à l'application"))
    })
    print("")
    dossier.ecrireFichier("user.json", user, True, True)
    contenu = dossier.contenuFichier("user.json", True)
    contenu = chiffSys.chiffrementTxt(contenu)
    dossier.ecrireFichier("user.json", contenu, True)
    valeurFichier = chiffSys.chiffrementTxt(int(time.time() - 86400))
    dossier.ecrireFichier("time.txt", valeurFichier, True)
    print(terminal.info("Fin de l'initialisation"))


init()
input(terminal.attendre("pour quitter"))
