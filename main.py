import src.verification as verification
import src.securite as securite
import src.fichier as fichier
import src.couleur as couleur
import src.authentification as authentification
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
    if not verification.verificationDepart(app, chiffSys, editeur, terminal):
        return False
    if not authentification.auth(terminal, editeur, chiffSys):
        return False
    # TODO Boucle
        # TODO Choix entre Chiffrer fichier txt/jpg ou png, Déchiffrer txt/jpg ou png, Paramètres, Se déconnecter
    print(terminal.info("Menu prochainement disponible ..."))
        # TODO Appel de la fonction choisi dans le menu


start()
time.sleep(1)
app.attendre(terminal, "pour quitter l'app.")
