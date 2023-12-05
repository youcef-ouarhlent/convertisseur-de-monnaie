from forex_python.converter import CurrencyRates

c = CurrencyRates()
historique = []
devises_preferees = {}  # Dictionnaire pour stocker les devises préférées de l'utilisateur

def ajouter_devise_preferee(devise, taux):
    devises_preferees[devise] = taux
    print(f"Devise {devise} ajoutée avec un taux de conversion de {taux}")

# Ajouter des devises par défaut
ajouter_devise_preferee('USD', 1.0)
ajouter_devise_preferee('EUR', 0.85)
ajouter_devise_preferee('GBP', 0.75)

while True:
    somme = int(input("Donnez une somme à convertir (0 pour quitter) : "))
    if somme == 0:
        break
    
    unitesource = input("Origine: Donnez le type d'argent : ").upper()
    unitedestinataire = input("Vous voulez le convertir en quoi ? ").upper()

    print(unitesource, "à", unitedestinataire, ":", somme)
    
    try:
        if unitesource in devises_preferees:
            taux_conversion = devises_preferees[unitesource]
            resultat = somme * taux_conversion
        else:
            resultat = c.convert(unitesource, unitedestinataire, somme)
        
        print("Résultat :", resultat)

        # Enregistrer l'historique de la conversion
        conversion = {
            "Montant": somme,
            "De": unitesource,
            "À": unitedestinataire,
            "Résultat": resultat
        }
        historique.append(conversion)
    
    except ValueError as e:
        print(f"Impossible de convertir : {e}")

    # Proposer à l'utilisateur d'ajouter une devise avec son taux de conversion
    ajouter_nouvelle_devise = input("Voulez-vous ajouter une nouvelle devise ? (O/N) : ").upper()
    if ajouter_nouvelle_devise == 'O':
        nouvelle_devise = input("Entrez le code de la nouvelle devise : ").upper()
        nouveau_taux = float(input(f"Entrez le taux de conversion de {unitesource} vers {nouvelle_devise} : "))
        ajouter_devise_preferee(nouvelle_devise, nouveau_taux)

# Afficher l'historique des conversions
print("\nHistorique des conversions :")
for index, conversion in enumerate(historique, start=1):
    print(f"Conversion {index}: {conversion}")
