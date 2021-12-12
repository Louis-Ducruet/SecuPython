import src.securite as securite
import src.fichier as fichier
import src.couleur as couleur
import src.app as app
import os

# Enable print color for windows terminal
os.system("color")
# init objects
chiffrement = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
editeur = fichier.Fichier("input", "output")
terminal = couleur.Couleur()


def start():
    app.efface(terminal)
    # Vérification si les données utilisateurs existe
    if not editeur.fichierExiste("user.txt", True):
        print(f"{terminal.bRouge}Erreur : Le fichier user.txt n'existe pas !{terminal.annule}\n")
        return False
    # Vérification s'il y a eu une tentative de hack

    # Autentification

    # Vérification si les dossiers input et output existe
    if not editeur.dossierExiste():
        print(f"{terminal.bRouge}Erreur : Le ou les dossiers {editeur.input} et {editeur.output} n'existe pas !{terminal.annule}\n")
        return False
    # Choix entre Chiffrer, Déchiffrer et Paramètres
    print(editeur.fichierExiste("test.txt"))
    message = editeur.contenuFichier("test.txt")
    message = chiffrement.chiffrement(message, True)
    print(message)
    editeur.ecrireFichier("test.txt", message)
    message = chiffrement.chiffrement(message, False)
    print(message)


start()
input(f"Presser {terminal.bNoir}{terminal.fJaune}ENTRER{terminal.annule} pour quitter le programme.")
