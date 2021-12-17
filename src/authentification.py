import src.verification as verification


def userFichier(editeur, chiffSys):
    user = editeur.contenuFichier("user.json", True)
    return chiffSys.chiffrement(user, False)


def auth(terminal, editeur, chiffSys):
    print(terminal.info("Authentification en cours de développement ..."))
    if not verification.userIntegrite(terminal, editeur, chiffSys):
        return False
    return True
# TODO Demande 5 fois login et mdp
# TODO Vérrouillage et envoie du mail