


"""
Fonction verif_input verifie que l'input donner par l'utilisateur est valide elle prend en argument soit une liste de charactere ou un integer
cond = 0 -> verifie pour le masque
cond = 1 -> verifie pour l'adresse ip IPV4
"""
def verif_input(cond):
    if type(cond)!= int: Texte_de_confirmation = "Veuillez entrez une option valide parmis: " + ",".join(cond) #formate le texte de rejection utiliser plus bas
    while True: #boucle infinie sortie par le retour de fonction
        char = input() #fonction retournant texte entrer par l'utilisateur  (char de charactere donc FRANCAIS)
        if len(char) == 0: continue  #empeche le programme de planter si l'utilisateur fais juste "enter"
        char = char.lower() #force les valeurs en miniscule
        if char[0] is "q": exit() #quitte le programme
        if cond == 0 or cond == 1: #verifie si condition 0 ou 1
            try: #capture l'erreur potentiellement lever  par la fonction int() si utilisateur ne lui donne pas un chiffre
                char = int(char) #transforme l'input en chiffre
                if cond == 0 and char >= 8 and char <= 30: return char #verifie pour cond -> 0
                if cond == 1 and char >= 0 and char <= 255:return char #verifie pour cond -> 0
                raise ValueError #si aucune condition est satisfaite exectute le bloc une ligne plus bas
            except ValueError: #executer si fcts int() plante ou si les conditions plus haut ne sont pas respecter
                if cond == 0:print("N'est pas un chiffre entre 8 et 30") #message pour condition 1
                if cond == 1:print("N'est pas un chiffre entre 0 et 255")#message pour condition 2
                continue #on continue a tourner en rond

        if char[0] in cond: return char[0] #si le premier char est dans notre liste de condition on retourne sinon ...
        print(Texte_de_confirmation) # on imprime le message formatter plus haut avec condition pi on boucle

Drapeau = True  # Sert a sortir de la boucle a la fin de l'execution
while Drapeau:  # Boucle infini pour calcul adressage
    masque = -1  #initialisation de la variable du masque qui sera prise plus bas
    ip = [-1,-1,-1,-1] #initialisation d'un tableau qui contiendra l'adresse ip
    print("Voulez vous calculer l'adressage d'une adresse Ip Ipv4(a) ou Ipv6(b)?")  # asser clair
    Cond = verif_input(['a','b'])  # lit un input clavier et cond (de condition c'est francais) sera utiliser pour choisir le type d'adresse
    if Cond is "a": #ipv4
        print("Veuillex indiquez la valeur du masque (entre 8 et 30): ")# ... clair
        masque = verif_input(0) #trouve valeurs du masque
        print("Veuillez entrex la valeurs de l'adresse Ipv4 en decimal, un bloc a la fois: ") #instruction a l'utilisateur
        for i in range(4): ip[i] = verif_input(1) #prend un bloc de l'adresse ipv4 a la fois sur une boucle qui bouclle 4 fois

