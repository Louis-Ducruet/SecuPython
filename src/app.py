import os

import src.classe.affichage as affichage


def afficheMenu(affichage: affichage.Affichage):
    menu = [
        "chiffrer (.txt)", "déchiffrer (.txt)", "chiffrer (.jpg, .jpeg, .png)", "déchiffrer (.jpg, .jpeg, .png)",
        "les paramètres", "se déconnecter"
    ]
    print(affichage.info("Menu SecuPython"))
    print(affichage.menu(menu))


def afficheParametre(affichage: affichage.Affichage):
    menu = [
        "changer d'adresse mail", "changer de login", "changer de mot de passe", "ajouter un utilisateur",
        "supprimer ce compte", "retour au menu principale"
    ]
    print(affichage.info("Paramètres SecuPython"))
    print(affichage.menu(menu))


def efface(affichage: affichage.Affichage):
    os.system('cls') if os.name == 'nt' else os.system('clear')
    print(affichage.logo())
