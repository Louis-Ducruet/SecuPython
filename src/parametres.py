import random

import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.classe.user as user
import src.email.codeChangeEmail as message


def action(terminal: affichage.Affichage, messagerie: email.Email, utilisateur: user.User):
    menu = input(terminal.input("un", "numéro", "correspondant à un menu"))
    if menu not in ["1", "2", "3", "4", "5", "6"]:
        print(terminal.attention("Le menu \"{}\" n'existe pas".format(menu)))
        input(terminal.attendre("pour continuer"))
        return False
    app.efface(terminal)
    menu = int(menu)
    if menu % 2 == 0:
        if menu == 2:
            changeLogin(terminal, utilisateur)
            return False
        if menu == 4:
            ajoutUser(terminal, utilisateur)
            return False
        else:
            return True
    else:
        if menu == 1:
            changeEmail(terminal, messagerie, utilisateur)
            return False
        if menu == 3:
            changeMDP(terminal, utilisateur)
            return False
        else:
            suppUser(terminal, utilisateur)


def changeEmail(terminal: affichage.Affichage, messagerie: email.Email, utilisateur: user.User):
    # Afficher le titre du menu
    print(terminal.info("Changer l'adresse email"))
    # Demande de l'adresse mail
    adresse = input(terminal.input("la nouvelle", "adresse email", "de sécurité"))
    # Génération d'un code aléatoire et envoie du mail contenant le code
    code = "%06d" % random.randint(1, 999999)
    print(terminal.info("Envoie d'un mail de confirmation ..."))
    messagerie.envoyer(message.html(code), "Vérification de l'adresse email", True, adresse)
    # Demande du code
    userCode = input(terminal.input("le", "code", "reçu par email"))
    # Si bon mettre à jour l'adresse mail
    if userCode == code:
        utilisateur.changerEmail(adresse)
        print(terminal.info("Le changement est effectué."))
    # Sinon afficher message d'erreur et retour aux paramètres
    else:
        print(terminal.alerte("Code faux : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def changeLogin(terminal: affichage.Affichage, utilisateur: user.User):
    # Afficher le titre du menu
    print(terminal.info("Changer de login"))
    # Demande du nouveau login
    login = input(terminal.input("le nouveau", "login", "de connexion"))
    # S'il n'est pas vide on modifie le login du compte connecter
    if login != "":
        utilisateur.changerLogin(login)
        print(terminal.info("Le changement est effectué."))
    # Sinon message d'erreur et retour aux paramètres
    else:
        print(terminal.alerte("Login vide : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def changeMDP(terminal: affichage.Affichage, utilisateur: user.User):
    # Afficher le titre du menu
    print(terminal.info("Changer de mot de passe"))
    # Demande du nouveau mot de passe
    mdp = input(terminal.input("le nouveau", "mot de passe", "de connexion"))
    # S'il n'est pas vide on modifie le mot de passe du compte connecter
    if mdp != "":
        utilisateur.changerLogin(mdp)
        print(terminal.info("Le changement est effectué."))
    # Sinon message d'erreur et retour aux paramètres
    else:
        print(terminal.alerte("Mot de passe vide : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def ajoutUser(terminal: affichage.Affichage, utilisateur: user.User):
    # Afficher le titre du menu
    print(terminal.info("Ajouter un utilisateur"))
    # Demande du login et du mot de passe
    login = input(terminal.input("le", "login", "de connexion"))
    mdp = input(terminal.input("le nouveau", "mot de passe", "de connexion"))
    # S'ils ne sont pas vide on crée le compte
    if login != "" and mdp != "":
        utilisateur.ajouterUser(login, mdp)
        print(terminal.info("Le changement est effectué."))
    # Sinon message d'erreur et retour aux paramètres
    else:
        print(terminal.alerte("Login ou Mot de passe vide : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def suppUser(terminal: affichage.Affichage, utilisateur: user.User):
    # Afficher le titre du menu
    print(terminal.info("Supprimer ce compte"))
    # demande de confirmation
    choix = input(terminal.input("Voulez vous", "Oui ou Non", "supprimer votre compte"))
    # Si oui et s'il y a au moins deux comptes on supprime le compte actuel
    if choix == "Oui" and len(utilisateur.user['users']) > 1:
        utilisateur.supprimerUser()
        print(terminal.info("Le changement est effectué."))
        input(terminal.attendre("pour quitter"))
        # Fermeture de l'application
        exit()
    else:
        # Sinon message d'erreur et retour aux paramètres
        print(terminal.alerte("Annulation de la suppression : retour au paramètres"))
        input(terminal.attendre("pour continuer"))
