import string
import random
import colorama
import maskpass


def enregistrement():
        print("1-Enregistrement : ")
        print("\ta-Email : ")
        print("\n\t\t\ta1-Introduire le nom et le prénom pour avoir \n"
              "\t\t\tl'email sous la forme de nom.prenom@centrale.tn")
        print("\n\t\t\ta2-Introduire convenablement votre email selon vos préférences en respectant le model obligatoire. ")
        while True:
             x = str(input("\nDonner votre choix: "))
             if (x == 'a1' or x == 'a2'):
              break
             else:
                 print("Mauvaise saisie vous êtes invité à saisir uniquement (a1) ou (a2).")


        def fonctionA1():
            reprendre = 'r'
            while reprendre == 'r':
             global Email
             while True:
                 nom=input("\nVotre nom s'il vous plais : ")
                 if  (nom.isalpha()==False):
                     print("Erreur de saisie, veuiller utiliser uniquement des caractères alphabetique.")
                 else:
                     prenom=input("Votre prénom s'il vous plais : ")
                     if (prenom.isalpha()==False):
                         print("Erreur de saisie, veuiller utiliser uniquement des caractères alphabetique.")
                     else:
                         Email = nom + "." + prenom + "@centrale.tn"
                         break
             print(f"\nVoicie votre email:({nom}.{prenom}@centrale.tn), si il ne vous convient pas vous pouvez toujours le modifier en tapant (r)"
                      "\nsinon taper une lettre differente de (r) pour passer à l'étape suivante.")
             reprendre = str(input("\nvoulez vous continur ou reprendre: "))


        def fonctionA2(email):
            global Email
            Email = email
            import re
            regex = re.compile(r"\b[a-zA-Z]+\.[a-zA-Z]+@centrale+\.+tn\b",)

            if re.fullmatch(regex, email):
                return True

        while True :
            match x :
                case 'a1' :
                    fonctionA1()
                    break

                case 'a2' :
                    email=input("Saisir email (Model obligatoir: nom.prenom@centrale.tn) : ")
                    if fonctionA2(email):
                        print(f"\nVotre email ({email})  est validé vous pouvez passer à l'étape suivante. ")
                        break
                    else :
                        print(f"Votre email ({email}) est invalide, veuiller reprendre en suivant le model obligatoire s'il vous plais ")
        global motPass
        print("\n1-Enregistrement : ")
        print("\tb-Password : Model obligatoire, votre mot de passe doit contenir:"
              "\n( 8 caractères obligatoire , une Majuscule, une minuscule, un Chiffre et un caractère special)")
        print("\n\t\t\t-b1-Générer automatiquement votre mot de passe. ")
        print("\n\t\t\t-b2-Introduire convenablement votre mot de passe.")

        while True:
            y = str(input("\nDonner votre choix: "))
            if (y == 'b1' or y == 'b2'):
                break
            else:
                print("Mauvaise saisie vous êtes invité à saisir uniquement (b1) ou (b2).")



        def fonctionB1():
           global motPass
           while True:
            A=string.ascii_uppercase
            B=string.ascii_lowercase
            chiff=string.digits
            spec=string.punctuation
            motPass = ("".join((random.choice(A + B + chiff + spec) for i in range(8))))
            a = any(x in string.digits for x in motPass)
            b = any(x in string.ascii_lowercase for x in motPass)
            c = any(x in string.ascii_uppercase for x in motPass)
            d = any(x in string.punctuation for x in motPass)
            if (a == True and b == True and c == True and d == True):
               print(f"\nvotre mot de passe généré automatiquement est: {motPass}")
               break
            else:
                continue

        def fonctionB2():
                import maskpass
                global motPass
                while True:
                    motPass = maskpass.askpass("saisir votre mot de passe: ")
                    a=any(x in string.digits for x in motPass)
                    b=any(x in string.ascii_lowercase for x in motPass)
                    c=any(x in string.ascii_uppercase for x in motPass)
                    d=any(x in string.punctuation for x in motPass)
                    if (a==True and b==True and c==True and d==True):
                       if len(motPass) < 8 or len(motPass) > 8:
                         print("Votre mot de passe ne dois pas contenir moins de 8 caracteres ou plus de 8 caracteres ")
                       else:
                        print(f"votre mot de passe a été valider avec succès")
                        break
                    else:
                         print("Votre mot de passe doit contenir au moins (une Majuscule, une minuscule, un Chiffre et un caractere special)")


        while True:
            match y:
                case 'b1':
                    fonctionB1()
                    break
                case 'b2':
                    fonctionB2()
                    break
def authentification():
    y = Email
    y1 = motPass
    with open("Enregistrement.txt","w") as file :
        file.write(f"{y}et{y1}")
    with open("Enregistrement.txt","r") as f1 :
        c=f1.readline().split('et')[0]
    with open("Enregistrement.txt", "r") as f2:
        c1=f2.readline().split('et')[1]
    print("\n2-Authentification:")
    while True:
            x = str(input(colorama.Fore.RED +"\n\t\t\t2a-veuiller saisir votre email pour l'authentification: "))
            if (x == c):
                print(f"\t\t\tBienvenue {c}")
                while True:
                    x1 = maskpass.askpass((colorama.Fore.GREEN + "\n\t\t\t2b-veuiller saisir votre mot de passe: "))
                    if (x1 == c1):
                        print("\t\t\tauthentification terminé.")
                        break
                    else:
                        print("\t\t\tle mot de passe saisie ne correspond pas à votre Email.")
                        continue
                break
            else:
                print(colorama.Fore.WHITE + "\t\t\tl'Email saisie ne correspond à aucun utilisateur.")
                print("\nsi vous n'avez pas encore été enregistrer vous pouvez le faire en tapant(retour) "
                      "\nsinon si vous êtes déjà enregister vous pouvez reprendre la saisie de l'email en tapant(continue)")
                enregistre=str(input("\nsaisir votre choix: "))
                if enregistre == "retour":
                    print(enregistrement())
                    print(authentification())
                    break
                elif enregistre !="continue":
                    print("Mauvaise saisie, vous allez être rediriger vers l'authentification de l'email. ")
                else:
                     continue

