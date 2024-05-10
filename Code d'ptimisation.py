import tkinter as tk

def collect_preferences():
    preferences = {
        "matiere_preferee": matiere_preferee_entry.get(),
        "horaire_ideal": horaire_ideal_entry.get(),
        "horaire_professeur": horaire_professeur_entry.get()
    }
    poids_preferences = {
        "matiere_preferee": 2,
        "horaire_ideal": 1,
        "horaire_professeur": 3
    }
    return preferences, poids_preferences

def check_schedule_conflicts(preferences):
    user_schedule = {
        "horaire_ideal": preferences["horaire_ideal"],
        "horaire_professeur": preferences["horaire_professeur"]
    }

    # Exemple de logique de vérification de conflits
    if user_schedule["horaire_ideal"] == user_schedule["horaire_professeur"]:
        print("Conflit d'horaire : L'horaire idéal et l'horaire du professeur se chevauchent.")
        # Proposez des solutions pour résoudre le conflit, par exemple, modifier l'horaire idéal ou choisir un autre cours.
    else:
        print("Pas de conflit d'horaire.")

def check_break_times(preferences):
    duree_pause = 15  # Durée de la pause en minutes
    debut_cours_minutes = int(preferences["horaire_ideal"].split(":")[0]) * 60 + int(preferences["horaire_ideal"].split(":")[1])
    fin_cours_minutes = int(preferences["horaire_professeur"].split(":")[0]) * 60 + int(preferences["horaire_professeur"].split(":")[1])

    if fin_cours_minutes - debut_cours_minutes < duree_pause:
        print("Attention : Le temps entre les cours est inférieur à la durée de la pause.")


def check_workload_balance(preferences):
    # On suppose que les horaires sont donnés sous forme de listes de tuples (jour, heure_debut, heure_fin)
    horaires = [
        ("Lundi", "8:00", "10:00"),
        ("Lundi", "14:00", "16:00"),
        ("Mardi", "10:00", "12:00"),
        ("Mercredi", "8:00", "10:00"),
        ("Mercredi", "14:00", "16:00"),
        ("Vendredi", "8:00", "10:00"),
        ("Vendredi", "14:00", "16:00")
    ]

    # Créer un dictionnaire pour compter le nombre de cours par jour
    cours_par_jour = {}
    for jour in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]:
        cours_par_jour[jour] = 0

    # Compter le nombre de cours par jour
    for cours in horaires:
        jour = cours[0]
        cours_par_jour[jour] += 1

    # Calculer la moyenne du nombre de cours par jour
    moyenne_cours_par_jour = sum(cours_par_jour.values()) / len(cours_par_jour)

    # Comparer le nombre de cours par jour à la moyenne
    for jour, nombre_cours in cours_par_jour.items():
        if nombre_cours < moyenne_cours_par_jour:
            print(f"Attention : Le {jour} a moins de cours que la moyenne.")
        elif nombre_cours > moyenne_cours_par_jour:
            print(f"Attention : Le {jour} a plus de cours que la moyenne.")
        else:
            print(f"Le {jour} a un nombre de cours équilibré.")

def offer_flexibility(preferences):
    # Logique pour offrir des solutions alternatives en cas de conflits ou de contraintes imprévues
    # Cette fonction pourrait proposer des horaires alternatifs, des cours en ligne ou d'autres solutions pour résoudre les conflits.
    print("Offrir des solutions alternatives en cas de conflits ou de contraintes imprévues.")


def planifier_evenement():
    preferences, poids_preferences = collect_preferences()
    print("Préférence matière préférée :", preferences["matiere_preferee"])
    print("Préférence horaire idéal :", preferences["horaire_ideal"])
    print("Horaire choisi par le professeur :", preferences["horaire_professeur"])

    check_schedule_conflicts(preferences)
    check_break_times(preferences)

# Interface utilisateur
root = tk.Tk()
root.title("Planification d'événement")

matiere_preferee_label = tk.Label(root, text="Matière préférée :")
matiere_preferee_label.pack()
matiere_preferee_entry = tk.Entry(root)
matiere_preferee_entry.pack()

horaire_ideal_label = tk.Label(root, text="Horaire idéal :")
horaire_ideal_label.pack()
horaire_ideal_entry = tk.Entry(root)
horaire_ideal_entry.pack()

horaire_professeur_label = tk.Label(root, text="Horaire choisi par le professeur :")
horaire_professeur_label.pack()
horaire_professeur_entry = tk.Entry(root)
horaire_professeur_entry.pack()

planifier_button = tk.Button(root, text="Planifier l'événement", command=planifier_evenement)
planifier_button.pack()

root.mainloop()
