import src.verification as verification
import src.app as app
import json


def userFichier(editeur, chiffSys):
    user = editeur.contenuFichier("user.json", True)
    return chiffSys.chiffrement(user, False)


def auth(terminal, editeur, chiffSys):
    if not verification.userIntegrite(terminal, editeur, chiffSys):
        return False
    user = json.loads(userFichier(editeur, chiffSys))
    for i in range(5):
        app.efface(terminal)
        print(terminal.info("Authentification en cours de développement ..."))
        if i != 0:
            print(terminal.attention("La combinaison id/mdp est incorrect il vous reste {} tentative(s)".format(5 - i)))
        login = input(terminal.input("votre", "login"))
        mdp = input(terminal.input("votre", "mot de passe"))
        for id, compte in enumerate(user['users']):
            if login == compte['login'] and mdp == compte['password']:
                app.currentUser = id
                return True
    # TODO Vérrouillage et envoie du mail
    return False