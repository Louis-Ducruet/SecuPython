import src.verification as verification
import src.securite as securite
import src.fontionalite as fonctionalite
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
    while True:
        app.efface(terminal)
        app.afficheMenu(terminal)
        menu = input(terminal.input("un nombre entre 1 et 6 pour", "choisir un menu"))
        if menu in ["1", "2", "3", "4", "5", "6"]:
            app.efface(terminal)
            menu = int(menu)
            if fonctionalite.appelMenu(terminal, editeur, chiffrement, menu):
                print(terminal.info("Déconnecter."))
                return False
        else:
            print(terminal.attention("Le menu {} n'existe pas.".format(menu)))
            input(terminal.attendre("pour continuer."))


start()
time.sleep(1)
app.attendre(terminal, "pour quitter l'app.")
