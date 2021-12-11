# TODO check this website https://www.generacodice.com/fr/articolo/113783/How+to+print+colored+text+in+terminal+in+Python%3F

def start():
    print('\033[31m' + 'Texte rouge ' + '\033[0m')
    input("Presser " + "\033[93m" + "ENTRER" + "\033[0m" + " pour quitter le programme.")


start()
