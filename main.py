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
    # Définir les dossiers d'entrée et de sortie
    dossier = fichier.Fichier("input", "output")
    # Alternative avec un dossier unique
    # dossier = fichier.Fichier("data", "data")
    # création de la clé de chiffrement des fichiers système
    chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])
    # Vérification des conditions d'utilisation de l'application
    if not verification.verification(dossier, terminal, chiffSys):
        return False
    # création de la clé de chiffrement des fichiers utilisateurs
    chiffFile = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
    # chargement des paramètres utilisateurs
    utilisateur = user.User(dossier, chiffSys)
    # création de l'objet d'envoi de mail
    messagerie = email.Email(utilisateur)
    # Connexion de l'utilisateur
    if not connexion.connexion(dossier, terminal, chiffSys, utilisateur, messagerie):
        return False
    while True:
        app.efface(terminal)
        # Liste des fonctions disponible
        app.afficheMenu(terminal)
        if actionMenu.action(terminal, dossier, chiffFile, messagerie, utilisateur):
            return False


start()
input(terminal.attendre("pour quitter"))
