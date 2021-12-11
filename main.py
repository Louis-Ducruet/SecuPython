# TODO check this website https://www.generacodice.com/fr/articolo/113783/How+to+print+colored+text+in+terminal+in+Python%3F
import src.securite as securite
import src.fichier as fichier


def start():
    chiffrement = securite.Securite([[13, 24], [8, 14]], [[-7/5, 12/5], [4/5, -13/10]])
    editeur = fichier.Fichier("input", "output")
    print(
        " ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗\n"
        " ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║\n"
        " ███████╗█████╗  ██║     ██║   ██║██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║\n"
        " ╚════██║██╔══╝  ██║     ██║   ██║██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║\n"
        " ███████║███████╗╚██████╗╚██████╔╝██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║\n"
        " ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"
    )
    print(editeur.dossierExiste())
    print(editeur.fichierExiste("test.txt"))
    message = editeur.contenuFichier("test.txt")
    message = chiffrement.chiffrement(message, True)
    print(message)
    editeur.ecrireFichier("test.txt", message)
    message = chiffrement.chiffrement(message, False)
    print(message)
    input("Presser ENTRER pour quitter le programme.")


start()
