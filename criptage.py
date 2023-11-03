def cesar():
    global choix2
    print("\n\t*********************[Décalage par CESAR]*********************")
    print("\n\ta-Donner le mot à chiffrer")
    print("\n\tb- Revenir au menu principal ")
    while True:
        choix2 =str(input("\nDonner votre choix: "))
        if choix2=='b':
            return choix2
            break
        elif choix2!='a':
            print("Mauvaise saisie,vous êtes invité à choisir uniquement entre (a) ou (b)")
        else:
            return choix2
            break

def cesar2():
    if choix2 =='a':
        print("\t\t\t[Bienvenue dans le Décalage par CESAR]")
        print("\n\t1- Cesar avec code ASCII")
        print("\n\t2- Cesar dans les 26 lettres")
        while True:
            choix3 = str(input("\nVeuiller choisir comment vous allez chiffrer votre mot : "))
            if choix3 == '1':
                mot_secret1 = str(input("saisir le mot ou le texte à chiffrer en code ASCII: "))
                print(criptage1(mot_secret1))
                break
            elif choix3 != '2':
                print("Mauvaise saisie,vous êtes invité à choisir uniquement entre (1) ou (2)")
            else:
                print(alphabet())
                break
    elif choix2 != 'b':
        print("Mauvaise saisie,vous êtes invité à choisir uniquement entre (a) ou (b)")
        print(cesar())



def criptage1(mot_secret1):

    mot_chiffrer1=""
    mot_dechiffrer1=""
    for i in mot_secret1:
        nb_lettre = ord(i)+5
        mot_chiffrer1 += chr(nb_lettre)
    print(f"\nle mot ou le texte chiffrer est: {mot_chiffrer1}")
    while True:
        voir=str(input("\nsi vous voulez voir, si votre mot ou texte a été correctement chiffré"
                       "\nvous pouvez le faire en tapant (oui) sinon taper (non) pour ne pas voir: "))
        if voir=="oui":
            for i in mot_chiffrer1 :
                nb_lettre_coder = ord(i)-5
                mot_dechiffrer1 += chr(nb_lettre_coder)
            print(f"\nle mot dechiffrer est: {mot_dechiffrer1}")
            break
        elif voir!="non":
            print("\nMauvaise saisie vous êtes invité à entrer (oui) ou (non).")
        else:
            print("\nMerci d'avoir confiance en nous :)")
            break
#mot_secret1 =str(input("saisir le mot ou le texte à chiffrer: "))
#print(criptage1(mot_secret1))


def criptage2(mot_secret2):
    mot_chiffrer2=""
    mot_dechiffrer2=""
    for i in mot_secret2:
      nb_lettre2=ord(i)+5
      if nb_lettre2<ord("a") and nb_lettre2>=ord("A")+5:
        if nb_lettre2>ord("Z"):
            nb_lettre2-=26
            mot_chiffrer2+=chr(nb_lettre2)
        else:
            mot_chiffrer2+=chr(nb_lettre2)
      else:# nb_lettre2>=ord("a")+5 and nb_lettre2<=ord("z")+5:
        if nb_lettre2>ord("z"):
            nb_lettre2-=26
            mot_chiffrer2+=chr(nb_lettre2)
        else:
            mot_chiffrer2+=chr(nb_lettre2)
    print(f"\nvotre mot chiffré est: {mot_chiffrer2}")
    for i in mot_chiffrer2:
        nb_lettre_coder2 = ord(i) - 5
        if nb_lettre_coder2 <= ord("Z"):
            if nb_lettre_coder2 < ord("A"):
                nb_lettre_coder2 += 26
                mot_dechiffrer2+= chr(nb_lettre_coder2)
            else:
                mot_dechiffrer2+= chr(nb_lettre_coder2)
        else:
            if nb_lettre_coder2 < ord("a"):
                nb_lettre_coder2+= 26
                mot_dechiffrer2+= chr(nb_lettre_coder2)
            else:
                mot_dechiffrer2+= chr(nb_lettre_coder2)
    while True:
        voir = str(input("\nsi vous voulez voir, si votre mot a été correctement chiffré"
                         "\nvous pouvez le faire en tapant (oui) sinon taper (non) pour ne pas voir: "))
        if voir == "oui":
           print(f"\nvotre mot dechiffre est: {mot_dechiffrer2}")
           break
        elif voir != "non":
            print("\nMauvaise saisie vous êtes invité à entrer (oui) ou (non).")
        else:
            print("\nMerci d'avoir confiance en nous :)")
            break
def alphabet():
    while True:
        mot_secret2 = str(input("saisir le mot à chiffrer(uniquement des lettres alphabetiques(AZ-az)): "))
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        if any(x not in alphabet for x in mot_secret2):
            print("\nErruer détecter, vous avez saisie un où plusieur caractères non alphabetique")
        else:
            print(criptage2(mot_secret2))
            break
