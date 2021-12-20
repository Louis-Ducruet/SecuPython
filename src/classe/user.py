import src.classe.fichier as fichier
import src.classe.securite as securite
import json


class User:
    def __init__(self, dossier: fichier.Fichier, securite: securite.Securite):
        self.dossier = dossier
        self.securite = securite
        contenu = self.dossier.contenuFichier("user.json", True)
        contenu = self.securite.chiffrementTxt(contenu, False)
        self.user = json.loads(contenu)
        self.currentUser = 0
        self.email = self.user['default-email']

    def ajouterUser(self, login, motDePasse):
        self.user['users'].append({"login": login, "password": motDePasse})
        self.ecrireFichier()

    def changerEmail(self, email):
        self.user['default-email'] = email
        self.ecrireFichier()

    def changerLogin(self, login):
        self.user['users'][self.currentUser]['login'] = login
        self.ecrireFichier()

    def changerMotPasse(self, motDePasse):
        self.user['users'][self.currentUser]['password'] = motDePasse
        self.ecrireFichier()

    def ecrireFichier(self):
        self.dossier.ecrireFichier("user.json", self.user, True, True)
        contenu = self.dossier.contenuFichier("user.json", True)
        contenu = self.securite.chiffrementTxt(contenu)
        self.dossier.ecrireFichier("user.json", contenu, True)

    def supprimerUser(self):
        if len(self.user['users']) > 1:
            del(self.user['users'][self.currentUser])
            self.ecrireFichier()
            return True
        return False

    def userExist(self, login, motDePasse):
        for id, compte in enumerate(self.user['users']):
            if login == compte['login'] and motDePasse == compte['password']:
                self.currentUser = id
                return True
        return False
