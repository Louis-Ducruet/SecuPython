class Affichage:
    def __init__(self):
        self.annule = "\033[0m"
        self.blanc = ("\033[37m", "\033[47m")
        self.bleu = ("\033[34m", "\033[44m")
        self.cyan = ("\033[36m", "\033[46m")
        self.jaune = ("\033[33m", "\033[43m")
        self.noir = ("\033[30m", "\033[40m")
        self.rouge = ("\033[31m", "\033[41m")
        self.rose = ("\033[35m", "\033[45m")
        self.vert = ("\033[32m", "\033[42m")

        self.logoTxt = [
            "  {}███████╗███████╗ ██████╗██╗   ██╗{}██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗{}\n",
            "  {}██╔════╝██╔════╝██╔════╝██║   ██║{}██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║{}\n",
            "  {}███████╗█████╗  ██║     ██║   ██║{}██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║{}\n",
            "  {}╚════██║██╔══╝  ██║     ██║   ██║{}██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║{}\n",
            "  {}███████║███████╗╚██████╗╚██████╔╝{}██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║{}\n",
            "  {}╚══════╝╚══════╝ ╚═════╝ ╚═════╝ {}╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{}\n"
        ]

    def alerte(self, msg):
        return "{}{}Alerte : {}{}\n".format(self.rouge[1], self.blanc[0], msg, self.annule)

    def attendre(self, msg):
        return "Presser {}ENTER{} {}".format(self.jaune[0], self.annule, msg)

    def attention(self, msg):
        return "{}{}Attention : {}{}\n".format(self.jaune[1], self.noir[0], msg, self.annule)

    def info(self, msg):
        return "{}{}Info : {}{}\n".format(self.cyan[1], self.noir[0], msg, self.annule)

    def input(self, preMsg, msg, postMsg):
        return "Merci d'enter {} {}{}{} {} : ".format(preMsg, self.vert[0], msg, self.annule, postMsg)

    def logo(self):
        t = "\n"
        for line in self.logoTxt:
            t += line.format(self.cyan[0], self.jaune[0], self.annule)
        return t

    def menu(self, msgs):
        t = ""
        for id, msg in enumerate(msgs):
            t += "{} {} {} Pour {}{}{}.\n".format(self.rose[1], id + 1, self.annule, self.jaune[0], msg, self.annule)
        return t
