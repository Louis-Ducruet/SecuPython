import src.actionMenu as actionMenu
import src.app as app
import src.connexion as connexion
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.classe.user as user
import src.verification as verification

chiffFile = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])
dossier = fichier.Fichier("input", "output")
terminal = affichage.Affichage()
utilisateur = user.User(dossier, chiffSys)
messagerie = email.Email(utilisateur)


def start():
    app.efface(terminal)
    if not verification.verification(dossier, terminal, chiffSys):
        return False
    if not connexion.connexion(dossier, terminal, chiffSys, utilisateur, messagerie):
        return False
    while True:
        app.efface(terminal)
        app.afficheMenu(terminal)
        if actionMenu.action(terminal, dossier, chiffFile):
            return False


start()
input(terminal.attendre("pour quitter"))
