import src.verification as verification
import src.securite as securite
import src.fichier as fichier
import src.couleur as couleur
import src.app as app
import os
import time

# Enable print color for windows terminal
os.system("color")
# init objects
chiffrement = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])
editeur = fichier.Fichier("input", "output")
terminal = couleur.Couleur()


def start():
    app.efface(terminal)
    verification.verificationDepart(app, chiffSys, editeur, terminal)
    # TODO Authentification
    print(terminal.info("Authentification prochainement disponible ..."))
        # TODO Vérifier l'intégriter du fichier user.json
        # TODO Demande 5 fois login et mdp
        # TODO Vérrouillage et envoie du mail
    # TODO Boucle
        # TODO Choix entre Chiffrer fichier txt/jpg ou png, Déchiffrer txt/jpg ou png, Paramètres, Se déconnecter
    print(terminal.info("Menu prochainement disponible ..."))
        # TODO Appel de la fonction choisi dans le menu


start()
time.sleep(1)
app.attendre(terminal, "pour quitter l'app.")
