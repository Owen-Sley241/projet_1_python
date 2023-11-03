
def roulette():
    import math
    import random
    print("\t\t\t\t[Bienvenue dans le Jeu de la Roulette]")
    sortir = 's'
    while sortir == 's':
        while True:
            try:
                G = float(input("\nDe combien disposez vous: "))
                if G <= 0:
                    print("Erreur de saisie, veuiller saisir des valeurs strictements positives ")
                    continue
                print(f"\nvotre solde est initialisé à {G:.3f} euro")
                break
            except ValueError:
                print("\nmauvaise saisie, vous n'avez pas entrer un nombre!!!")
        Continue = 'c'
        while Continue == 'c':
            x1 = random.randrange(1000)
            while True:
                try:
                    m = float(input("\nveuiller saisir votre mise pour ce tour: "))
                    if m > G:
                        print("vous ne disposez pas de ce montant!!!")
                    elif m <= 0:
                        print(f"Erreur votre mise doit être > 0")
                    else:
                        print(f"Votre mise est initialisé à {m:.3f} euro")
                        break
                except ValueError:
                    print("Erreur veuiller reprendre avec des numeros s'il vous plait!!! ")
            G = G - m
            while True:
                try:
                    y = int(input("\nchoisiser un numero compris entre 0 et 999 sur lequel sera placer votre mise: "))
                    if y < 0:
                        print("Erreur votre numero n'est pas compris entre 0 et 999")
                    elif y > 999:
                        print("Erreur votre numero n'est pas compris entre 0 et 999")
                    else:
                        print(f"le numero sur lequel votre mise sera placer est {y} ")
                        break
                except ValueError:
                    print("mauvaise saisie veuiller saisir un nombre compris entre 0 et 999")
            print(f"\nle numero gagnant est {x1}")
            if x1 == y:
                print("félicitation vous avez fait le bon choix")
                G = math.ceil(G + (m * 3))
            elif x1 % 2 == 0:
                if y % 2 == 0:
                    print("félicitation vous n'avez pas trouver le bon numero mais vous avez trouver une bonne couleur de case (le rouge)")
                    G = math.ceil(G + m + (m * 0.5))
                else:
                    print("vous avez perdu ce tour!!!")
                    m = 0
            elif y % 2 != 0:
                print("félicitation vous n'avez pas trouver le bon numero mais vous avez trouver une bonne couleur de case (le noir)")
                G = math.ceil( G + m + (m * 0.5))
            else:
                print("vous avez perdu ce tour!!!")
                m = 0
            print("\n\t\t************************[Fin du tour]************************ ")
            if G == 0:
                print(f"\nla partie est terminé et vous avez perdu car votre solde est egal à {G} euro")
                break
            else:
                print(f"\n la valeur de votre solde est actuellement {G:.2f} euro")
            Continue = str(input("Voulez vous continuer avec un nouveau tour?(si oui entrer(c) sinon entrer une lettre differente de (c)): "))
        print("\n\t\t************************[Fin de la partie]*******************************")
        sortir = str(input("si vous voulez relancer une nouvelle partie entrer(s) sinon entrer une valeur differente pour sortir :"))
    print("\n vous avez quitté la partie, merci de votre participation ")

