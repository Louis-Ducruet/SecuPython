class Securite:
    def __init__(self, matrice1, matrice2):
        self.matrice1 = matrice1
        self.matrice2 = matrice2

    def chiffrementTxt(self, msg, chiffrement=True):
        numberMessage = []
        chiffreMessage = []
        messageChiffre = ""
        # Transforme la chaine de caractères en nombres dans un tableau.
        for key, lettre in enumerate(list(str(msg))):
            if key % 2 == 0:
                numberMessage.append([ord(lettre), ord(' ')])
            else:
                numberMessage[key // 2][1] = ord(lettre)
        # Chiffre le tableau en ce basant sur Hill
        for key, number in enumerate(numberMessage):
            if chiffrement:
                matrice = self.matrice1
            else:
                matrice = self.matrice2
            chiffreMessage.append([(number[0] * matrice[0][0] + number[1] * matrice[0][1]) % 1114111])
            chiffreMessage[key].append((number[0] * matrice[1][0] + number[1] * matrice[1][1]) % 1114111)
        # Détruit la variable numbreMessage
        numberMessage.clear()
        # Retransforme en chaine de caractères
        for chiffres in chiffreMessage:
            for chiffre in chiffres:
                # int() pour fixer les problèmes d'arrondi des float
                messageChiffre += chr(int(chiffre))
        # Détruit la variable chiffreMessage
        chiffreMessage.clear()
        return messageChiffre
