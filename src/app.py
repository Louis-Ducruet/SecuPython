import src.classe.affichage as affichage
import os


def afficheMenu(affichage: affichage.Affichage):
    menu = [
        "chiffrer (.txt)", "déchiffrer (.txt)",
        "chiffrer (.jpg, .png)", "déchiffrer (.jpg, .png)",
        "les paramètres", "se déconnecter"
    ]
    print(affichage.info("Menu SecuPython"))
    print(affichage.menu(menu))


def efface(affichage: affichage.Affichage):
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(affichage.logo())
