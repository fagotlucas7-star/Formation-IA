#  Enregistreur de seances d'entrainement
# Demande les détails de plusieurs series et affiche un bilan

print("=== Enregistreur de seances d'entrainement ===")
print()

# 1. Demander le prenom du client 
nom = input("Prenom du client ? ")

# 2. Demander le nombre de series 
nombre_series = int(input("combien de series ?"))

# 3. Creer 3 listes vides pour stocker les donnees 
exercices = []
charges =  []
repetitions = []

# 4. Boucler pour demander les infos de chaque serie 
for i in range(nombre_series):
    print()
    print(f"--- Serie {i + 1} ---")

    exercice = input("Exercice ? ")
    exercices.append(exercice)

    charge = float(input("Charges en KG "))
    charges.append(charge)

    reps = int(input("repetitions ? "))
    repetitions.append(reps)


# 5. Calculer les statistiques
print()
print("=== Bilan de la seance ===")

moyenne= sum(charges) / len(charges)

charge_max = max(charges)

min_charge = min(charges)

# 6. Calculer le volume total (charge * repetitions pour chaque serie, puis somme)
volume_total = 0
# A toi : boucler sur les indices (0, 1, 2...) pour recuperer charges[i] et repetitions[i]
# puis ajouter charges[i] * repetitions[i] a volume_total
for i in range(len(charges)):
    volume_total += charges [i]* repetitions[i]

# 7. Afficher le bilan
print()
print(f"Nombre de series : {nombre_series} ")
print(f"charge moyenne : {moyenne} kg")
print(f"charge max : {charge_max} kg")
print(f"min_charge : {min_charge} kg ")
# A toi : afficher les autres statistiques avec des f-strings

# 8. Donner un petit conseil selon le nombre de series

if nombre_series >= 6 :
    print("Grosse seance, recuperation importante")
elif nombre_series >= 4 :
    print("Seance equilibree")
else:
    print("Seance legere; tu peux pousser plus")
