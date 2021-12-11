# TODO check this website https://www.generacodice.com/fr/articolo/113783/How+to+print+colored+text+in+terminal+in+Python%3F
import src.securite as securite

def start():
    print(
    " ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗\n",
    "██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║\n",
    "███████╗█████╗  ██║     ██║   ██║██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║\n",
    "╚════██║██╔══╝  ██║     ██║   ██║██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║\n",
    "███████║███████╗╚██████╗╚██████╔╝██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║\n",
    "╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"
    )
    msg = securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]]).chiffrement("Coucou Paul comment ça ?", True)
    print(msg)
    print(securite.Securite([[2, 5], [1, 3]], [[3, -5], [-1, 2]]).chiffrement(msg, False))
    input("Presser ENTRER pour quitter le programme.")


start()
