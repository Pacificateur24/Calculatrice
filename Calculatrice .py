def ajouter(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : Division par zéro !"

print("Bienvenue dans la calculatrice Python !")
print("Options :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choix = input("Choisissez une option (1/2/3/4) : ")

num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))

if choix == '1':
    print("Résultat :", ajouter(num1, num2))
elif choix == '2':
    print("Résultat :", soustraire(num1, num2))
elif choix == '3':
    print("Résultat :", multiplier(num1, num2))
elif choix == '4':
    print("Résultat :", diviser(num1, num2))
else:
    print("Option invalide !")