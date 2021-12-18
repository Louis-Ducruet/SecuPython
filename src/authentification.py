import src.verification as verification
import src.email as email
import src.app as app
import json
import time


def decodeUser(editeur, chiffSys):
    user = editeur.contenuFichier("user.json", True)
    user = chiffSys.chiffrement(user, False)
    editeur.ecrireFichier("user.json", user, True)


def userFichier(editeur, chiffSys):
    user = editeur.contenuFichier("user.json", True)
    return chiffSys.chiffrement(user, False)


def auth(terminal, editeur, chiffSys):
    if not verification.userIntegrite(terminal, editeur, chiffSys):
        return False
    user = json.loads(userFichier(editeur, chiffSys))
    for i in range(5):
        app.efface(terminal)
        print(terminal.info("Authentification :"))
        if i != 0:
            print(terminal.attention("La combinaison id/mdp est incorrect il vous reste {} tentative(s)".format(5 - i)))
        login = input(terminal.input("votre", "login"))
        mdp = input(terminal.input("votre", "mot de passe"))
        for id, compte in enumerate(user['users']):
            if login == compte['login'] and mdp == compte['password']:
                app.currentUser = id
                return True
    app.efface(terminal)
    print(terminal.info("Authentification :"))
    print(terminal.info("Vérification du Login / Mdp ..."))
    editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
    mail = email.Mail(user)
    mail.envoyer()
    print(terminal.alerte("Trop de tentative de connection !"))
    print(terminal.attention("Par sécurité l'app est bloquée pour 24h."))
    return False
