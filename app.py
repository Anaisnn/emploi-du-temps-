from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
print(app.template_folder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "12345"

template_dir = os.path.abspath('/Users/rebecca_dargent/PycharmProjects/emploi du temps/templates')
app.template_folder = template_dir

db = SQLAlchemy(app)

class TimeTableModel(db.Model):
    __tablename__= 'timetables'
    id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String)
    branch = db.Column(db.String)
    std = db.Column(db.String)
    div = db.Column(db.String)
    tt_name = db.Column(db.String)
    json_string = db.Column(db.String)

@app.route('/')
def index():
    return render_template('create_emploi_du_temps.html')

@app.route('/create_emploi_du_temps', methods=['GET', 'POST'])
def create_emploi_du_temps():
    if request.method == 'POST':
        college = request.form['college']
        branch = request.form['branch']
        std = request.form['std']
        div = request.form['div']
        tt_name = request.form['tt_name']
        json_string = request.form['json_string']

        timetable = TimeTableModel(college=college, branch=branch, std=std, div=div, tt_name=tt_name,
                                   json_string=json_string)
        db.session.add(timetable)
        db.session.commit()
        # Réponse JSON indiquant que le formulaire a été soumis avec succès
        return jsonify({'message': 'Formulaire soumis avec succès'})
    else:
        # Redirigez vers la page d'accueil si la méthode de la requête n'est pas POST
        return redirect(url_for('index'))
        flash('Timetable created successfully', 'success')
        return redirect(url_for('index'))
    return render_template('create_emploi_du_temps.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
