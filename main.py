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
        print(f"{terminal.bRouge}Erreur : Le fichier user.txt n'existe pas !{terminal.annule}\n")
        return False
    # Vérification s'il y a eu une tentative de hack
    if not editeur.fichierExiste("time.txt", True):
        print(f"{terminal.bRouge}Erreur : Le fichier time.txt n'existe pas !{terminal.annule}\n")
        editeur.ecrireFichier("time.txt", chiffSys.chiffrement(int(time.time()), True), True)
        print(f"{terminal.bJaune}{terminal.fNoir}Création du fichier : Pour éviter toute tentative de fraude l'app est bloquer pour {terminal.fRouge}24h{terminal.annule}.\n")
        return False
    if not app.secuTime(editeur, chiffSys, terminal):
        print(f"{terminal.bRouge}Erreur : Une tentative de hack a bloqué l'application pour 24h!{terminal.annule}\n")
        return False
    # Autentification
    print(f"{terminal.bCyan}{terminal.fNoir}Info : Authentification prochainement disponible ...{terminal.annule}\n")
    # Vérification si les dossiers input et output existe
    if not editeur.dossierExiste():
        print(
            f"{terminal.bRouge}Erreur : Le ou les dossiers {editeur.input} et {editeur.output} n'existe pas !{terminal.annule}\n")
        return False
    # Choix entre Chiffrer, Déchiffrer et Paramètres
    print(f"{terminal.bCyan}{terminal.fNoir}Info : Menu prochainement disponible ...{terminal.annule}\n")


start()
input(f"Presser {terminal.bNoir}{terminal.fJaune}ENTRER{terminal.annule} pour quitter le programme.")
