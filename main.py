import src.actionMenu as actionMenu
import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.classe.user as user
import src.connexion as connexion
import src.verification as verification

terminal = affichage.Affichage()


def start():
    app.efface(terminal)
    dossier = fichier.Fichier("input", "output")
    chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])
    if not verification.verification(dossier, terminal, chiffSys):
        return False
    chiffFile = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
    utilisateur = user.User(dossier, chiffSys)
    messagerie = email.Email(utilisateur)
    if not connexion.connexion(dossier, terminal, chiffSys, utilisateur, messagerie):
        return False
    while True:
        app.efface(terminal)
        app.afficheMenu(terminal)
        if actionMenu.action(terminal, dossier, chiffFile, messagerie, utilisateur):
            return False


start()
input(terminal.attendre("pour quitter"))
