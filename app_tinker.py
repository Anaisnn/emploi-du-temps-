import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def generer_emploi_du_temps_apres_organisation():
    prenom = prenom_var.get()
    nom = nom_var.get()
    niveau_etude = niveau_etude_var.get()

    emploi_du_temps_window = tk.Toplevel(root)
    emploi_du_temps_window.title(f"Emploi du temps de {prenom} {nom} - {niveau_etude}")

    label_style = "Helvetica 10 bold"
    entry_style = "Helvetica 10"
    bg_color = "#f0f0f0"

    heures = [f"{heure}:00" for heure in range(8, 20)]
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]

    for i, heure in enumerate(heures):
        tk.Label(emploi_du_temps_window, text=heure, bg=bg_color, font=label_style, relief="solid", padx=10, pady=5).grid(row=i+1, column=0)

    for i, jour in enumerate(jours_semaine):
        tk.Label(emploi_du_temps_window, text=jour, bg=bg_color, font=label_style, relief="solid", padx=5, pady=5).grid(row=0, column=i+1)

        for j in range(1, len(heures) + 1):
            entry = tk.Entry(emploi_du_temps_window, font=entry_style, bd=1, relief="solid")
            entry.grid(row=j, column=i+1, padx=5, pady=5, sticky="nsew")
            emploi_du_temps_entries.append(entry)

    telecharger_button = tk.Button(emploi_du_temps_window, text="Télécharger l'emploi du temps", command=lambda: enregistrer_emploi_du_temps(emploi_du_temps_entries), bg="#4CAF50", fg="black", font="Helvetica 10 bold", relief="groove")
    telecharger_button.grid(row=len(heures)+2, columnspan=len(jours_semaine)+1, padx=10, pady=10)

def enregistrer_emploi_du_temps(entries):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for i, heure in enumerate(heures):
                file.write(heure + ":")
                for j, jour in enumerate(jours_semaine):
                    if j != 0:
                        file.write(",")
                    file.write(entries[i*len(jours_semaine)+j].get())
                file.write("\n")
        messagebox.showinfo("Enregistrement terminé", "L'emploi du temps a été enregistré avec succès.")

def afficher_emploi_du_temps():
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            for i, line in enumerate(file):
                line = line.strip().split(":")
                heure = line[0]
                activites = line[1].split(",")
                for j, activite in enumerate(activites):
                    emploi_du_temps_entries[i*len(jours_semaine)+j].insert(tk.END, activite)

root = tk.Tk()
root.title("Générateur d'emplois du temps")

prenom_var = tk.StringVar(root)
nom_var = tk.StringVar(root)
niveau_etude_var = tk.StringVar(root)

tk.Label(root, text="Prénom :", font="Helvetica 10 bold").grid(row=0, column=0, padx=10, pady=5)
prenom_entry = tk.Entry(root, textvariable=prenom_var, font="Helvetica 10")
prenom_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nom :", font="Helvetica 10 bold").grid(row=1, column=0, padx=10, pady=5)
nom_entry = tk.Entry(root, textvariable=nom_var, font="Helvetica 10")
nom_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Niveau d'étude :", font="Helvetica 10 bold").grid(row=2, column=0, padx=10, pady=5)
niveau_etude_entry = tk.Entry(root, textvariable=niveau_etude_var, font="Helvetica 10")
niveau_etude_entry.grid(row=2, column=1, padx=10, pady=5)

generer_button = tk.Button(root, text="Organiser l'emploi du temps", command=generer_emploi_du_temps_apres_organisation, font="Helvetica 10 bold", bg="#4CAF50", fg="black", relief="groove")
generer_button.grid(row=3, columnspan=2, padx=10, pady=10)

emploi_du_temps_entries = []

root.mainloop()


