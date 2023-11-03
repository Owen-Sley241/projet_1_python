from criptage import cesar
from criptage import cesar2
from Roulette import roulette
import colorama

def menu():

    print(colorama.Fore.WHITE + "\n\t*********************[MENU]*********************:")
    print("\n\tA-Jouer à la Roulette ")
    print("\n\tB- Décalage par CESAR")
    choix = str(input("\nDonner votre choix: "))
    if choix == 'A':
        print("\n\t*********************[Jeu de la Roulette]*********************")
        print("\n\ta- Commencer à jouer  ")
        print("\n\tb- Revenir au menu principal ")
        while True:
            choix1 = str(input("\nDonner votre choix: "))
            if choix1 == 'a':
                print(roulette())
                break
            elif choix1 != 'b':
                print("Mauvaise saisie,vous êtes invité à choisir uniquement entre (a) et (b)")
            else:
                print(menu())
                break

    elif choix != 'B':
        print("Mauvaise saisie,vous êtes invité à choisir uniquement entre (A) et (B)")
        print(menu())
    else:

        choix2 = cesar()
        if choix2 == 'b':
            print(menu())
        else:
            print(cesar2())

