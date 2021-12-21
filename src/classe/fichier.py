import src.classe.securite as securite
import json
import os.path
import time


class Fichier:
    def __init__(self, dossierEntree, dossierSortie):
        self.entree = dossierEntree
        self.sortie = dossierSortie

    def contenuFichier(self, fichier, inSrc=False):
        dossier = ("src" if inSrc else self.entree)
        chemin = dossier + "/" + fichier
        fichier = open(chemin, "r", encoding="utf-8")
        contenu = fichier.read()
        fichier.close()
        return contenu

    def contenuImage(self, fichier):
        chemin = self.entree + "/" + fichier
        file = open(chemin, "rb")
        contenu = file.read()
        file.close()
        return contenu

    def dossierExist(self):
        if os.path.exists(self.entree) and os.path.exists(self.sortie):
            if os.path.isdir(self.entree) and os.path.isdir(self.sortie):
                return True
        return False

    def ecrireFichier(self, fichier, msg, inSrc=False, isJson=False):
        dossier = ("src" if inSrc else self.sortie)
        chemin = dossier + "/" + fichier
        fichier = open(chemin, "w", encoding="utf-8")
        json.dump(msg, fichier) if isJson else fichier.write(msg)
        fichier.close()

    def ecrireHeure(self, chiffSys: securite.Securite):
        valeurFichier = chiffSys.chiffrementTxt(int(time.time()))
        self.ecrireFichier("time.txt", valeurFichier, True)

    def ecrireImage(self, fichier, contenu):
        chemin = self.sortie + "/" + fichier
        file = open(chemin, "wb")
        file.write(contenu)
        file.close()

    def fichierExiste(self, fichier, inSrc=False):
        dossier = ("src" if inSrc else self.entree)
        if os.path.exists(dossier + "/" + fichier):
            if os.path.isfile(dossier + "/" + fichier):
                return True
        return False
