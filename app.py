from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "12345"

db = SQLAlchemy(app)


class TimeTableModel(db.Model):
   __tablename__ = 'timetables'
   id = db.Column(db.Integer, primary_key=True)
   college = db.Column(db.String)
   branch = db.Column(db.String)
   std = db.Column(db.String)
   div = db.Column(db.String)
   tt_name = db.Column(db.String)
   json_string = db.Column(db.String)

   def __init__(self, college, branch, std, div, tt_name, json_string):
       self.college = college
       self.branch = branch
       self.std = std
       self.div = div
       self.tt_name = tt_name
       self.json_string = json_string

@app.route('/')
def index():
    return render_template('emploi_du_temps.html')

@app.route('/generer_emploi_du_temps', methods=['GET','POST'])
def obtenir_id_dernier_eleve_insere(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT LAST_INSERT_ROWID() AS last_id")
    row = cursor.fetchone()
    if row:
        return row["last_id"]
    return N

def generer_emploi_du_temps():
    if request.method == 'POST':
        statut = request.form['statut']
        conn = create_connection("database.db")
        if conn is not None:
            if statut == "professeur":
                nom = request.form['nom']
                numero_universite = request.form['numero_universite']
                heures_cours = request.form['heures_cours']
                query = f"INSERT INTO Professeurs (nom_prof, identifiant, heures_cours) VALUES ('{nom}', '{numero_universite}', '{heures_cours}')"
                execute_query(conn, query)
            elif statut == "eleve":
                ufr = request.form['ufr']
                niveau = request.form['niveau']
                nombre_matieres = int(request.form['nombreMatieres'])
                matieres = request.form.getlist('matieres')
                horaires = request.form.getlist('horaire')
                query = f"INSERT INTO Eleves (ufr, niveau, nombre_matieres) VALUES ('{ufr}', '{niveau}', {nombre_matieres})"
                execute_query(conn, query)
                eleve_id = obtenir_id_dernier_eleve_insere(conn)

                for matiere in matieres:
                    query_matiere = f"INSERT INTO matiere (eleve_id, nom) VALUES ({eleve_id}, '{matiere}')"
                    execute_query(conn, query_matiere)

                for horaire in horaires:
                    query_horaire = f"INSERT INTO Horaires_Eleves (eleve_id, horaire) VALUES ({eleve_id}, '{horaire}')"
                    execute_query(conn, query_horaire)


                return "Données de l'élève enregistrées avec succès."






if __name__ == '__main__':
    app.run(debug=True)
