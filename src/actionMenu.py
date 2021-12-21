import src.app as app
import src.classe.affichage as affichage
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.parametres as parametres


def action(terminal: affichage.Affichage, dossier: fichier.Fichier, chiffrement: securite.Securite):
    menu = input(terminal.input("un", "numéro", "correspondant à un menu"))
    if menu not in ["1", "2", "3", "4", "5", "6"]:
        print(terminal.attention("Le menu \"{}\" n'existe pas".format(menu)))
        input(terminal.attendre("pour continuer"))
        return False
    app.efface(terminal)
    menu = int(menu)
    if menu % 2 == 0:
        if menu == 2:
            chiffrementTxt(terminal, dossier, chiffrement, False)
            return False
        if menu == 4:
            pass
        else:
            print(terminal.info("Vous êtes déconnecté(e)"))
            return True
    else:
        if menu == 1:
            chiffrementTxt(terminal, dossier, chiffrement, True)
            return False
        if menu == 3:
            pass
        else:
            while True:
                app.efface(terminal)
                app.afficheParametre(terminal)
                if parametres.action(terminal):
                    return False


def chiffrementTxt(terminal: affichage.Affichage, dossier: fichier.Fichier, chiffrement: securite.Securite, chiffre):
    menuName = "Chiffrer" if chiffre else "Déchiffrer"
    print(terminal.info(menuName + " (.txt)"))
    file = input(
        terminal.input("le nom du fichier à {} dans le dossier".format(menuName.lower()), "{}".format(dossier.entree),
                       ""))
    print("")
    if dossier.fichierExiste(file) and file.endswith(".txt"):
        msg = chiffrement.chiffrementTxt(dossier.contenuFichier(file), chiffre)
        dossier.ecrireFichier(file, msg)
        print(terminal.info("Fichier {} disponible dans le dossier {}".format(menuName.lower(), dossier.sortie)))
    else:
        print(terminal.attention("Le fichier {} n'existe pas ou n'est pas un .txt".format(file)))
    input(terminal.attendre("pour continuer."))
