# Fonction pour effectuer une opération
def calculer(opération, num1, num2):
    if opération == "+":
        return num1 + num2
    elif opération == "-":
        return num1 - num2
    elif opération == "*":
        return num1 * num2
    elif opération == "/":
        return num1 / num2
    else:
        return "Opération invalide."

print("Bienvenue dans la calculatrice basique !")
print("Choisissez une opération : +, -, *, /")

opération = input("Saisissez l'opération souhaitée : ")
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le second nombre : "))

résultat = calculer(opération, num1, num2)
print(f"Résultat : {résultat}")
