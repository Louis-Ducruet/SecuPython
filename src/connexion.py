import time

import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.classe.user as user
import src.email.erreurConnexion as message


def connexion(dossier: fichier.Fichier, terminal: affichage.Affichage, chiffSys: securite.Securite, user: user.User,
              email: email.Email):
    # Les 5 tentatives disponibles
    for i in range(5):
        # Affiche le titre du menu
        app.efface(terminal)
        print(terminal.info("Authentification"))
        # Affiche le nombre de tentatives disponible si au moins une erreur
        if i != 0:
            print(terminal.attention("La combinaison id/mdp est incorrect il vous reste {} tentative(s)".format(5 - i)))
        # Demande Login et mote de passe
        login = input(terminal.input("votre", "login", "de connexion"))
        mdp = input(terminal.input("votre", "mot de passe", "de connexion"))
        print("")
        # Message d'attente
        print(terminal.info("Vérification du Login / Mdp ..."))
        # Simulation de lag pour masquer l'envoie du mail lors de la 5ème itération
        if i != 4:
            time.sleep(1)
        # Sortie de boucle si utilisateur bon
        if user.userExist(login, mdp):
            return True
    # Au bout des 5 tentatives
    # MaJ du fichier de verrouillage
    dossier.ecrireHeure(chiffSys)
    # Envoie du mail d'information
    email.envoyer(message.html, "Tentative de connexion", True)
    app.efface(terminal)
    # Message d'information utilisateur
    print(terminal.alerte("Trop de tentative de connection !"))
    print(terminal.attention("Par sécurité l'app est bloquée pour 24h."))
    return False
