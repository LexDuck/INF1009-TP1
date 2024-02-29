"""
Fonction verif_input verifie que l'input donner par l'utilisateur est valide elle prend en argument soit une liste de charactere ou un integer
cond = MASK -> verifie pour le masque
cond = v4 -> verifie pour Ipv4
cond = v6 -> verifie pour Ipv6
"""


def verif_input(cond):
    """avec trop de commentaire c'est limite moi clair verifie pour liste d'input"""
    if cond is ["a"]: txt_de_confirm = "Veuillez entrez une option valide parmis: " + ",".join(cond)

    while True:  # boucle infinie sortie par le retour de fonction
        char = input()  # fonction retournant texte entrer par l'utilisateur  (char de charactere donc FRANCAIS)
        if len(char) == 0: continue  # empeche le programme de planter si l'utilisateur fais juste "enter"
        if char[0] == "q": exit()  # quitte le programme
        char = char.lower()  # force les valeurs en miniscule

        if cond == "MASK" or cond == "v4" or cond == "v6":  # verifie si condition 0, 1, 2
            try:  # capture l'erreur potentiellement lever  par la fonction int() si utilisateur ne lui donne pas un chiffre
                char = abs(int(char))  # transforme l'input en chiffre
                if cond == "MASK" and char >= 1 and char <= 30: return char   # verifie pour mask
                if cond == "v4" and char <= 255: return format(char, "08b") # verifie pour ipv4 retourne binaire
                if cond == "v6" and char <=65535: return format(char,"16b") # meme chose v6
                raise ValueError  # si aucune condition est satisfaite exectute le bloc une ligne plus bas
            except ValueError:  # executer si fcts int() plante ou si les conditions plus haut ne sont pas respecter
                if cond == "MASK": print("N'est pas un chiffre entre 1 et 30")  #rejection mask
                if cond == "v4": print("N'est pas un chiffre entre 0 et 255")  # rejection v4
                if cond == "v6": print("N'est pas un chiffre entre 0 et 65535")  # rejection v6
                continue  # on continue a tourner en rond

        if char[0] in cond: return char[0]  # si le premier char est dans notre liste de condition on retourne sinon ...
        print(txt_de_confirm)  # on imprime le message formatter plus haut avec condition pi on boucle


ip = ""  # initialisation d'un String qui contiendra l'adresse ip en binaire
while True:  # Boucle infini pour calcul adressage q quitte le programme dans n'importe qu'elle demande d'input

    print("Voulez vous calculer l'adressage d'une adresse Ip Ipv4(a) ou Ipv6(b)?")  # asser clair
    Cond = verif_input(['a','b'])  # lit un input clavier et cond (de condition c'est francais) sera utiliser pour choisir le type d'adresse
    print("Veuillex indiquez la valeur du masque (entre 8 et 30): ")  # ... clair
    masque = verif_input("MASK")  # trouve valeurs du masque
    if Cond == "a":  # ipv4
        print("Veuillez entrer la valeurs de l'adresse Ipv4 en decimal, un bloc a la fois: ")  # instruction a l'utilisateur
        for i in range(4): ip += verif_input("v4")  # prend un bloc de l'adresse ipv4 a la fois sur une boucle qui boucle 4 fois
    if Cond == "b":
        print("Veuillez entrer la valeurs de l'adresse Ipv6 en hexagonal, un bloc a la fois: ")
        for i in range(8): ip += verif_input("v6")  # prend un bloc de l'adresse ipv6 a la fois sur une boucle qui boucle 8 fois retourne binaire
