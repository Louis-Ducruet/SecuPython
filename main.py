import src.app as app
import src.classe.affichage as affichage
import src.classe.fichier as fichier
import src.classe.securite as securite
import src.verification as verification

dossier = fichier.Fichier("input", "output")
terminal = affichage.Affichage()
chiffFile = securite.Securite([[13, 24], [8, 14]], [[-7 / 5, 12 / 5], [4 / 5, -13 / 10]])
chiffSys = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]])


def start():
    app.efface(terminal)
    if not verification.verification(dossier, terminal, chiffSys):
        return False
    app.afficheMenu(terminal)


start()
input(terminal.input("", "", ""))
