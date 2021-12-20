import time

import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.classe.user as user
import src.email.erreurConnexion as message


def connexion(dossier: fichier.Fichier, terminal: affichage.Affichage, chiffSys: securite.Securite, user: user.User,
              email: email.Email):
    for i in range(5):
        app.efface(terminal)
        print(terminal.info("Authentification"))
        if i != 0:
            print(terminal.attention("La combinaison id/mdp est incorrect il vous reste {} tentative(s)".format(5 - i)))
        login = input(terminal.input("votre", "login", ""))
        mdp = input(terminal.input("votre", "mot de passe", ""))
        print("")
        print(terminal.info("Vérification du Login / Mdp ..."))
        if i != 4:
            time.sleep(1)
        if user.userExist(login, mdp):
            return True
    dossier.ecrireHeure(chiffSys)
    email.envoyer(message.html, "Tentative de connexion", True)
    app.efface(terminal)
    print(terminal.alerte("Trop de tentative de connection !"))
    print(terminal.attention("Par sécurité l'app est bloquée pour 24h."))
    return False
