import tkinter as tk
from tkinter import ttk
import sqlite3
import random

# Fonction pour créer une connexion à la base de données
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

# Fonction pour exécuter une requête SQL
def execute_query(conn, query, params=None):
    cursor = conn.cursor()
    try:
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return None

# Fonction pour récupérer l'ID du dernier élève inséré
def obtenir_id_dernier_eleve_insere(conn):
    cursor = conn.cursor()
    query = "SELECT MAX(id) FROM Eleves"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0]

# Fonction pour générer l'emploi du temps d'un professeur
def generer_emploi_du_temps_prof(heures_cours):
    # Définir les créneaux horaires disponibles
    creneaux_horaires = [
        "Lundi 8h-10h",
        "Lundi 10h-12h",
        "Lundi 14h-16h",
        "Lundi 16h-18h",
        "Mardi 8h-10h",
        "Mardi 10h-12h",
        "Mardi 14h-16h",
        "Mardi 16h-18h",
        "Mercredi 8h-10h",
        "Mercredi 10h-12h",
        "Mercredi 14h-16h",
        "Mercredi 16h-18h",
        "Jeudi 8h-10h",
        "Jeudi 10h-12h",
        "Jeudi 14h-16h",
        "Jeudi 16h-18h",
        "Vendredi 8h-10h",
        "Vendredi 10h-12h",
        "Vendredi 14h-16h",
        "Vendredi 16h-18h"
    ]

    # Trier les créneaux horaires par ordre aléatoire
    random.shuffle(creneaux_horaires)

    # Sélectionner les créneaux horaires en fonction du nombre d'heures de cours
    emploi_du_temps = []
    for i in range(heures_cours):
        emploi_du_temps.append(creneaux_horaires[i])

    return emploi_du_temps

# Fonction pour générer l'emploi du temps d'un élève
def generer_emploi_du_temps_eleve(nombre_matieres):
    # Définir les créneaux horaires disponibles
    creneaux_horaires = [
        "Lundi 8h-10h",
        "Lundi 10h-12h",
        "Lundi 14h-16h",
        "Lundi 16h-18h",
        "Mardi 8h-10h",
        "Mardi 10h-12h",
        "Mardi 14h-16h",
        "Mardi 16h-18h",
        "Mercredi 8h-10h",
        "Mercredi 10h-12h",
        "Mercredi 14h-16h",
        "Mercredi 16h-18h",
        "Jeudi 8h-10h",
        "Jeudi 10h-12h",
        "Jeudi 14h-16h",
        "Jeudi 16h-18h",
        "Vendredi 8h-10h",
        "Vendredi 10h-12h",
        "Vendredi 14h-16h",
        "Vendredi 16h-18h"
    ]

    # Trier les créneaux horaires par ordre aléatoire
    random.shuffle(creneaux_horaires)

    # Sélectionner les créneaux horaires en fonction du nombre de matières
    emploi_du_temps = []
    for i in range(nombre_matieres):
        emploi_du_temps.append(creneaux_horaires[i])

    return emploi_du_temps

# Fonction pour générer l'emploi du temps d'un professeur
def generer_emploi_du_temps_professeur():
    # Récupérer les données du professeur depuis la base de données
    conn = create_connection("database.db")
    if conn is not None:
        # Modifier la requête pour utiliser des paramètres et éviter les injections SQL
        query = "SELECT * FROM Professeurs WHERE nom_prof = ? AND identifiant = ?"
        params = (nom_var.get(), numero_universite_var.get())
        result = execute_query(conn, query, params=params)  # Ajouter l'argument params pour passer les paramètres à la fonction execute_query
        if result is not None:
            heures_cours = result[0][2]  # Récupérer les heures de cours du professeur
            # Générer l'emploi du temps du professeur en utilisant les heures de cours récupérées depuis la base de données
            emploi_du_temps = generer_emploi_du_temps_prof(heures_cours)
            # Afficher l'emploi du temps du professeur dans une nouvelle fenêtre
            emploi_du_temps_window = tk.Toplevel(root)
            emploi_du_temps_window.title(f"Emploi du temps de {prenom_var.get()} {nom_var.get()}")
            emploi_du_temps_label = tk.Label(emploi_du_temps_window, text="\n".join(emploi_du_temps))
            emploi_du_temps_label.pack()

