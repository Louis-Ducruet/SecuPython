import src.app as app
import src.classe.affichage as affichage
import src.classe.email as email
import src.email.codeChangeEmail as message
import src.classe.user as user
import random


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
            pass
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
            pass


def changeEmail(terminal: affichage.Affichage, messagerie: email.Email, utilisateur: user.User):
    print(terminal.info("Changer l'adresse email"))
    adresse = input(terminal.input("la nouvelle", "adresse email", "de sécurité"))
    code = "%06d" % random.randint(1, 999999)
    print(terminal.info("Envoie d'un mail de confirmation ..."))
    messagerie.envoyer(message.html(code), "Vérification de l'adresse email", True, adresse)
    userCode = input(terminal.input("le", "code", "reçu par email"))
    if userCode == code:
        utilisateur.changerEmail(adresse)
        print(terminal.info("Le changement est effectué."))
    else:
        print(terminal.alerte("Code faux : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def changeLogin(terminal: affichage.Affichage, utilisateur: user.User):
    print(terminal.info("Changer de login"))
    login = input(terminal.input("le nouveau", "login", "de connexion"))
    if login != "":
        utilisateur.changerLogin(login)
        print(terminal.info("Le changement est effectué."))
    else:
        print(terminal.alerte("Login vide : retour au paramètres"))
    input(terminal.attendre("pour continuer"))


def changeMDP(terminal: affichage.Affichage, utilisateur: user.User):
    print(terminal.info("Changer de mot de passe"))
    login = input(terminal.input("le nouveau", "mot de passe", "de connexion"))
    if login != "":
        utilisateur.changerLogin(login)
        print(terminal.info("Le changement est effectué."))
    else:
        print(terminal.alerte("Mot de passe vide : retour au paramètres"))
    input(terminal.attendre("pour continuer"))
