class Couleur:
    def __init__(self):
        self.fNoir = "\033[30m"
        self.fRouge = "\033[31m"
        self.fVert = "\033[32m"
        self.fJaune = "\033[33m"
        self.fBleu = "\033[34m"
        self.fRose = "\033[35m"
        self.fCyan = "\033[36m"
        self.fBlanc = "\033[37m"
        self.bNoir = "\033[40m"
        self.bRouge = "\033[41m"
        self.bVert = "\033[42m"
        self.bJaune = "\033[43m"
        self.bBleu = "\033[44m"
        self.bRose = "\033[45m"
        self.bCyan = "\033[46m"
        self.bBlanc = "\033[47m"
        self.annule = "\033[0m"
        self.logoTxt = [
            "  {}███████╗███████╗ ██████╗██╗   ██╗{}██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗{}\n",
            "  {}██╔════╝██╔════╝██╔════╝██║   ██║{}██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║{}\n",
            "  {}███████╗█████╗  ██║     ██║   ██║{}██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║{}\n",
            "  {}╚════██║██╔══╝  ██║     ██║   ██║{}██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║{}\n",
            "  {}███████║███████╗╚██████╗╚██████╔╝{}██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║{}\n",
            "  {}╚══════╝╚══════╝ ╚═════╝ ╚═════╝ {}╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{}\n"
        ]

    def logo(self):
        t = "\n"
        for line in self.logoTxt:
            t += line.format(self.fCyan, self.fJaune, self.annule)
        return t

    def alerte(self, message):
        return "{}{}Alerte : {}{}\n".format(self.bRouge, self.fBlanc, message, self.annule)

    def attention(self, message):
        return "{}{}Attention : {}{}\n".format(self.bJaune, self.fNoir, message, self.annule)

    def info(self, message):
        return "{}{}Info : {}{}\n".format(self.bCyan, self.fNoir, message, self.annule)

    def attendre(self, message):
        return "Presser {}ENTER{} {}".format(self.fJaune, self.annule, message)