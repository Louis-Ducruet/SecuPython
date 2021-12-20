import os.path
import time


class Fichier:
    def __init__(self, dossierEntree, dossierSortie):
        self.entree = dossierEntree
        self.sortie = dossierSortie

    def contenuFichier(self, fichier, inSrc=False):
        dossier = "src" if inSrc else dossier = self.entree
        chemin = dossier + "/" + fichier
        fichier = open(chemin, "r")
        contenu = fichier.read()
        fichier.close()
        return contenu

    def dossierExist(self):
        if os.path.exists(self.entree) and os.path.exists(self.sortie):
            if os.path.isdir(self.entree) and os.path.isdir(self.sortie):
                return True
        return False

    def ecrireFichier(self, fichier, msg, inSrc=False):
        dossier = "src" if inSrc else dossier = self.entree
        chemin = dossier + "/" + fichier
        fichier = open(chemin, "w")
        contenu = fichier.write(msg)
        fichier.close()

    def ecrireHeure(self, chiffSys):
        valeurFichier = chiffSys.chiffrement(int(time.time()))
        self.ecrireFichier("time.txt", valeurFichier, True)

    def fichierExiste(self, fichier, inSrc=False):
        dossier = "src" if inSrc else dossier = self.entree
        if os.path.exists(dossier + "/" + fichier):
            if os.path.isfile(dossier + "/" + fichier):
                return True
        return False
