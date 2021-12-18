def appelMenu(terminal, menu):
    if menu % 2 == 0:
        if menu == 2:
            print(terminal.info("Menu 2 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        elif menu == 4:
            print(terminal.info("Menu 4 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        else:
            print(terminal.info("Menu 6 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
    else:
        if menu == 1:
            print(terminal.info("Menu 1 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        elif menu == 3:
            print(terminal.info("Menu 3 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
        else:
            print("\n", terminal.info("Menu 5 bientôt disponible ..."))
            input(terminal.attendre("pour continuer."))
