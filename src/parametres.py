import src.app as app
import src.classe.affichage as affichage


def action(terminal: affichage.Affichage):
    menu = input(terminal.input("un", "numéro", "correspondant à un menu"))
    if menu not in ["1", "2", "3", "4", "5", "6"]:
        print(terminal.attention("Le menu \"{}\" n'existe pas".format(menu)))
        input(terminal.attendre("pour continuer"))
        return False
    app.efface(terminal)
    menu = int(menu)
    if menu % 2 == 0:
        if menu == 2:
            pass
        if menu == 4:
            pass
        else:
            return True
    else:
        if menu == 1:
            pass
        if menu == 3:
            pass
        else:
            pass
