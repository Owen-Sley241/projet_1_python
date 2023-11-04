import main
import cowsay
import Menu

with open("Enregistrement.txt", "a") as file:
    file.write("[la liste des Emails et_mots de passes.]\n")
cowsay.fox('projet1:')
main.projet()
Menu.menu()
print("\n\n[FIN DU PROGAMME]")