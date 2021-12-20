import src.app as app
import src.classe.affichage as affichage


def start():
    terminal = affichage.Affichage()
    app.efface(terminal)
    app.afficheMenu(terminal)
    input(terminal.input("", "", ""))


start()
