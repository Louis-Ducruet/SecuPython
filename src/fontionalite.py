def appelMenu(terminal, editeur, chiffrement, menu):
    if menu % 2 == 0:
        if menu == 2:
            chiffrementTxt(terminal, editeur, chiffrement, False)
        elif menu == 4:
            print(terminal.info("Menu 4 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        else:
            return True
    else:
        if menu == 1:
            chiffrementTxt(terminal, editeur, chiffrement, True)
        elif menu == 3:
            print(terminal.info("Menu 3 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        else:
            print("\n", terminal.info("Menu 5 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))


def chiffrementTxt(terminal, editeur, chiffrement, chiffre):
    menuName = "Chiffrer"
    if not chiffre:
        menuName = "Déchiffrer"
    print(terminal.info(menuName + " (.txt)"))
    fichier = input(
        terminal.input("le nom du fichier à {} dans le dossier".format(menuName.lower()), "{}".format(editeur.input)))
    print("")
    if editeur.fichierExiste(fichier) and fichier.endswith(".txt"):
        msg = chiffrement.chiffrement(editeur.contenuFichier(fichier), chiffre)
        editeur.ecrireFichier(fichier, msg)
        print(terminal.info("Fichier {} disponible dans le dossier {}".format(menuName.lower(), editeur.output)))
    else:
        print(terminal.attention("Le fichier {} n'existe pas ou n'est pas un .txt".format(fichier)))
    input(terminal.attendre("pour continuer."))
