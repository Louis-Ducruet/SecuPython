class Securite:
    def __init__(self, matriceC, matriceD):
        self.matriceC = matriceC
        self.matriceD = matriceD

    def chiffrement(self, message, chiffrement):
        numberMessage = []
        chiffreMessage = []
        messageChiffre = ""
        # Transforme la chaine de caractères en nombres dans un tableau.
        for key, lettre in enumerate(list(message)):
            if key % 2 == 0:
                numberMessage.append([ord(lettre), ord(' ')])
            else:
                numberMessage[key//2][1] = ord(lettre)
        # Chiffre le tableau en ce basant sur Hill
        for key, number in enumerate(numberMessage):
            if chiffrement:
                chiffreMessage.append([(number[0] * self.matriceC[0][0] + number[1] * self.matriceC[0][1]) % 1114111])
                chiffreMessage[key].append((number[0] * self.matriceC[1][0] + number[1] * self.matriceC[1][1]) % 1114111)
            else:
                chiffreMessage.append([(number[0] * self.matriceD[0][0] + number[1] * self.matriceD[0][1]) % 1114111])
                chiffreMessage[key].append((number[0] * self.matriceD[1][0] + number[1] * self.matriceD[1][1]) % 1114111)
        # Détruit la variable numbreMessage
        numberMessage.clear()
        # Retransforme en chaine de caractères
        for chiffres in chiffreMessage:
            for chiffre in chiffres:
                messageChiffre += chr(chiffre)
        # Détruit la variable chiffreMessage
        chiffreMessage.clear()
        return messageChiffre
