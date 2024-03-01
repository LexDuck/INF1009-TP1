"""
Tp1 Reseau
realiser dans le cadre du cour INF1009 par Felix Theriault et  Baba Tounde Moustapha
remis a David Brouillette
remis le 1 mars 2024
"""



"""
Fonction verif_input verifie que l'input donner par l'utilisateur est valide elle prend en argument soit une liste de charactere ou un integer
cond = Msq4 -> verifie pour le masque en v4
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
        try:  # capture l'erreur potentiellement lever  par la fonction int() si utilisateur ne lui donne pas un chiffre
            if cond == "Msq4": #masque
                char = abs(int(char))  # transforme l'input en chiffre
                if char <= 30: return char   # verifie pour Msq4
                raise ValueError  # si aucune condition est satisfaite exectute le bloc une ligne plus bas
            if cond == "Msq6":  # masque
                char = abs(int(char))  # transforme l'input en chiffre
                if char <= 126: return char  # verifie pour Msq4
                raise ValueError  # si aucune condition est satisfaite exectute le bloc une ligne plus bas
            if cond == "v4": #ipv4
                char = abs(int(char))  # transforme l'input en chiffre
                if char <= 255: return format(char, "08b") # verifie pour ipv4 retourne binaire
                raise ValueError  # si aucune condition est satisfaite exectute le bloc une ligne plus bas
            if cond == "v6": # condition d'erreur de l'adresse du ipv6
                for i in range(len(char)):
                    if not char[i] in "0123456789abcdef" : raise ValueError # message d'erreur en cas de de non comformiter
                bits = format(int(char,16),"016b") # farmatage en bit
                if len(bits) <= 16: return bits
                raise ValueError  # si aucune condition est satisfaite exectute le bloc une ligne plus bas


        except ValueError:  # executer si fcts int() plante ou si les conditions plus haut ne sont pas respecter
            if cond == "Msq4": print("N'est pas un chiffre entre 4 et 30")  # rejection Msq4
            if cond == "Msq6": print ("N'est pas un chiffre entre 4 et 126") # rejecction Msq6
            if cond == "v4": print("N'est pas un chiffre entre 0 et 255")  # rejection v4
            if cond == "v6": print("N'est pas un chiffre entre 0 et FFFF")  # rejection v6

            continue  # on continue a tourner en rond

        if char[0] in cond: return char[0]  # si le premier char est dans notre liste de condition on retourne sinon ...
        if cond is ["a"]:print(txt_de_confirm)  # on imprime le message formatter plus haut avec condition pi on boucle
"""Fonction prennant un string binaires et une version et retournant une addresse ip formatter"""
def binaire_a_adresse(ip,cond): # fonction qui format du binaire en adresse ip
    ipString = '' #Initilasation du string
    if cond == "ipv6": #formattage ipv6 ish
        for i in range(8):#check les blocs de 16 bits
            ipString+=(":"+format(int(ip[i*16:i*16+16], 2),'x'))#convertie en hexadecimal
        return ipString[1:]# chop chop le premier character du string
    if cond == "ipv4": # formatage ipv4
        for i in range(4): #4 bloc de 8 bits
            ipString+=(","+str(int(ip[i*8:i*8+8], 2)))# formate les bits vers du decimal
        return ipString[1:]# chop chop la virgule

class adressage:#nitialisation de la classe d'adressage#
    def __init__(self, ip_bin, masque): # le constructeur des adresse#
        self.ip = ip_bin #le ip lui meme #
        self.masque = masque # le masque des adresse 3
        self.prefix = ip_bin[:masque] # le prefixe #
        self.nBits = len(self.ip)-len(self.prefix) # le nombre de bit apres le masque

    def premiere_adresse(self):#nitialisation de la classe du la premiere adresse
        premiere_adresse = self.prefix # construction de la premiere adresse
        for i in range(self.nBits-1): #la premiere adresse utilisiable est toujours l'adresse avec 1 a la fin
            premiere_adresse += "0" #toute les reste est 0
        return premiere_adresse + "1" #retourne la premiere adresse
    def derniere_adresse(self,cond):#nitialisation de la classe du la derniere adresse
        derniere_adresse = self.prefix # construction de la dreniere adresse
        for i in range(self.nBits-1): # le dernier bits sera ajouter a la fin
            derniere_adresse += "1" # ajoute un 1 a la derniere adresse
        if cond == "v4": return derniere_adresse + "0" # resultat si ladress est un ipv4 #
        else: return derniere_adresse + "1" # resultat si ladresse est un ipv6#
    def nReseaumax(self): # les fonction de la classe d'adressage#
        nBin_reseau = "" # le nombre de reseau max en binaire#
        for i in range(self.nBits): #ajoute un 1 pour chaque bits qui nest pas le prefixe
            nBin_reseau += "1" #ajoute un 1
        return int(nBin_reseau,2)+1 # retourne le nombre de reseau en decimale
    def adresseMasque(self): # initialisation de l'adresse masque #
        adresseM = "" # variable contenant l'adresse masque
        for i in range(self.masque): #des 1 pour la longueur du masque
            adresseM += "1"  # ajoute 1 au masque
        for j in range(self.nBits): #des 0 pour le reste
            adresseM += "0" #ajoute un 0
        return adresseM  # retourne le masque

    def adresseReseau(self): # difinition de ladresse reseau
        adresseReseau = self.prefix  # ajout du prefixe
        for i in range(self.nBits): #des 0 pour le reste
            adresseReseau += "0" #clair
        return adresseReseau # retourne l'adresse reseau
    def sous_reseau_possible(self): #definition du sous reseau possible *c'est a dire toujours puisque je n'accepte pas les valeurs de masque ne permettant pas de subnet
        if self.nBits == 2: return 0 #valeur de retour si bits insuffisant
        sous_reseau = "" # variable contenant le sous reseau
        for i in range(self.nBits - 2): #deux bits doivent etre laisser pour avoir minimu 2 adresse dispo
            sous_reseau += "1" #ajout de un 1
        return int(sous_reseau, 2) + 1 # retourne de la valeur du sous reseau

ip = ""  # initialisation d'un String qui contiendra l'adresse ip en binaire

while True:  # Boucle infini pour calcul adressage q quitte le programme dans n'importe qu'elle demande d'input

    print("Voulez vous calculer l'adressage d'une adresse Ip Ipv4(a) ou Ipv6(b)?")  # asser clair
    Cond = verif_input(['a','b'])  # lit un input clavier et cond (de condition c'est francais) sera utiliser pour choisir le type d'adresse

    if Cond == "a":  # ipv4
        print("Veuillex indiquez la valeur du masque (entre 4 et 30): ")  # ... clair
        masque = verif_input("Msq4")  # trouve valeurs du masque
        print("Veuillez entrer la valeurs de l'adresse Ipv4 en decimal, un bloc a la fois: ")  # instruction a l'utilisateur
        for i in range(4): ip += verif_input("v4")  # prend un bloc de l'adresse ipv4 a la fois sur une boucle qui boucle 4 fois
        formatteur_ip = adressage(ip, masque)  #creation de l'object adressage
        print("l'adresse calculer : " + binaire_a_adresse(ip,"ipv4"))# affiche l'adresse calculer
        print("l'adresse reseau : " + binaire_a_adresse(formatteur_ip.adresseReseau(), "ipv4"))  # affiche l'adresse reseau
        print("la premiere adresse : " + binaire_a_adresse(formatteur_ip.premiere_adresse(), "ipv4")) #affiche la premiere adresse
        print("la derniere adresse : " + binaire_a_adresse(formatteur_ip.derniere_adresse("v4"), "ipv4"))#affiche la dreniere adresse
        print("l'adresse de diffusion : " + binaire_a_adresse(formatteur_ip.derniere_adresse("v6"),"ipv4"))  # affiche l'adresse  de diffusion#
        print("l'adresse du masque : " + binaire_a_adresse(formatteur_ip.adresseMasque(), "ipv4")) # affiche l'adresse de masque ipv4
        print("le nombre de reseaux maximal: "+str(formatteur_ip.nReseaumax())) # affiche le nombre de reseau max dispo
        print("le nombre de reseaux utilisable: " + str(formatteur_ip.nReseaumax()-2)) # affiche le nombre de reseau utilisable
        print("sous reseau possible: " + str(formatteur_ip.sous_reseau_possible())) #calcule le nombre de sous reseau possible
        if ip[:12] == "101011000001" or ip[:8] == "00001010" or ip[:16] == 	"1100000010101000": print("Il s'agit d'une adresse non routable") # verification si l'adresse est non routable
        elif ip[:8] == "01111111": print("Il s'agit de l'adresse de bouclage") # verifie si l'adresse est bouclable
        else: print("l'adresse est routable") # saffiche si l'adresse est routable
    if Cond == "b": #ipv6
        print("Veuillex indiquez la valeur du masque (entre 4 et 126): ")  # ... clair
        masque = verif_input("Msq6")  # trouve valeurs du masque en ipv6
        print("Veuillez entrer la valeurs de l'adresse Ipv6 en hexagonal, un bloc a la fois: ") #... clair
        for i in range(8): ip += verif_input("v6")  # prend un bloc de l'adresse ipv6 a la fois sur une boucle qui boucle 8 fois retourne binaire
        formatteur_ip = adressage(ip, masque)  #creation de l'object adressage
        print("l'adresse calculer : " + binaire_a_adresse(ip, "ipv6"))  # affiche l'adresse calculer
        print("l'adresse reseau : " + binaire_a_adresse(formatteur_ip.adresseReseau(),"ipv6"))  # affiche l'adresse reseau
        print("la premiere adresse : " + binaire_a_adresse(formatteur_ip.premiere_adresse(), "ipv6"))  #imprime la premiere adresse
        print("la derniere adresse : " + binaire_a_adresse(formatteur_ip.derniere_adresse("v6"), "ipv6"))  #imprime et formatte la derniere adresse
        print("le nombre de reseaux maximal: " + str(formatteur_ip.nReseaumax())) #imprime le nombre d'hote maximale
        print("le nombre de reseaux utilisable: " + str(formatteur_ip.nReseaumax() - 1))  # affiche le nombre de reseau utilisable
        print("sous reseau possible: " + str(formatteur_ip.sous_reseau_possible())) #calcule le nombre de sous reseau possible
        if ip[:7] == "1111110": print("L'adresse fournit est une adresse locale seulement")#commence par FC00::/7
        elif int(ip,2) == 1: print("L'adresse fournit est l'adresse de bouclage")  # ::1 est l'adresse de bouclage
        else: print("l'adresse est routable") # si ni locale ni bouclage elle est routable
        print("Une adresse ipv6 n'a pas d'adresse de diffusion") #c'est vrai


