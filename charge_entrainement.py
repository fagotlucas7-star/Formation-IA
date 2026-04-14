# Mon premier programme 
# Calculateur de charge d'entrainement

print ("=== Calculateur de charge d'entrainement ===")
print()

# On demande les informations à l'utilisateur
nom = input("quel est ton prénom ? ")
exercice = input("quel exercice ? (squat / Bench / SDT)")
un_rm = float(input("Quel est ton 1RM sur cet exercice (en Kg) ? "))
pourcentage = float(input("tu veux travailler à quel pourcentage de ton 1rm ? (ex: 75)"))
repetitions = int(input("combien de répétitions par série ? "))

# On clacule la charge à mettre sur la barre 
charge = un_rm*(pourcentage/100)

# On affiche le résultat 
print()
print("=== Résultat ===")
print(f"Salut {nom} !")
print(f"Pour ton exercice de {exercice}, tu vas travailler à {pourcentage}% de ton 1RM.")
print(f"Charge à mettre sur la barre :{charge} kg")
print(f"Tu vas faire {repetitions} répétitions par série.")
print()

# On donne un conseil un conseil selonl'intensité 
if pourcentage >= 90:
    print("⚡️ Intensité maximale : focus sur la force pure, repos long entre les séries (3-5 min).")
elif pourcentage >= 75:
    print("💪 Intensité élevée : zone de force hypertrophique, repos court (60-90 sec).")
elif pourcentage >= 60:
    print("🔥 Intensité modérée : zone d'hypetrophie, repos court (60-90 sec).")
else:
    print("🌱 Intensité faible : zone d'endurance ou de récupération, repos très court.")