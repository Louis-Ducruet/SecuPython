import json
import os.path
import time

import src.classe.securite as securite


class Fichier:
    def __init__(self, dossierEntree, dossierSortie):
        self.entree = dossierEntree
        self.sortie = dossierSortie

    def contenuFichier(self, fichier, inSrc=False):
        # Création du chemin d'accès au fichier
        dossier = ("src" if inSrc else self.entree)
        chemin = dossier + "/" + fichier
        # Ouverture du fichier en lecture et lecture
        fichier = open(chemin, "r", encoding="utf-8")
        contenu = fichier.read()
        # Fermeture du fichier
        fichier.close()
        return contenu

    def contenuImage(self, fichier):
        # Création du chemin d'accès au fichier
        chemin = self.entree + "/" + fichier
        # Ouverture du fichier en lecture binaire et lecture
        file = open(chemin, "rb")
        contenu = file.read()
        # Fermeture du fichier
        file.close()
        return contenu

    # Vérifie si les dossiers entrée et sortie existe et sont des dossiers
    def dossierExist(self):
        if os.path.exists(self.entree) and os.path.exists(self.sortie):
            if os.path.isdir(self.entree) and os.path.isdir(self.sortie):
                return True
        return False

    def ecrireFichier(self, fichier, msg, inSrc=False, isJson=False):
        # Création du chemin d'accès au fichier
        dossier = ("src" if inSrc else self.sortie)
        chemin = dossier + "/" + fichier
        # Ouverture du fichier en écriture et écrire
        fichier = open(chemin, "w", encoding="utf-8")
        json.dump(msg, fichier) if isJson else fichier.write(msg)
        # Fermeture du fichier
        fichier.close()

    # Construction du fichier time.txt
    def ecrireHeure(self, chiffSys: securite.Securite):
        valeurFichier = chiffSys.chiffrementTxt(int(time.time()))
        self.ecrireFichier("time.txt", valeurFichier, True)

    def ecrireImage(self, fichier, contenu):
        # Création du chemin d'accès au fichier
        chemin = self.sortie + "/" + fichier
        # Ouverture du fichier en écriture binaire et écrire
        file = open(chemin, "wb")
        file.write(contenu)
        # Fermeture du fichier
        file.close()

    def fichierExiste(self, fichier, inSrc=False):
        # Création du chemin d'accès au fichier
        dossier = ("src" if inSrc else self.entree)
        # Vérifie s'il existe et si c'est un fichier
        if os.path.exists(dossier + "/" + fichier):
            if os.path.isfile(dossier + "/" + fichier):
                return True
        return False