# Fonction pour générer l'emploi du temps d'un élève
def generer_emploi_du_temps_eleve():
    # Récupérer les données de l'élève depuis la base de données
    conn = create_connection("database.db")
    if conn is not None:
        # Modifier la requête pour utiliser des paramètres et éviter les injections SQL
        query = "SELECT * FROM Eleves WHERE ufr = ? AND niveau = ?"
        params = (ufr_var.get(), niveau_var.get())
        result = execute_query(conn, query, params=params)  # Ajouter l'argument params pour passer les paramètres à la fonction execute_query
        if result is not None:
            nombre_matieres = result[0][2]  # Récupérer le nombre de matières de l'élève
            # Générer l'emploi du temps de l'élève en utilisant le nombre de matières récupéré depuis la base de données
            emploi_du_temps = generer_emploi_du_temps_eleve(nombre_matieres)
            # Afficher l'emploi du temps de l'élève dans une nouvelle fenêtre
            emploi_du_temps_window = tk.Toplevel(root)
            emploi_du_temps_window.title(f"Emploi du temps de {prenom_var.get()} {nom_var.get()}")
            emploi_du_temps_label = tk.Label(emploi_du_temps_window, text="\n".join(emploi_du_temps))
            emploi_du_temps_label.pack()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur d'emplois du temps")

# Frame principal
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky="nsew")

# Label et Combobox pour choisir le statut
statut_label = ttk.Label(main_frame, text="Statut:")
statut_label.grid(row=0, column=0, sticky="w")
statut_var = tk.StringVar()
statut_combobox = ttk.Combobox(main_frame, textvariable=statut_var, values=["professeur", "eleve"])
statut_combobox.grid(row=0, column=1, padx=10, sticky="we")

# Bouton pour soumettre le formulaire
submit_button = ttk.Button(main_frame, text="Soumettre", command=lambda: generer_emploi_du_temps())
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

# Variables pour stocker les informations de l'utilisateur
prenom_var = tk.StringVar(root)
nom_var = tk.StringVar(root)
niveau_etude_var = tk.StringVar(root)
numero_universite_var = tk.StringVar(root)
ufr_var = tk.StringVar(root)
niveau_var = tk.StringVar(root)

# Demander les informations de l'utilisateur
tk.Label(root, text="Prénom :", font="Helvetica 10 bold").grid(row=2, column=0, padx=10, pady=5)
prenom_entry = tk.Entry(root, textvariable=prenom_var, font="Helvetica 10")
prenom_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Nom :", font="Helvetica 10 bold").grid(row=3, column=0, padx=10, pady=5)
nom_entry = tk.Entry(root, textvariable=nom_var, font="Helvetica 10")
nom_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Niveau d'étude :", font="Helvetica 10 bold").grid(row=4, column=0, padx=10, pady=5)
niveau_etude_entry = tk.Entry(root, textvariable=niveau_etude_var, font="Helvetica 10")
niveau_etude_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Numéro d'identifiant universitaire :", font="Helvetica 10 bold").grid(row=5, column=0, padx=10, pady=5)
numero_universite_entry = tk.Entry(root, textvariable=numero_universite_var, font="Helvetica 10")
numero_universite_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="UFR :", font="Helvetica 10 bold").grid(row=6, column=0, padx=10, pady=5)
ufr_entry = tk.Entry(root, textvariable=ufr_var, font="Helvetica 10")
ufr_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="Niveau :", font="Helvetica 10 bold").grid(row=7, column=0, padx=10, pady=5)
niveau_entry = tk.Entry(root, textvariable=niveau_var, font="Helvetica 10")
niveau_entry.grid(row=7, column=1, padx=10, pady=5)

# Fonction pour générer l'emploi du temps
def generer_emploi_du_temps():
    if statut_var.get() == "professeur":
        generer_emploi_du_temps_professeur()
    elif statut_var.get() == "eleve":
        generer_emploi_du_temps_eleve()

# Lancer la boucle principale
root.mainloop()