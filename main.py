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
    # Vérification si les données utilisateurs existe
    if not editeur.fichierExiste("user.txt", True):
        print(terminal.alerte("Le fichier user.txt n'existe pas !"))
        return False
    # Vérification s'il y a eu une tentative de hack
    if not editeur.fichierExiste("time.txt", True):
        print(terminal.alerte("Le fichier time.txt n'existe pas !"))
        editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
        print(terminal.attention("Création du fichier, par sécurité l'app est bloquée pour 24h."))
        return False
    if not app.secuTime(editeur, chiffSys, terminal):
        print(terminal.alerte("Suite à une tentative de hack l'app est bloquée pendant 24h !"))
        return False
    # Autentification
    print(terminal.info("Authentification prochainement disponible ..."))
    # Vérification si les dossiers input et output existe
    if not editeur.dossierExiste():
        print(terminal.alerte("Le ou les dossier(s) {} {} n'existe(nt) pas".format(editeur.input, editeur.output)))
        return False
    # Choix entre Chiffrer, Déchiffrer et Paramètres
    print(terminal.info("Menu prochainement disponible ..."))


start()
input(f"Presser {terminal.bNoir}{terminal.fJaune}ENTRER{terminal.annule} pour quitter le programme.")
