import os


class Fichier:
    def __init__(self, input, output, src="src"):
        self.input = input
        self.output = output
        self.src = src

    def dossierExiste(self):
        if os.path.exists(self.input) and os.path.exists(self.output):
            if os.path.isdir(self.input) and os.path.isdir(self.output):
                return True
        return False

    def fichierExiste(self, fichier, inSrc=False):
        if inSrc:
            dossier = self.src
        else:
            dossier = self.input
        if os.path.exists(dossier + "/" + fichier):
            if os.path.isfile(dossier + "/" + fichier):
                return True
        return False

    def contenuFichier(self, fichier):
        fichier = self.input + "/" + fichier
        fichier = open(fichier, "r", encoding="utf-8")
        contenu = fichier.read()
        fichier.close()
        return contenu

    def ecrireFichier(self, fichier, message):
        fichier = self.output + "/" + fichier
        fichier = open(fichier, "w", encoding="utf-8")
        fichier.write(message)
        fichier.close()
